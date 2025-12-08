# custom_csv_reader.py
import csv

class CustomCsvReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        records = []
        with open(self.file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append(row)
        return records

    def search(self, query):
        query = query.lower()
        data = self.load_data()
        results = []

        for row in data:
            combined = " ".join(row.values()).lower()
            if query in combined:
                results.append(row)
        return results

    def retrieve_information(self, query):
        results = self.search(query)
        if not results:
            return "No relevant information found."

        response = "Here is the information I found:\n\n"
        for row in results:
            response += (
                f"- PolicyID: {row['PolicyID']}\n"
                f"  CustomerName: {row['CustomerName']}\n"
                f"  PlanType: {row['PlanType']}\n"
                f"  Premium: {row['Premium']}\n"
                f"  Notes: {row['Notes']}\n\n"
            )
        return response
