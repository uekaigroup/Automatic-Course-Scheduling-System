from django.contrib import admin
from teacher.models import Teacher,Teachstage
from professional.models import Professional,Stage,StageOrder
from classes.models import Classes
from area.models import Area

# Register your models here.

@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    exclude = []



@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    exclude = []
    # inlines = [
    #     TeachstageInline,
    # ]



@admin.register(StageOrder)
class StageOrderAdmin(admin.ModelAdmin):
    exclude = []

class TeachstageInline(admin.TabularInline):
    model = Teachstage

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [
        TeachstageInline
    ]
    # exclude = []


@admin.register(Classes)
class ClasseAdmin(admin.ModelAdmin):
    exclude = []
    class Media:
        js=('home/js/getstage.js',)

    # def add_view(self, request, form_url='', extra_context=None):
    #     return super().add_view(request, form_url, extra_context)
    # def save_model(self, request, obj, form, change):
    #     obj.u=request.user
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    exclude = []



