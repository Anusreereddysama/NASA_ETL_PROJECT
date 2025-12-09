import json
from pathlib import Path
from datetime import datetime
import requests

data_dir=Path(__file__).resolve().parents[1]/"data"/"raw"
data_dir.mkdir(parents=True,exist_ok=True)

def  extract_nasa_data():
        url="https://api.nasa.gov/planetary/apod?api_key=kd4Nrn9qVDW6BQ58c8qZdXJe3N4ZLfhI77ykCjx5"
        resp=requests.get(url)
        resp.raise_for_status()
        data=resp.json()
        filename=data_dir/f"nasa.json"
        filename.write_text(json.dumps(data, indent=2))
        print(f"Extracted nasa image content data save to :{filename}")
        return data

if __name__=="__main__":
        extract_nasa_data()