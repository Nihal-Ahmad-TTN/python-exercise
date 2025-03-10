import openpyxl
from .models import Question


def import_polls_from_excel(file_path):
    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active

        for row in sheet.iter_rows(values_only=True):
            if not row or len(row) < 2:
                print("Skipping invalid row:", row)
            question = row
            Question.objects.create(question=question)
        print("Excel data imported successfully.")

    except Exception as e:
        print(f"Error processing file: {str(e)}")