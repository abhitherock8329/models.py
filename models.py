from django.db import models

# (Assuming your Enrollment, Question, and Choice models are defined here and are correct)

class Submission(models.Model):
    # ForeignKey to Enrollment
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    
    # ManyToManyField to Choice
    choices = models.ManyToManyField(Choice)

    # Appropriate string representation method
    def __str__(self):
        return f"Submission for {self.enrollment}"
