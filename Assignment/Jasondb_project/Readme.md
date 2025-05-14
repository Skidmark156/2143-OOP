# JsonDB Project

## Overview

This project implements a generic JSON database class (`JsonDB`) with full CRUD support (Create, Read, Update, Delete), and extends it through subclassing for three specific types of data:
- People (`PeopleDB`)
- Meteorites (`MeteoriteDB`)
- Earthquakes (`EarthquakeDB`)

The goal is to demonstrate object-oriented programming (OOP) principles, particularly **inheritance** and **domain-specific extensions** of a base class.

---

## 🧱 Project Structure

├── jsondb.py # Base class for generic JSON DB operations
├── people_db.py # Subclass for handling people-specific logic
├── meteorite_db.py # Subclass for meteorite-specific logic
├── earthquake_db.py # Subclass for earthquake-specific logic
├── main.py # Sample usage and testing script
├── people.json # JSON file for storing people records
├── meteorites.json # JSON file for storing meteorite records
├── earthquakes.json # JSON file for storing earthquake records


---

## 🧠 Key Features

### ✅ `JsonDB` (Base Class)
- Loads and saves JSON data from a file.
- Stores records in memory (`self.data`).
- Provides basic `create`, `read`, `update`, and `delete` methods.
- Automatically saves changes to file.

### 🧩 Subclasses

#### `PeopleDB`
- Extends `JsonDB` to handle personal data.
- Adds search by name (`find_by_name`).
- Can be expanded to validate fields like SSN or phone number.

#### `MeteoriteDB`
- Supports finding meteorites by year range.
- Can return the top N heaviest meteorites.

#### `EarthquakeDB`
- Filters earthquakes by magnitude.
- Retrieves coordinates from nested geometry data.

---

## ▶️ How to Run

1. Ensure you have Python 3 installed.
2. Make sure all `.py` and `.json` files are in the same folder.
3. Open a terminal and navigate to the folder.
4. Run the project:

```bash
python main.py

Paul Silva
Class: OOP
Assignment: OOP JsonDB Inheritance Project