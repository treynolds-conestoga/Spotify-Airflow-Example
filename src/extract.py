import pandas as pd
from datetime import datetime
#import requests
import json

def get_spotify_keys() -> pd.DataFrame:
    with open("./secret/spotify_secret.json") as file:
        file_contents = file.read()

    print(file_contents)
    print(file_contents["api_key"])
    print(file_contents["user_id"])


if __name__ == "__main__":
    get_spotify_keys()