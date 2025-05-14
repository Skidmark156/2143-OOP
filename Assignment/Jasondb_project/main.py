from people_db import PeopleDB
from meteorite_db import MeteoriteDB
from earthquake_db import EarthquakeDB

def main():
    # People
    people_db = PeopleDB("people.json")
    people_db.create_person("Teresa", "Smith", "Austin")
    people_db.create_person("John", "Doe", "Dallas")
    print("People named Teresa:", people_db.find_by_name(first_name="Teresa"))

    # Meteorites
    meteor_db = MeteoriteDB("meteorites.json")
    print("Meteorites from 1900–1950:", meteor_db.find_by_year_range(1900, 1950))
    print("Top 3 heaviest meteorites:", meteor_db.find_heaviest_meteorites(3))

    # Earthquakes
    quake_db = EarthquakeDB("earthquakes.json")
    print("Quakes between 5.0 and 7.0 magnitude:", quake_db.filter_by_magnitude(5.0, 7.0))
    print("Coordinates of quake ID 'us1234':", quake_db.get_coordinates("us1234"))

if __name__ == "__main__":
    main()
