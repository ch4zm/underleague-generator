import os
from glob import glob
from .constants import HERE, DATA, GEO


def get_city_country_codes():
    """Return a sorted list of country codes"""
    country_codes = set()
    for fpath in glob(GEO + "/*.txt"):
        fname = os.path.basename(fpath)
        if "states" in fname:
            continue
        country_code = fname.split(".")[0]
        country_codes.add(country_code)
    return sorted(list(country_codes))


def get_state_country_codes():
    country_codes = set()
    for fpath in glob(GEO + "/*_states.txt"):
        fname = os.path.basename(fpath)
        country_code = fname.split("_")[0]
        country_codes.add(country_code)
    return sorted(list(country_codes))


def get_cities_data_file_from_country_code(country_code):
    fname = country_code + ".txt"
    return os.path.join(GEO, fname)


def get_states_data_file_from_country_code(country_code):
    fname = country_code + "_states.txt"
    return os.path.join(GEO, fname)


def get_team_names_data_file():
    fname = "team_names.txt"
    return os.path.join(DATA, fname)


def get_leagues_divisions_data_file():
    fname = "leagues_divisions.txt"
    return os.path.join(DATA, fname)


def get_cities_count(country_code):
    city_fname = f"{country_code}.txt"
    city_fpath = os.path.join(GEO, city_fname)
    if not os.path.exists(city_fpath):
        raise Exception(
            f"Error: could not run get_city_count(): invalid country code {country_code} for cities"
        )
    with open(city_fpath, "r") as f:
        data = f.readlines()
    data = [j.strip() for j in data if len(j.strip()) > 0]
    return len(data)


def get_states_count(country_code):
    st_fname = f"{country_code}_states.txt"
    st_fpath = os.path.join(GEO, st_fname)
    if not os.path.exists(st_fpath):
        raise Exception(
            f"Error: could not run get_state_count(): invalid country code {country_code} for states"
        )
    with open(states_fpath, "r") as f:
        data = f.readlines()
    data = [j.strip() for j in data if len(j.strip()) > 0]
    return len(data)
