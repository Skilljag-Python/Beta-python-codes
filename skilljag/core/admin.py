from django.contrib import admin
from .models import Language, Skill, Value, State, City, SkillGroup, Country

admin.site.register(Skill)
admin.site.register(Value)
admin.site.register(City)
admin.site.register(State)
admin.site.register(SkillGroup)
admin.site.register(Country)
admin.site.register(Language)