from django.contrib import admin
from .models import (
    Consultation,
    Exercise,
    WorkoutExercise,
    Workout,
    Plan,
    Question,
    Answer,
)

# Register your models here.
admin.site.register(Consultation)
admin.site.register(Exercise)
admin.site.register(WorkoutExercise)
admin.site.register(Workout)
admin.site.register(Plan)
admin.site.register(Question)
admin.site.register(Answer)
