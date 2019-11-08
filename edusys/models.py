from django.db import models


class Course(models.Model):
    days_of_week = [
        ("0", 'شنبه'),
        ("1", 'یکشنبه'),
        ("2", 'دوشنبه'),
        ("3", 'سه‌شنبه'),
        ("4", 'چهارشنبه')
    ]
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.CharField(max_length=2, choices=days_of_week, default=0)
    second_day = models.CharField(max_length=2, choices=days_of_week, default=0)
