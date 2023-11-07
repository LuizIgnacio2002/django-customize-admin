from django.db import models

class Student(models.Model):
    document_type = models.CharField(max_length=10, verbose_name="Document Type")
    document_number = models.CharField(max_length=10, verbose_name="Document Number")
    code = models.CharField(max_length=8, verbose_name="Code")
    first_name = models.CharField(max_length=256, verbose_name="First Name")
    last_name = models.CharField(max_length=256, verbose_name="Last Name")
    email = models.CharField(max_length=100, verbose_name="Email")

    def __str__(self):
        text = "{0}, {1} ({2})"
        return text.format(self.last_name, self.first_name, self.code)