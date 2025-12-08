# custom_csv_writer.py
from typing import List, TextIO

class CustomCsvWriter:
    """Write rows (lists of strings) to a CSV file."""
    def __init__(self, file: TextIO):
        self.f = file

    def _needs_quote(self, s: str) -> bool:
        return ',' in s or '"' in s or '\n' in s or '\r' in s

    def _quote_field(self, s: str) -> str:
        if '"' in s:
            s = s.replace('"', '""')
        if self._needs_quote(s):
            return f'"{s}"'
        return s

    def writerow(self, row: List[str]):
        processed = [self._quote_field('' if cell is None else str(cell)) for cell in row]
        self.f.write(','.join(processed) + '\n')

    def writerows(self, rows):
        for r in rows:
            self.writerow(r)
