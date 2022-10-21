from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

from .forms import (
    CreateConsultationForm,
    CreateExerciseForm,
    CreateWorkoutForm,
    CreateWorkoutExerciseForm,
    CreatePlanForm,
    CreateQuestionForm,
    CreateAnswerForm,
)
from .models import Consultation, Exercise, Workout, Plan, Question, Answer


@csrf_exempt
@login_required(login_url="login")
def index(request):
    # Index page to display all plans for the user and all completed consultations for the PT
    # Pagination is also used on this page
    if request.user.is_staff:
        plan = Consultation.objects.all().order_by("-timestamp")
    else:
        plan = Plan.objects.filter(user=request.user.id).order_by("-timestamp")
    paginator = Paginator(plan, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if request.GET.get("page") != None:
        try:
            plan = paginator.page(request.GET.get("page"))
        except:
            plan = paginator.page(1)
    else:
        plan = paginator.page(1)
    return render(request, "fitness/index.html", {"plan": plan, "page_obj": page_obj})


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "fitness/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "fitness/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "fitness/register.html", {"message": "Passwords must match."}
            )
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "fitness/register.html", {"message": "Username already taken."}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "fitness/register.html")


@login_required(login_url="login")
def consultation(request):
    # Function for client to fill out the initial consultation form
    if request.method == "POST":
        form = CreateConsultationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = CreateConsultationForm()
    return render(request, "fitness/consultation.html", {"form": form})


@login_required(login_url="login")
def create_exercise(request):
    # Function for PT to create exercises that are unique for each user and their workouts
    if request.method == "POST":
        form = CreateExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("createexercise"))
    else:
        form = CreateExerciseForm()
    return render(request, "fitness/createexercise.html", {"form": form})


@login_required(login_url="login")
def create_workout(request):
    # Function for PT to create workouts for users as part of a plan
    if request.method == "POST":
        form = CreateWorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("createworkout"))
    else:
        form = CreateWorkoutForm()
    return render(request, "fitness/createworkout.html", {"form": form})


@login_required(login_url="login")
def create_workout_exercise(request):
    # Function for PT to group exercises and workouts together
    if request.method == "POST":
        form = CreateWorkoutExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("createworkoutexercise"))
    else:
        form = CreateWorkoutExerciseForm()
    return render(request, "fitness/createworkoutexercise.html", {"form": form})


@login_required(login_url="login")
def create_plan(request):
    # Function for PT to create a plan, which is a group of workouts based on Consultation form information
    workout = Workout.objects.all()
    if request.method == "POST":
        form = CreatePlanForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = CreatePlanForm()
    return render(
        request, "fitness/createplan.html", {"form": form, "workout": workout}
    )


@login_required(login_url="login")
def client_workouts(request):
    # Function displaying all the workouts and exercises for each user
    # Pagination is also present on this page
    user = request.user.id
    workout = Workout.objects.filter(user=user).order_by("-timestamp")
    paginator = Paginator(workout, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if request.GET.get("page") != None:
        try:
            workout = paginator.page(request.GET.get("page"))
        except:
            workout = paginator.page(1)
    else:
        workout = paginator.page(1)
    return render(
        request,
        "fitness/clientworkouts.html",
        {"workout": workout, "page_obj": page_obj},
    )


@csrf_exempt
@login_required(login_url="login")
def get_exercise(request, exercise_id):
    # Function to be able to 'GET' all exercises via fetching in Javascript
    user = request.user.id
    exercise = Exercise.objects.get(pk=exercise_id)
    return JsonResponse(model_to_dict(exercise), safe=False)


@csrf_exempt
@login_required(login_url="login")
def update_exercise(request, exercise_id):
    # Function to be able to update exercise variables in workouts via Javascript and 'PUT' method
    try:
        exercise = Exercise.objects.get(pk=exercise_id)
    except Exercise.DoesNotExist:
        return JsonResponse({"error": "Invalid path."}, status=400)

    if request.method == "PUT":
        data = json.loads(request.body)
        exercise_info = data.get("exercise_info")
        exercise.exercise_info = exercise_info
        exercise.save()
        return JsonResponse({"exercise_info": exercise.exercise_info}, status=200)
    else:
        return JsonResponse({"error": "PUT request required."}, status=400)


@login_required(login_url="login")
def question(request):
    # Page for clients to ask questions about plan, workouts, exercises or anything else
    # Pagination is used on this webpage
    answer = Answer.objects.filter(user=request.user.id).order_by("-timestamp")
    paginator = Paginator(answer, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if request.GET.get("page") != None:
        try:
            answer = paginator.page(request.GET.get("page"))
        except:
            answer = paginator.page(1)
    else:
        answer = paginator.page(1)
    if request.method == "POST":
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = CreateQuestionForm()
    return render(
        request,
        "fitness/question.html",
        {"form": form, "answer": answer, "page_obj": page_obj},
    )


@login_required(login_url="login")
def answer(request):
    # Page for PT to answer any client questions
    # Pagination is also used on this page
    if request.user.is_staff:
        question = Question.objects.all().order_by("-timestamp")
        paginator = Paginator(question, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        if request.GET.get("page") != None:
            try:
                question = paginator.page(request.GET.get("page"))
            except:
                question = paginator.page(1)
        else:
            question = paginator.page(1)
        if request.method == "POST":
            form = CreateAnswerForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("index"))
        else:
            form = CreateAnswerForm()
        return render(
            request,
            "fitness/answer.html",
            {"form": form, "question": question, "page_obj": page_obj},
        )
