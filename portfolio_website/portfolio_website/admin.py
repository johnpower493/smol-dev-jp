```python
from django.contrib import admin
from .models import Project, Skill

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'technology', 'image')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
```