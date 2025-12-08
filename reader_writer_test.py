# reader_writer_test.py
from custom_csv import CustomCsvReader, CustomCsvWriter

# 1️⃣ Write CSV
rows = [
    ['PolicyID', 'CustomerName', 'PlanType', 'Premium', 'Notes'],
    ['104', 'Arjun "AJ" Singh', 'Health Premium', '6000', 'Customer said: "Need full coverage."'],
    ['105', 'Priya Sharma', 'Life Standard', '7800', 'Address updated on 15/12/2024']
]

with open('combined_insurance.csv', 'w', encoding='utf-8', newline='') as f:
    writer = CustomCsvWriter(f)
    writer.writerows(rows)

# 2️⃣ Read CSV back
with open('combined_insurance.csv', 'r', encoding='utf-8') as f:
    reader = CustomCsvReader(f)
    for row in reader:
        print(row)
