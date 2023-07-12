import datetime
from openpyxl import load_workbook


def read_and_print_first_line():
    file_path = 'data/The Museum Tower Middle Block 201901-202212.xlsx'

    try:
        workbook = load_workbook(file_path)
        sheet = workbook.active

        first_row = sheet[1]
        for cell in first_row:
            print(cell.value)

    except Exception as e:
        print(f"Error reading Excel file: {str(e)}")

read_and_print_first_line()
