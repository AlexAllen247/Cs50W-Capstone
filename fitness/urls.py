from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("consultation", views.consultation, name="consultation"),
    path("createexercise", views.create_exercise, name="createexercise"),
    path("createworkout", views.create_workout, name="createworkout"),
    path(
        "createworkoutexercise",
        views.create_workout_exercise,
        name="createworkoutexercise",
    ),
    path("createplan", views.create_plan, name="createplan"),
    path("clientworkouts", views.client_workouts, name="clientworkouts"),
    path("exercises_api/id/<int:exercise_id>", views.get_exercise, name="get_exercise"),
    path(
        "exercises_api/save/<int:exercise_id>",
        views.update_exercise,
        name="save_exercise",
    ),
    path("question", views.question, name="question"),
    path("answer", views.answer, name="answer"),
]
