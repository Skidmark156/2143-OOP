from jsondb import JsonDB

class MeteoriteDB(JsonDB):
    """
    Specialized DB for meteorite records.
    """

    def __init__(self, filepath):
        super().__init__(filepath)

    def find_by_year_range(self, start_year, end_year):
        """
        Returns meteorites with 'year' in [start_year, end_year].
        """
        result = []
        for meteor in self.data:
            try:
                year = int(meteor.get("year", 0))
                if start_year <= year <= end_year:
                    result.append(meteor)
            except ValueError:
                continue
        return result

    def find_by_location(self, lat, lng, radius):
        """
        Finds meteorites within a radius (naive Euclidean distance).
        Assumes meteor has 'reclat' and 'reclong'.
        """
        result = []
        for meteor in self.data:
            try:
                mlat = float(meteor.get("reclat"))
                mlng = float(meteor.get("reclong"))
                dist = ((mlat - lat) ** 2 + (mlng - lng) ** 2) ** 0.5
                if dist <= radius:
                    result.append(meteor)
            except (TypeError, ValueError):
                continue
        return result

    def find_heaviest_meteorites(self, limit=5):
        """
        Returns top N heaviest meteorites.
        """
        valid = [m for m in self.data if "mass" in m]
        valid.sort(key=lambda x: float(x.get("mass", 0)), reverse=True)
        return valid[:limit]
