from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    teacher_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_id')
    min_reading_level = models.PositiveSmallIntegerField(default=0)
    max_reading_level = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name
        

class StudentProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    reading_level = models.PositiveSmallIntegerField(default=0)


class Book(models.Model):
    title = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    rich_text = models.TextField()
    classroom_id = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    min_reading_level = models.PositiveSmallIntegerField(default=0)
    max_reading_level = models.PositiveSmallIntegerField(default=0)

    class CorrectnessLevel(models.TextChoices):
        NONE = 'NONE', _('None')
        CLOSE = 'CLOSE', _('Close')
        EXACT = 'EXACT', _('Exact')
        
    correctness_level = models.CharField(
        max_length=5,
        choices=CorrectnessLevel.choices,
        default=CorrectnessLevel.EXACT,
    )


class UserAssignment(models.Model):
    student_profile_id = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    grade = models.FloatField(default=0)
    correctness_score = models.FloatField(default=0)
    date_completed = models.DateTimeField(blank=True, null=True)
    word_index = models.PositiveIntegerField(default=0)
    late_exemption_granted = models.BooleanField(default=False)
    completion_time = models.PositiveIntegerField(default=0)


class MissedWord(models.Model):
    word = models.CharField(max_length=20)
    user_assignment_id = models.ForeignKey(UserAssignment, on_delete=models.CASCADE)
    word_index = models.PositiveIntegerField()
    known = models.BooleanField()


