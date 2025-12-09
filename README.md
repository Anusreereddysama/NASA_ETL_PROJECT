# 🌌 NASA APOD ETL Pipeline

An end-to-end ETL (Extract, Transform, Load) pipeline built using NASA’s Astronomy Picture of the Day (APOD) API.  
This project demonstrates how real-world API data can be extracted, cleaned, transformed, and loaded into a cloud-hosted PostgreSQL database using Supabase.

---

##  Project Overview

This ETL pipeline performs:
- Extracts data from the NASA APOD API
- Transforms raw JSON into clean, structured tabular data
- Handles missing and optional API fields safely
- Loads data into Supabase (PostgreSQL) using batch inserts
- Follows best practices for scalable data pipelines

---

##  Tech Stack

- Python
- Pandas
- NASA APOD API
- Supabase (PostgreSQL)
- python-dotenv
- Git & GitHub

---

##  Project Structure

   ETL_NASA/
   ├── Scripts/
   │   ├── extract_nasa.py       # Extracts data from NASA APOD API
   │   ├── transform_nasa.py     # Transforms raw JSON into CSV
   │   └── load_nasa.py          # Loads cleaned data into Supabase
   ├── data/
   │   ├── raw/                  # Raw API responses (not committed)
   │   └── staged/               # Cleaned CSV files (not committed)
   ├── .env                      # Environment variables (ignored)
   ├── .gitignore
   └── README.md

##  Database Schema

CREATE TABLE nasa_apod (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    title VARCHAR(255) NOT NULL,
    explanation TEXT NOT NULL,
    media_type VARCHAR(50),
    image_url TEXT,
    inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

---

##  How to Run the ETL Pipeline

1. Clone the repository

   - git clone https://github.com/Anusreereddysama/NASA_ETL_PROJECT
   - cd ETL_NASA

2. Create & activate virtual environment (optional)

   python -m venv venv  
   source venv/bin/activate   # macOS/Linux

3. Install dependencies

   pip install -r requirements.txt

   Required libraries:
   - pandas
   - requests
   - supabase
   - python-dotenv

4. Environment configuration

   Create a `.env` file with:

   SUPABASE_URL=your_supabase_url  
   SUPABASE_KEY=your_supabase_anon_key  
   NASA_API_KEY=your_nasa_api_key  


5. Run the pipeline

   python Scripts/extract_nasa.py  
   python Scripts/transform_nasa.py  
   python Scripts/load_nasa.py  

---

##  Key Learnings

   - Handling real-world, inconsistent API data
   - Schema-aligned database inserts
   - Batch loading for efficient data ingestion
   - Building production-style ETL pipelines
   - Using cloud databases with Python

---



## Author
Anusree Reddy  

---

