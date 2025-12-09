import os
import time
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

def load_to_supabase():

    csv_path = "../data/staged/nasa_cleaned.csv"
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Missing file: {csv_path}")

    df = pd.read_csv(csv_path)
    df = df[[
        "date",
        "title",
        "explanation",
        "media_type",
        "url"
    ]].rename(columns={
        "url": "image_url"
    })

    batch_size = 20

    for i in range(0, len(df), batch_size):

        batch_df = df.iloc[i:i + batch_size]

        batch = (
            batch_df
            .where(pd.notnull(batch_df), None)
            .to_dict("records")
        )

       
        supabase.table("nasa_apod").insert(batch).execute()

        print(f"Inserted rows {i + 1} → {min(i + batch_size, len(df))}")
        time.sleep(0.5)

    print("Finished loading NASA data")

if __name__ == "__main__":
    load_to_supabase()
