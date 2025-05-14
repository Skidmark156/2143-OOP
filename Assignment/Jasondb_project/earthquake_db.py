from jsondb import JsonDB

class EarthquakeDB(JsonDB):
    """
    Specialized DB for earthquake records.
    Assumes 'features' list, like GeoJSON from USGS feeds.
    """

    def __init__(self, filepath):
        super().__init__(filepath)

    def filter_by_magnitude(self, min_mag, max_mag):
        """
        Returns earthquakes in the magnitude range.
        Assumes record['properties']['mag'].
        """
        result = []
        for quake in self.data:
            try:
                mag = float(quake["properties"]["mag"])
                if min_mag <= mag <= max_mag:
                    result.append(quake)
            except (KeyError, TypeError, ValueError):
                continue
        return result

    def get_coordinates(self, quake_id):
        """
        Returns coordinates from record['geometry']['coordinates']
        """
        for quake in self.data:
            if quake.get("id") == quake_id:
                return quake.get("geometry", {}).get("coordinates", None)
        return None
