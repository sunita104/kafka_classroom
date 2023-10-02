from django.contrib import admin

# Register your models here.

from todolist.models import *

admin.site.register(Task)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(CourseStudent)
admin.site.register(CourseTeacher)