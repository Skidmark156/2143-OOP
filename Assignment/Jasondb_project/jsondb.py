import json
import os

class JsonDB:
    """
    A generic JSON-based database class with CRUD operations.
    Stores data in-memory as a list of dictionaries.
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []
        self._load_data()

    def _load_data(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                try:
                    self.data = json.load(file)
                except json.JSONDecodeError:
                    self.data = []
        else:
            self.data = []

    def _save_data(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.data, file, indent=4)

    def create(self, record):
        """
        Adds a new record (dict). Assigns a unique ID if not present.
        Returns the record ID.
        """
        if "id" not in record:
            record["id"] = self._generate_new_id()
        self.data.append(record)
        self._save_data()
        return record["id"]

    def read(self, filters=None):
        """
        Returns all records or those that match the filters (dict).
        """
        if not filters:
            return self.data
        result = []
        for record in self.data:
            if all(record.get(k) == v for k, v in filters.items()):
                result.append(record)
        return result

    def update(self, record_id, new_data):
        """
        Updates a record with a given ID.
        """
        for record in self.data:
            if record.get("id") == record_id:
                record.update(new_data)
                self._save_data()
                return True
        return False  # Not found

    def delete(self, record_id):
        """
        Deletes a record by ID.
        """
        for i, record in enumerate(self.data):
            if record.get("id") == record_id:
                del self.data[i]
                self._save_data()
                return True
        return False  # Not found

    def _generate_new_id(self):
        """
        Generates a new unique ID (assumes numeric IDs).
        """
        existing_ids = [record.get("id", 0) for record in self.data if isinstance(record.get("id"), int)]
        return max(existing_ids, default=0) + 1
