from abc import ABC, abstractmethod
import csv
import json

from os import path

# Common Data Interface
class IData(ABC):
    @abstractmethod
    def get_data(self) -> list[dict]:
        pass

# Data Format Adapters
class CSVAdapter(IData):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self) -> list[dict]:
        data = []
        with open(self.file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data

class JSONAdapter(IData):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self) -> list[dict]:
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        return data

# Legacy Data Source (Incompatible Interface)
class LegacyDataSource:
    def get_legacy_data(self):
        # Complex legacy data retrieval logic
        legacy_data = [
            {"id": 1, "name": "Alice", "age": 30},
            {"id": 2, "name": "Bob", "age": 25}
        ]
        return legacy_data

# Adapter for Legacy Data Source
class LegacyDataAdapter(IData):
    def __init__(self, legacy_source):
        self.legacy_source = legacy_source

    def get_data(self) -> list[dict]:
        legacy_data = self.legacy_source.get_legacy_data()
        # Convert legacy data to the common format
        return legacy_data

# Usage
csv_adapter = CSVAdapter(path.abspath("patterns/adapter") + '/data.csv')
json_adapter = JSONAdapter(path.abspath("patterns/adapter") + '/data.json')
legacy_adapter = LegacyDataAdapter(LegacyDataSource())

# Process data uniformly
for adapter in [csv_adapter, json_adapter, legacy_adapter]:
    data = adapter.get_data()
    for item in data:
        print(item)