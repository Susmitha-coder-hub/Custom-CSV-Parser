from custom_csv_writer import CustomCsvWriter

rows = [
    ['PolicyID', 'CustomerName', 'PlanType', 'Premium', 'Notes'],
    ['104', 'Arjun "AJ" Singh', 'Health Premium', '6000', 'Customer said: "Need full coverage."'],
    ['105', 'Priya Sharma', 'Life Standard', '7800', 'Address updated on 15/12/2024']
]

with open('new_insurance.csv', 'w', encoding='utf-8', newline='') as f:
    writer = CustomCsvWriter(f)
    writer.writerows(rows)
