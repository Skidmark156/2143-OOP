from jsondb import JsonDB

class PeopleDB(JsonDB):
    """
    Specialized DB for handling people records.
    """

    def __init__(self, filepath):
        super().__init__(filepath)

    def find_by_name(self, first_name=None, last_name=None):
        """
        Returns people matching first and/or last name.
        """
        result = []
        for person in self.data:
            if (first_name is None or person.get("first_name") == first_name) and \
               (last_name is None or person.get("last_name") == last_name):
                result.append(person)
        return result

    def create_person(self, first_name, last_name, city, ssn=None, phone=None):
        """
        Creates a new person entry with optional validation.
        """
        # Basic validation (expand if needed)
        if not first_name or not last_name or not city:
            raise ValueError("First name, last name, and city are required.")
        person = {
            "first_name": first_name,
            "last_name": last_name,
            "city": city,
            "ssn": ssn,
            "phone": phone
        }
        return self.create(person)
