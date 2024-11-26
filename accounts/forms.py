from django import forms
from .models import Employee

class EmployeeEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'mobile', 'designation', 'gender', 'courses', 'img_upload']  # Correct field name

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit():
            raise forms.ValidationError("Mobile number must be numeric.")
        if len(mobile) != 10:
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")
        return mobile

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Employee.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is already in use.")
        return email




from django import forms
from .models import Employee
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

def validate_file_extension(file):
    valid_extensions = ['jpg', 'png']
    if not file.name.split('.')[-1].lower() in valid_extensions:
        raise ValidationError("Only .jpg and .png files are allowed.")

class EmployeeForm(forms.ModelForm):
    mobile_no = forms.CharField(
        validators=[RegexValidator(r'^\d+$', 'Enter a valid numeric mobile number.')]
    )

    class Meta:
        model = Employee
        fields = ['name', 'email', 'mobile', 'designation', 'gender', 'courses', 'img_upload']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Employee.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError("This email is already in use.")
        return email

    def clean_img(self):
        img = self.cleaned_data.get('img_upload')
        if img:
            validate_file_extension(img)
        return img



from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    COURSE_CHOICES = [
        ('MCA', 'MCA'),
        ('BCA', 'BCA'),
        ('BSC', 'BSC'),
    ]

    courses = forms.ChoiceField(
        choices=COURSE_CHOICES,
        widget=forms.RadioSelect,  # Render as checkboxes
        required=True  # Ensure at least one course is selected
    )

    class Meta:
        model = Employee
        fields = ['name', 'email', 'mobile', 'designation', 'gender', 'courses', 'img_upload']
