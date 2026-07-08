import os
import sys

# Add src to python path to import database helpers
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
import database

# Establish connection
conn = database.get_db_connection()

# Initialize the database schema if not already done
database.init_db()

# List of extracted candidate restaurants in Sevilla Este
candidates = [
    {
        "name": "Restaurante Zelai Sevilla Este",
        "description": "Elegant dining space offering modern interpretations of traditional Andalusian tapas and dishes.",
        "cuisine_type": "Tapas",
        "price_level": 2,
        "lat": 37.404845,
        "lng": -5.928120,
        "address": "Calle Alcalde Luis Uruñuela, 16, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/zelai_sevilla_este",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
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
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "El Fogón de Sergio",
        "description": "Traditional Andalusian cuisine specializing in charcoal-grilled meats (carnes a la brasa) and fresh seafood in a family-friendly space.",
        "cuisine_type": "Spanish",
        "price_level": 2,
        "lat": 37.392794,
        "lng": -5.920204,
        "address": "Av. de las Ciencias, 12, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/el_fogon_de_sergio",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "Taberna La Botica",
        "description": "Cozy tavern offering a diverse selection of traditional tapas, completely gluten-free, with a selection of fine wines and creative cocktails.",
        "cuisine_type": "Tapas",
        "price_level": 2,
        "lat": 37.394800,
        "lng": -5.922800,
        "address": "Av. de las Ciencias, 21, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1562601579-579bc89ff716?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/taberna_la_botica",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "Benavente Gastrobar",
        "description": "High-quality gastrobar serving beautifully presented tapas, local wines, and fusion dishes in a modern atmosphere.",
        "cuisine_type": "Tapas",
        "price_level": 2,
        "lat": 37.395800,
        "lng": -5.926200,
        "address": "Av. de las Ciencias, 22, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1598515214211-89d3e73ae83b?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/benavente_gastrobar",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "Street Food Burger Sevilla Este",
        "description": "Popular spot for gourmet burgers, loaded fries, and craft beers in a cool street-art inspired venue.",
        "cuisine_type": "Burgers",
        "price_level": 2,
        "lat": 37.395200,
        "lng": -5.922000,
        "address": "Av. de las Ciencias, 38, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/street_food_burger_sevilla_este",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "Bar Volare Vinos y Tapas",
        "description": "Unpretentious neighborhood bar famous for its typical Andalusian tapas, cold beers, and quick friendly service.",
        "cuisine_type": "Tapas",
        "price_level": 1,
        "lat": 37.394859,
        "lng": -5.921658,
        "address": "Av. de las Ciencias, 16, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1598515214211-89d3e73ae83b?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/bar_volare_sevilla_este",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "La Posada del Duque",
        "description": "Well-known restaurant specializing in charcoal-grilled meats and traditional Andalusian recipes, ideal for groups and events.",
        "cuisine_type": "Spanish",
        "price_level": 3,
        "lat": 37.406800,
        "lng": -5.926400,
        "address": "Calle Administrador Gutiérrez Anaya, 8, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1546964124-0cce460f38ef?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/la_posada_del_duque",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "L'Asalvajá",
        "description": "Creative modern tapas and dishes using local fresh ingredients in a stylish, welcoming environment.",
        "cuisine_type": "Tapas",
        "price_level": 2,
        "lat": 37.408700,
        "lng": -5.923500,
        "address": "Calle Cueva del Agua, 8, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1515467876026-78f87773c22a?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/lasalvaja_sevilla_este",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "Il Mago Pancione",
        "description": "Authentic Italian pizzeria serving sourdough pizzas made with fresh ingredients, following traditional family recipes.",
        "cuisine_type": "Italian",
        "price_level": 2,
        "lat": 37.402600,
        "lng": -5.922100,
        "address": "Calle Japón, 6, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/il_mago_pancione",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "Malvada Geisha Sushi",
        "description": "Modern sushi fusion dining experience, combining Japanese traditions with Andalusian elements.",
        "cuisine_type": "Japanese",
        "price_level": 2,
        "lat": 37.397000,
        "lng": -5.923000,
        "address": "Av. de las Ciencias, 19, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/malvada_geisha",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "Oshiro",
        "description": "High-end authentic Japanese cuisine with techniques inspired directly by Tokyo sushi masters.",
        "cuisine_type": "Japanese",
        "price_level": 3,
        "lat": 37.401275,
        "lng": -5.924166,
        "address": "Calle Donantes de Sangre, S/N, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1611143669185-af224c5e3252?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/oshiro_sevilla_este",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "Mesón-Asador Triana",
        "description": "Traditional Spanish steakhouse offering charcoal-grilled meats, fresh local fish, and a warm rustic ambiance.",
        "cuisine_type": "Spanish",
        "price_level": 2,
        "lat": 37.404500,
        "lng": -5.923400,
        "address": "Calle Milano Plomizo, 85, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/meson_asador_triana",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "Café Bar La Ola",
        "description": "Friendly local bar in Calle Japón, well-liked for its vibrant community atmosphere and classic Andalusian tapas.",
        "cuisine_type": "Tapas",
        "price_level": 1,
        "lat": 37.402200,
        "lng": -5.920000,
        "address": "Calle Japón, 30, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1598515214211-89d3e73ae83b?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/cafe_bar_la_ola",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "Atípico",
        "description": "Burger joint located inside the local food market, famous for high-quality retinta beef patties and unique sauces.",
        "cuisine_type": "Burgers",
        "price_level": 2,
        "lat": 37.405000,
        "lng": -5.918000,
        "address": "Mercado de Abastos de Sevilla Este, Av. del Deporte, Local 13, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/atipico_sevilla_este",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    },
    {
        "name": "Cervecería Arturo",
        "description": "Lively local brewery and tapas bar, very popular for its ice-cold beers and fresh seafood tapas.",
        "cuisine_type": "Seafood",
        "price_level": 2,
        "lat": 37.401400,
        "lng": -5.922100,
        "address": "Calle Séptimo Día, 12, 41020 Sevilla",
        "cover_image_url": "https://images.unsplash.com/photo-1534080391025-096d299a4645?auto=format&fit=crop&w=800&q=80",
        "osm_id": "agent_ext/cerveceria_arturo",
        "neighborhood": "Sevilla Este",
        "validation_status": "pending"
    }
]

inserted_count = 0
for cand in candidates:
    # database.insert_candidate_restaurant returns True if inserted, False if duplicate osm_id
    success = database.insert_candidate_restaurant(conn, cand)
    if success:
        print(f"Inserted: {cand['name']}")
        inserted_count += 1
    else:
        print(f"Skipped (Duplicate/Already Exists): {cand['name']}")

print(f"\nDone! Seeding complete. Inserted {inserted_count} new candidate restaurants.")
conn.close()
