import pandas as pd
import openpyxl
from Bot.Parser import internetMagazinParser
import os
import time

class ExcelTableCreator:


    def __init__(self, filename):
        self.filename = filename
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = "Данные"
        self.workbook.append = pd.DataFrame(columns=['Название', 'Старая цена', 'Новая цена'])

    def write_to_excel(self, smartphones):
        for row in smartphones:
            print("пошел процесс")
            self.sheet.append([row.name, row.old_price, row.new_price])
        self.workbook.save("data.xlsx")
        print("закончил процесс")

        def wait_for_file_ready(file_path, timeout=60):
            """
            Ожидает завершения записи в файл.
            """
            start_time = time.time()
            while True:
                if os.path.exists(file_path):
                    try:
                        with open(file_path, 'rb') as _:
                            print(f"Файл {file_path} готов к отправке.")
                            return
                    except (IOError, PermissionError):
                        pass  # Файл еще используется системой

                if time.time() - start_time > timeout:
                    raise TimeoutError(f"Файл {file_path} так и не стал доступен за {timeout} секунд.")

                time.sleep(1)

if __name__ == "__main__":
    parser = internetMagazinParser.InternetMagazinParser()



