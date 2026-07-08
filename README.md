# Neighborhood Explorer Module

An isolated utility for searching, validating, and preparing restaurant listings for import into the FoodieDot application's database.

---

## 1. Directory Structure

```text
/explore
├── README.md               # Setup and usage guide (this file)
├── agents.md               # Guidelines for subsequent AI agents
├── prompt.md               # Instruction set for data gathering AI agent
├── requirements.txt        # Python dependency list
├── src/
│   ├── database.py         # SQLite connection and schema creation
│   ├── app.py              # Streamlit interactive verification UI
│   └── export.py           # CLI data exporter (JSON & SQL seeds)
└── data/
    ├── explorer.db         # Local SQLite database (auto-generated)
    ├── validated_restaurants.json # Validated export file (auto-generated)
    └── validated_restaurants.sql  # Validated export SQL file (auto-generated)
```

---

## 2. Setup Instructions

Ensure you have Python 3.8+ installed, then follow these steps:

1.  **Open Terminal** in the `/explore` directory.
2.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```
3.  **Activate Virtual Environment**:
    *   **Windows (PowerShell)**:
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```
    *   **Windows (CMD)**:
        ```cmd
        .\venv\Scripts\activate.bat
        ```
    *   **macOS / Linux**:
        ```bash
        source venv/bin/activate
        ```
4.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
5.  **Initialize the Database**:
    ```bash
    python src/database.py
    ```
    This creates the SQLite database `data/explorer.db` and configures the schema.

---

## 3. Data Gathering Strategy
Since we do not rely on an automated API scraper (which often returns partial, unnamed, or low-quality data), we use an AI agent to populate candidate listings.

1.  Open the instructions in **`prompt.md`**.
2.  Feed the prompt contents to an AI agent (or execute the steps yourself) to discover restaurants, coordinates, descriptions, and high-quality photo URLs.
3.  Follow the template in `prompt.md` to create a `seed_candidates.py` script.
4.  Run it to insert listings under `pending` status.
    ```bash
    python seed_candidates.py
    ```

---

## 4. Verification UI
To review, edit, map-validate, and approve/reject candidates, start the Streamlit application:

```bash
streamlit run src/app.py
```

*   **View Pending Candidates**: Select a candidate, review its location on the map, edit or fill in missing fields (like price level or cuisine type), and click **Approve** or **Reject**.
*   **Location Validation**: Interactive Folium mapping shows exactly where the coordinates resolve.
*   **Export**: Navigate to the **Approved Restaurants** tab to download your validated listings as a `validated_restaurants.json` file or `validated_restaurants.sql` seed script.

---

## 5. Exporting via CLI
If you prefer exporting without launching the Streamlit interface, run the export script:

```bash
# Export in both formats to the default data/ folder
python src/export.py

# Export only SQL format to a custom directory
python src/export.py --format sql --output-dir ./my_seeds
```
Outputs match the main application's `global_restaurants` schema, making them ready to seed.
# FoodieExplore
