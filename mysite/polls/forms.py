from django import forms
from .models import Choice, UploadExcel

class VoteForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        widgets = {
            'choice_text': forms.RadioSelect
        }

# class PollExcelUploadForm(forms.ModelForm):
#     class Meta:
#         model = UploadExcel
#         fields = ['file']


class ExcelUpload(forms.Form):
    file = forms.FileField()
    def clean_file(self):
        file = self.cleaned_data['file']
        if not (file.name.endswith('.xlsx') or file.name.endswith('.xls')):
            raise forms.ValidationError("Invalid file format")
        if file.size > 5 * 1024 * 1024:
            raise forms.ValidationError("File too large! Max size is 5MB.")
        return file
    