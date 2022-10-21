from django.contrib.auth.models import User
from django.db import models


class Consultation(models.Model):
    class FitnessGoal(models.TextChoices):
        FAT_LOSS = "Fat Loss"
        GAIN_MUSCLE = "Gain Muscle"
        GAIN_STRENGTH = "Gain Strength"

    class PreviousExerciseExperience(models.TextChoices):
        ZERO_EXPERIENCE = "Zero Experience"
        BEGINNER = "Beginner"
        INTERMEDIATE = "Intermediate"
        ADVANCED = "Advanced"

    class CurrentActivityLevel(models.TextChoices):
        NO_ACTIVITY = "No Activity"
        LIGHT_ACTIVITY = "Light Activity"
        MODERATE_ACTIVITY = "Moderate Activity"
        INTENSE_ACTIVITY = "Intense Activity"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="consultation"
    )
    age = models.PositiveSmallIntegerField(null=False, blank=False)
    gender = models.CharField(max_length=10, null=False, blank=False)
    height_in_cms = models.CharField(max_length=5, null=False, blank=False)
    weight_in_kgs = models.CharField(max_length=5, null=False, blank=False)
    fitness_goal = models.CharField(
        max_length=20, choices=FitnessGoal.choices, default=FitnessGoal.FAT_LOSS
    )
    previous_exercise_experience = models.CharField(
        max_length=20,
        choices=PreviousExerciseExperience.choices,
        default=PreviousExerciseExperience.ZERO_EXPERIENCE,
    )
    current_activity_level = models.CharField(
        max_length=50,
        choices=CurrentActivityLevel.choices,
        default=CurrentActivityLevel.NO_ACTIVITY,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    any_injuries_or_underlying_health_conditions = models.TextField(
        max_length=1000, null=True
    )

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"{self.user} {self.fitness_goal}"


class Exercise(models.Model):
    class BodyPart(models.TextChoices):
        ABS = "Abs"
        ADDUCTORS = "Adductors"
        BICEPS = "Biceps"
        CALVES = "Calves"
        CHEST = "Chest"
        FOREARMS = "Forearms"
        FRONT_DELTS = "Front Delts"
        GLUTES = "Glutes"
        HAMSTRINGS = "Hamstrings"
        HIP_FLEXORS = "Hip Flexors"
        LATS = "Lats"
        LOWER_BACK = "Lower Back"
        OBLIQUES = "Obliques"
        QUADS = "Quads"
        REAR_DELTS = "Rear Delts"
        SIDE_DELTS = "Side Delts"
        TRAPS = "Traps"
        TRICEPS = "Triceps"

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    body_part = models.CharField(
        max_length=40, choices=BodyPart.choices, default=BodyPart.ABS
    )
    video_link = models.URLField(max_length=1000, null=True, blank=True)
    exercise_info = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ["user"]

    def __str__(self):
        return f"{self.user}'s {self.name}"


class WorkoutExercise(models.Model):

    workout = models.ForeignKey(
        "Workout", on_delete=models.CASCADE, null=True, blank=True
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.workout} {self.exercise}"


class Workout(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, unique=True, null=True)
    exercises = models.ManyToManyField(Exercise, through=WorkoutExercise)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return self.name


class Plan(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    workout = models.ManyToManyField(Workout)
    training_notes = models.CharField(max_length=10000, null=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return self.name


class Question(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return self.question


class Answer(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return self.answer
