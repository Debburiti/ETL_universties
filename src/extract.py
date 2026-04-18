import requests
from typing import List, Dict

class Extract:
    """Class responsible for extracting data from the Hipolabs API."""

    def __init__(self):
        pass

    def extract_country(self, country: str) -> List[Dict]:
        """
        Accesses the API URL and deserializes the returned data into JSON format.

        Args:
            country (str): The name of the country to search for.

        Returns:
            List[Dict]: A list of dictionaries containing university data.
        """
        url = f"http://universities.hipolabs.com/search?country={country}"
        response = requests.get(url)
        response.raise_for_status()
        universities = response.json()
        return universities