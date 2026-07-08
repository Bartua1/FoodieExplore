import os
import sqlite3
import uuid
from datetime import datetime

DEFAULT_DB_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
DEFAULT_DB_PATH = os.path.join(DEFAULT_DB_DIR, "explorer.db")

def get_db_connection(db_path=DEFAULT_DB_PATH):
    """Establishes a connection to the SQLite database."""
    # Ensure the directory exists
    db_dir = os.path.dirname(db_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
        
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path=DEFAULT_DB_PATH):
    """Initializes the database schema if it doesn't already exist."""
    conn = get_db_connection(db_path)
    cursor = conn.cursor()
    
    # Create the candidate_restaurants table matching global_restaurants + extra columns
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidate_restaurants (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        cuisine_type TEXT,
        price_level INTEGER,
        lat REAL NOT NULL,
        lng REAL NOT NULL,
        address TEXT,
        cover_image_url TEXT,
        is_promoted INTEGER NOT NULL DEFAULT 0,
        promotion_end_at TEXT,
        created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
        updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
        likes_count INTEGER NOT NULL DEFAULT 0,
        views_count INTEGER NOT NULL DEFAULT 0,
        validation_status TEXT NOT NULL DEFAULT 'pending',
        neighborhood TEXT NOT NULL,
        osm_id TEXT UNIQUE
    )
    """)
    
    conn.commit()
    conn.close()
    print(f"Database initialized at: {db_path}")

def insert_candidate_restaurant(conn, restaurant):
    """
    Inserts a candidate restaurant dict into the database.
    If the osm_id already exists, it is ignored to prevent duplicates and keep existing validation.
    
    restaurant dict should contain:
        name, lat, lng, neighborhood
    optional:
        description, cuisine_type, price_level, address, cover_image_url, osm_id, is_promoted, promotion_end_at
    """
    cursor = conn.cursor()
    
    # Generate local UUID if not provided
    rest_id = restaurant.get("id") or str(uuid.uuid4())
    
    name = restaurant.get("name")
    description = restaurant.get("description")
    cuisine_type = restaurant.get("cuisine_type")
    price_level = restaurant.get("price_level")
    lat = restaurant.get("lat")
    lng = restaurant.get("lng")
    address = restaurant.get("address")
    cover_image_url = restaurant.get("cover_image_url")
    is_promoted = 1 if restaurant.get("is_promoted") else 0
    promotion_end_at = restaurant.get("promotion_end_at")
    validation_status = restaurant.get("validation_status") or "pending"
    neighborhood = restaurant.get("neighborhood")
    osm_id = restaurant.get("osm_id")
    
    # Ensure current timestamp is set for created/updated if needed
    now_str = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    created_at = restaurant.get("created_at") or now_str
    updated_at = restaurant.get("updated_at") or now_str
    likes_count = restaurant.get("likes_count") or 0
    views_count = restaurant.get("views_count") or 0

    try:
        cursor.execute("""
        INSERT INTO candidate_restaurants (
            id, name, description, cuisine_type, price_level, lat, lng, address, 
            cover_image_url, is_promoted, promotion_end_at, created_at, updated_at, 
            likes_count, views_count, validation_status, neighborhood, osm_id
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            rest_id, name, description, cuisine_type, price_level, lat, lng, address,
            cover_image_url, is_promoted, promotion_end_at, created_at, updated_at,
            likes_count, views_count, validation_status, neighborhood, osm_id
        ))
        conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        # Expected if osm_id already exists
        return False

def get_restaurants_by_status(conn, status, neighborhood=None):
    """Fetches candidates by validation status and optionally neighborhood."""
    cursor = conn.cursor()
    if neighborhood:
        cursor.execute("""
        SELECT * FROM candidate_restaurants 
        WHERE validation_status = ? AND neighborhood = ?
        ORDER BY created_at DESC
        """, (status, neighborhood))
    else:
        cursor.execute("""
        SELECT * FROM candidate_restaurants 
        WHERE validation_status = ?
        ORDER BY created_at DESC
        """, (status,))
    
    return [dict(row) for row in cursor.fetchall()]

def update_restaurant_status(conn, restaurant_id, status, updated_fields=None):
    """
    Updates the status and other fields of a candidate restaurant.
    updated_fields is a dictionary of additional columns to update.
    """
    cursor = conn.cursor()
    now_str = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    if not updated_fields:
        updated_fields = {}
        
    updated_fields["validation_status"] = status
    updated_fields["updated_at"] = now_str
    
    set_clause = ", ".join([f"{col} = ?" for col in updated_fields.keys()])
    values = list(updated_fields.values())
    values.append(restaurant_id)
    
    cursor.execute(f"""
    UPDATE candidate_restaurants 
    SET {set_clause} 
    WHERE id = ?
    """, values)
    conn.commit()

def get_valid_restaurants(conn):
    """Fetches all validated restaurants for export."""
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM candidate_restaurants 
    WHERE validation_status = 'valid'
    ORDER BY name ASC
    """)
    return [dict(row) for row in cursor.fetchall()]

if __name__ == "__main__":
    init_db()
