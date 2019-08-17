from django.contrib import admin
from teacher.models import Teacher,TeacherData
from professional.models import Professional,Stage
from classes.models import Classes
from area.models import Area

# Register your models here.

@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    exclude = []

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    exclude = []

# @admin.register(Pub_stage)
# class Pub_stageAdmin(admin.ModelAdmin):
#     exclude = []

class TeacherDataInline(admin.TabularInline):
    model = TeacherData

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [
        TeacherDataInline
    ]
    # exclude = []

# class Stage_n_nInline(admin.TabularInline):
#     model = Stage_n_n
@admin.register(Classes)
class ClasseAdmin(admin.ModelAdmin):
    exclude = []
    # inlines = [
    #     Stage_n_nInline
    # ]
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    exclude = []



