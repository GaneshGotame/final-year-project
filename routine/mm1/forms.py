from django.forms import ModelForm
from. models import *
from django import forms


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            'r_number',
            'seating_capacity'
        ]


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = [
            'uid',
            'name'
        ]


class MeetingTimeForm(ModelForm):
    class Meta:
        model = MeetingTime
        fields = [
            'pid',
            'time',
            'day'
        ]
        widgets = {
            'pid': forms.TextInput(),
            'time': forms.Select(),
            'day': forms.Select(),
        }


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_number', 'course_name', 'credit_hours', 'instructors']


class SemesterForm(ModelForm):
    class Meta:
        model = Semester
        fields = ['semester', 'courses']


class SelectsemesterForm(ModelForm):
    class Meta:
        model = Selectsemester
        fields = ['select_semester_id', 'semester', 'num_class_in_week']
