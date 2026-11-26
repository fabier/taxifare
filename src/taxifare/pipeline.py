import pandas as pd
import numpy as np

lonlat_features = [
    "pickup_latitude",
    "pickup_longitude",
    "dropoff_latitude",
    "dropoff_longitude",
]


def scale_distance(dist):
    dist_min = 0
    dist_max = 100
    scaled = (dist - dist_min) / (dist_max - dist_min)
    return scaled


def scale_passenger(p):
    p_min = 0.0
    p_max = 8.0
    p_scaled = (p - p_min) / (p_max - p_min)
    return p_scaled


def scale_timedelta():
    pass


def manhattan_distance_for_pipe(df):
    distance = manhattan_distance_vectorized(df, *lonlat_features)
    return pd.DataFrame({"distance": distance})


def manhattan_distance_vectorized(
    df: pd.DataFrame, start_lat: str, start_lon: str, end_lat: str, end_lon: str
) -> dict:
    """
    Calculate the Manhattan distance in km between two points on the earth (specified in decimal degrees).
    Vectorized version for pandas df
    """
    earth_radius = 6371

    lat_1_rad, lon_1_rad = np.radians(df[start_lat]), np.radians(df[start_lon])
    lat_2_rad, lon_2_rad = np.radians(df[end_lat]), np.radians(df[end_lon])

    dlon_rad = lon_2_rad - lon_1_rad
    dlat_rad = lat_2_rad - lat_1_rad

    manhattan_rad = np.abs(dlon_rad) + np.abs(dlat_rad)
    manhattan_km = manhattan_rad * earth_radius

    return manhattan_km


def transform_time_features():
    pass
