import xlsxwriter


class ExcelGenerator:
    def __init__(self, file_name='output.xlsx'):
        self.workbook = xlsxwriter.Workbook(file_name)
        self.current_sheet = None

    def create_sheet(self, sheet_name='Sheet1'):
        self.current_sheet = self.workbook.add_worksheet(sheet_name)

    def write_data(self, row, col, data):
        if self.current_sheet:
            self.current_sheet.write(row, col, data)
        else:
            print("No sheet selected. Create a sheet first.")

    def generate_from_data_structure(self, data_structure):
        if not self.current_sheet:
            self.create_sheet()

        for row_index, row_data in enumerate(data_structure):
            for col_index, cell_data in enumerate(row_data):
                self.write_data(row_index, col_index, cell_data)

    def save_file(self):
        if self.workbook:
            self.workbook.close()
        else:
            print("No workbook to save.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.save_file()


if __name__ == '__main__':
    data_structure = [
        ['Name', 'Age', 'City'],
        ['John', 25, 'New York'],
        ['Alice', 30, 'San Francisco'],
    ]

    with ExcelGenerator() as f:
        f.create_sheet("Mysheet")
        # TODO:Generate Excel from data structure
        f.generate_from_data_structure(data_structure)
