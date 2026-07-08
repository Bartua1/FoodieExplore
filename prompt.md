# Instruction: Extract & Seed Candidate Restaurants

You are an AI data gathering agent tasked with finding and compiling restaurant details for a specific neighborhood and seeding them into the local SQLite database.

## Objective
Extract detailed restaurant information for the target neighborhood (starting with **Sevilla Este**), find high-quality image URLs, and seed them into `data/explorer.db` as `'pending'` status candidate restaurants.

---

## 1. Target Neighborhood & Scope
*   **Target Neighborhood**: `Sevilla Este` (Seville, Spain)
*   **Bounding Box Reference**: Latitude `37.385` to `37.415`, Longitude `-5.945` to `-5.905`.
*   **Target Count**: Aim to collect a representative list of 10-20 popular and well-rated restaurants in this area.

---

## 2. Restaurant Schema details
For each restaurant, extract or generate the following properties:

| Property Name | SQLite Column | Required | Description / Requirements |
| :--- | :--- | :--- | :--- |
| `name` | `name` | Yes | Official name of the restaurant. |
| `description` | `description` | No | A short summary of the restaurant, its atmosphere, and key specialties. |
| `cuisine_type` | `cuisine_type` | No | E.g., Tapas, Italian, Burgers, Spanish, Mediterranean, Japanese. |
| `price_level` | `price_level` | No | Integer from `1` (cheap) to `4` (very expensive). |
| `lat` | `lat` | Yes | Latitude coordinate (float, must be valid for the neighborhood). |
| `lng` | `lng` | Yes | Longitude coordinate (float, must be valid for the neighborhood). |
| `address` | `address` | No | Full street address of the restaurant. |
| `cover_image_url` | `cover_image_url` | No | A direct, public URL to a high-quality photo representing the food or venue (e.g. from Unsplash or public maps images). |
| `neighborhood` | `neighborhood` | Yes | `'Sevilla Este'` (or the active neighborhood being explored). |
| `osm_id` | `osm_id` | Yes | A unique source identifier to prevent duplicates. You can format it as `agent_ext/<name_slug>` if not pulling directly from OpenStreetMap. |

---

## 3. Data Gathering Protocol
1.  **Search & Discovery**: Use web search tools or maps to look up popular restaurants, tapas bars, and cafes in the target neighborhood.
2.  **Verify Coordinates**: Ensure the latitude and longitude are accurate and place the marker exactly in the correct neighborhood.
3.  **Photos**: Find direct, hotlinkable image URLs. Prefer stable stock images or valid public links. If no image is available, leave it as `None` or use a standard culinary placeholder URL.
4.  **Avoid Duplicates**: Use a unique `osm_id` slug (like `agent_ext/restaurant_name_slug`) for every entry.

---

## 4. Seeding Script Template
Create a temporary script named `seed_candidates.py` in the `/explore` root and write python code using the `/explore/src/database.py` helpers. Here is a template you can populate and run:

```python
import os
import sys

# Add src to python path to import database helpers
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
import database

# Establish connection
conn = database.get_db_connection()

# Initialize the database schema if not already done
database.init_db()

# List of extracted candidate restaurants
candidates = [
    {
        "name": "Restaurante Zelai Sevilla Este",
        "description": "Modern tapas and traditional Andalusian dishes in a stylish setting.",
        "cuisine_type": "Tapas",
        "price_level": 2,
        "lat": 37.404845,
        "lng": -5.928120,
        "address": "Calle Alcalde Luis Uruñuela, 16, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/zelai_sevilla_este",
        "neighborhood": "Sevilla Este"
    },
    {
        "name": "Cervecería La Grande Sevilla Este",
        "description": "Famous for fresh seafood, prawns, and freezing cold beer served in a lively traditional atmosphere.",
        "cuisine_type": "Seafood",
        "price_level": 2,
        "lat": 37.402241,
        "lng": -5.925482,
        "address": "Av. de las Ciencias, 4, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/la_grande_sevilla_este",
        "neighborhood": "Sevilla Este"
    }
    # Add more restaurants here...
]

inserted_count = 0
for cand in candidates:
    # database.insert_candidate_restaurant returns True if inserted, False if duplicate osm_id
    success = database.insert_candidate_restaurant(conn, cand)
    if success:
        print(f"Inserted: {cand['name']}")
        inserted_count += 1
    else:
        print(f"Skipped (Duplicate): {cand['name']}")

print(f"\nDone! Seeding complete. Inserted {inserted_count} new candidate restaurants.")
conn.close()
```

## 5. Execution Steps
1.  Run web search or browse online sources to collect 10-15 restaurants.
2.  Populate a script like `seed_candidates.py` with your findings.
3.  Run the script: `python seed_candidates.py`.
4.  Confirm database updates by querying the database or launching the verification UI.
