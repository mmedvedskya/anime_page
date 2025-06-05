from django.contrib import admin
from .models import Program, ProgramPoints, People

admin.site.register(People)
admin.site.register(Program)
admin.site.register(ProgramPoints)