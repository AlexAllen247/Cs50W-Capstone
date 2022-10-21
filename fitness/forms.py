from django import forms
from .models import (
    Consultation,
    Exercise,
    Workout,
    WorkoutExercise,
    Plan,
    Question,
    Answer,
)


class CreateConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = "__all__"
        exclude = ["user"]
        widgets = {
            "age": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.TextInput(attrs={"class": "form-control"}),
            "height_in_cms": forms.TextInput(attrs={"class": "form-control"}),
            "weight_in_kgs": forms.TextInput(attrs={"class": "form-control"}),
            "fitness_goal": forms.Select(attrs={"class": "form-control"}),
            "previous_exercise_experience": forms.Select(
                attrs={"class": "form-control"}
            ),
            "current_activity_level": forms.Select(attrs={"class": "form-control"}),
            "any_injuries_or_underlying_health_conditions": forms.Textarea(
                attrs={
                    "rows": 3,
                    "maxlength": 1000,
                    "class": "form-control",
                    "placeholder": "Write here...",
                }
            ),
        }


class CreateExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = "__all__"
        widgets = {
            "user": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "body_part": forms.Select(attrs={"class": "form-control"}),
            "video_link": forms.TextInput(attrs={"class": "form-control"}),
            "exercise_info": forms.Textarea(
                attrs={
                    "rows": 2,
                    "maxlength": 200,
                    "class": "form-control",
                    "placeholder": "Write a combination of sets/reps/weight or other variables...",
                }
            ),
        }


class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = "__all__"
        exclude = ["exercises"]
        widgets = {
            "user": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class CreateWorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = "__all__"
        widgets = {
            "workout": forms.Select(attrs={"class": "form-control"}),
            "exercise": forms.Select(attrs={"class": "form-control"}),
        }


class CreatePlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = "__all__"
        widgets = {
            "user": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "training_notes": forms.Textarea(
                attrs={
                    "rows": 10,
                    "maxlength": 10000,
                    "class": "form-control",
                    "placeholder": "Write here...",
                }
            ),
            "workout": forms.CheckboxSelectMultiple(attrs={"class": "form-control"}),
        }


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
        exclude = ["user"]
        widgets = {
            "question": forms.Textarea(
                attrs={
                    "rows": 5,
                    "maxlength": 1000,
                    "class": "form-control",
                    "placeholder": "Write your question here...",
                }
            )
        }


class CreateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"
        widgets = {
            "user": forms.Select(attrs={"class": "form-control"}),
            "answer": forms.Textarea(
                attrs={
                    "rows": 5,
                    "maxlength": 1000,
                    "class": "form-control",
                    "placeholder": "Write your response...",
                }
            ),
        }
