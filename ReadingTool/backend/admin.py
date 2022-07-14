from django.contrib import admin
from .models import Book, Classroom, Assignment, MissedWord, UserAssignment

# Register your models here.

@admin.register(Book)
class BookModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')


@admin.register(Classroom)
class BookModel(admin.ModelAdmin):
    list_filter = ('name', 'teacher_id')
    list_display = ('name', 'teacher_id')


@admin.register(Assignment)
class AssignmentModel(admin.ModelAdmin):
    list_filter = ('title', 'classroom_id')
    list_display = ('title', 'classroom_id')


@admin.register(UserAssignment)
class UserAssignmentModel(admin.ModelAdmin):
    list_filter = ('user_id', 'assignment_id', 'grade')
    list_display = ('user_id', 'assignment_id', 'grade')


@admin.register(MissedWord)
class MissedWordModel(admin.ModelAdmin):
    list_filter = ('word', 'word_index', 'user_assignment_id')
    list_display = ('word', 'word_index', 'user_assignment_id')
