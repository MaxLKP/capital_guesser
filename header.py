from pystac_client import Client
import urllib.request
import pandas as pd
import numpy as np
import streamlit as st
import subprocess

api_url = "https://earth-search.aws.element84.com/v1"

client = Client.open(api_url)
collections = client.get_collections()

collection = "sentinel-2-c1-l2a"

data = pd.read_csv("./data/data.txt", delimiter = ",")

options_capitals = np.sort(data["Capital"].to_numpy())
options_countries = np.sort(data["Country"].to_numpy())

def run_streamlit():
    subprocess.run(["python", "-m", "streamlit", "run", "./streamlit_app.py"])
    return None

def get_points():
    st.write(f"Points: {st.session_state.points}")
    return None

def get_result(data):
    line = np.random.randint(0, len(data))
    data_line = data.iloc[line]
    return data_line

def reset_result():
    result = get_satelite_image()
    st.session_state.result = result
    st.session_state.capital = st.session_state.result["Capital"]
    st.session_state.country = st.session_state.result["Country"]
    return None

def get_satelite_image():
    result = get_result(data)
    results = client.search(collections = [collection], intersects = {"type": "Point", "coordinates": [result["Longitude"], result["Latitude"]]}, datetime = "2026-05-01/2026-08-29")
    items = results.item_collection()
    item = items[-1].assets["thumbnail"].href
    urllib.request.urlretrieve(item, "./geo_images/geo_image.png")
    return result
