
from django.db import models


class Course(models.Model):
    """Represents a course containing questions."""

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    """Represents a question belonging to a course."""

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="questions"
    )
    question_text = models.CharField(max_length=500)
    marks = models.PositiveIntegerField(default=1)

    def is_get_score(self):
        """Return the score for this question."""
        return self.marks

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """Represents an answer choice for a question."""

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices"
    )
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    """Records a student's submission for a question."""

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="submissions"
    )
    selected_choice = models.ForeignKey(
        Choice,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="submissions"
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission {self.pk}"

