# Cs50W Final Project Capstone

### Video Demo: https://www.youtube.com/watch?v=52olNvZ_xWk

## Description:

This is the final project of the Cs50 Web Application course. This web application is designed for Personal Trainers to manage their clients, create workouts and monitor progress. Clients can keep track of their progress and maintain contact with their Personal Trainer. The web application has two distinct UI/UX's:
    1. The Personal Trainer can create exercises, workouts and plans for their clients, and provide feedback for any questions from their clients.
    2. Clients can fill out a consultation form on which their plans will be based. They can update and log their workouts and can interact with their Personal Trainer to ask any questions and better enable consistent long term progress.
The website requires users to be logged in as the functionality of this web application depends upon the distinction between whether the user is a client or the Personal Trainer(staff). I chose to complete this project because as a fully qualified Personal Trainer I understand how this application would assist the management of clients and individual client development.

Main Technologies used:

- HTML
- Bootstrap
- Javascript
- Python
- Django

## Distinctiveness and Complexity:

This project satisfies the distinctiveness requirements because it is not a Google Search clone, a Wiki clone, an e-commerce web application, an emailing system or a social media network. This web application is a completely different theme: a client management system for a personal trainer. For the client, the features are a means to track their fitness progress in order to help them achieve their fitness goals. For the personal trainer, the features are a means to create unique exercise programs and plans for clients. As outlined in the description above, this separates this project from all the other assignments and is distinct from them.

Regarding complexity, as per the Capstone project requirements this web application has been built using Django with a total of seven models in the backend to maintain the database for consultations, exercises, workout exercises, workouts, plans, questions and answers. The built-in Django User model was used for each user. The highest level of complexity in the whole web application was determining the model relationship between exercises, workouts and plans. This had not been a concern in any of the previous assignments. The model structure settled on was a direct relationship of Exercise -> Workout Exercise -> Workout -> Plan. The reason why I decided on this model structure is because the path of each exercise and the variables for the exercise (sets/reps/weight/time etc) are unique for each client. And because of this the personal trainer must create each exercise for each client. After this point he can create a workout for that client and then assign those exercises to that workout through the Workout Exercise model. Then those workouts are grouped together to form the plan for each client.

JavaScript was required to be used on the frontend for clients to update their exercise training variables in each workout. This was achieved asynchronously via a call to fetch after which the exercise training variable is saved to the database. This allows the user to update their exercises without a reload of the entire page. This is an essential element of complexity to enable each client to track their progress in each exercise in each workout.

This web application is mobile-responsive. This was achieved by using Bootstrap, which also gives the website a clean and clear UI/UX for the user. The application resizes with different viewports, with all features remaining on a mobile view.

## File Contents and Explanation:

- `capstone` project directory
	- `settings.py`
        - in `INSTALLED APPS` fitness was added to allow the web application to run.
        - my profile was added to `CSRF_TRUSTED_ORIGINS` to allow the web application to run.
	- `urls.py`
        - the `path("", include("fitness.urls"))` was added to allow the urls of the web application to run.

- `fitness` main project directory
	- `migrations` all the migrations of the web application.
	- `static`
		- `fitness/index.js`
            - this is the file containing all the necessary JavaScript for the web application. There are two main functions: the first allows an exercise to be updated by fetching the exercise and changing the DOM to allow the user to fill in the updated details of the exercise. The second function then saves the updated exercise to the database via a PUT method.
	- `templates`
		- `fitness/`
            - `answer.html`
                - This is a separate page where the trainer can recieve and answer any questions the client may have about their plan, workout, exercise or anything else. This page also has pagination put in place for all the questions, so as not to clog the webpage.
            - `clientworkouts.html`
                - This page displays all the workouts of a client's plan, along with all the exercises of each plan. The user can click on each exercise and they will be taken to a video link of the necessary exercise to be performed. This enables the user to fully understand what is expected of them. This is the page where a user can log and update the progress of each exercise in each workout.
            - `consultation.html`
                - This is a form for a client to fill out in order to get a plan with all the exercises and workouts for them to reach their fitness goals. The necessary information provided by the client is: age, gender, height, weight, fitness goal, current activity, previous exercise experience and any injuries or health issues. This information allows the trainer to create a bespoke plan for the client.
            - `createexercise.html`
                - This page allows the trainer to create exercises for their clients. Each exercise has a name, designated user/client, body part trained, a video link (musclewiki.com was used for the whole website) and exercise info, which is where all potential training variables for each exercise are placed. This allows the possibility for the trainer to set different variables for his clients whether that be sets, reps, weight, time, tempo or anything they wish. The video link allows the client to have a clear visual representation of the exercise and what is required of them, so the exercise can be performed correctly without the trainer present. The video links are accessible for the clients on their workout pages.
            - `createplan.html`
                - This is the form page to then group all of the workouts for a client into a single plan. The trainer can also give a lengthy amount of training notes to the client, so the client has an understanding of how to execute the plan in the best possible way.
            - `createworkout.html`
                - A form for the trainer to create unique workout names and assign them to his clients. These are the building blocks for the long term fitness plans of each client.
            - `createworkoutexercise.html`
                - This form allows the linkage of exercise to workout, as each workout will be comprised of many exercises. The exercises are ordered by user, so it is easier for the personal trainer to assign the correct exercises to the workout of the user.
            - `index.html`
                - When the trainer logs in they are directed to a page that lists all of the consultations that have been completed by their clients. The trainer can then use this information to construct the necessary exercises, workouts and plans for their client's goals. Pagination is used on this page, so the webpage doesn't become clogged up as the trainer builds their client base.
                - When a user/client logs in they are directed to a page that lists all of the plans created for them by their trainer. No plans will be displayed when the client first registers as they have not completed a consultation form. However, once a consultation form is filled out, then a plan will be displayed. The information displayed are all the workouts and the training notes of that plan. When clicking on the workout the user will be taken to their workouts page. Pagination is used on this page, so the webpage doesn't become clogged if the client continues to ask for more plans in the future.
            - `layout.html`
                - This page is the layout page and template that can be extended to all the other pages of the web application. It is the base for each html page.
            - `login.html`
                - This is the login page for users to login to the web application.
            - `question.html`
                - This page is a question section of the website. This allows clients to ask any questions they may have regarding their training or anything else to their trainer. The answers to those questions appear below the question form once they are answered.
            - `register.html`
                - This is the registration page for users to register to the web application.
    - `admin.py`
        - for the registration of `Consultation`, `Exercise`, `WorkoutExercise`, `Workout`, `Plan`, `Question` and `Answer` models in the admin page.
    - `forms.py`
        - `CreateConsultationForm` is the form created for client to fill out their information for the Personal Trainer.
        - `CreateExerciseForm` is the form used for the Personal Trainer to create exercises.
        - `CreateWorkoutForm` is the form used for the Personal Trainer to create workouts.
        - `CreateWorkoutExerciseForm` is the form used for the Personal Trainer link exercises and workouts.
        - `CreatePlanForm` is the form used for the Personal Trainer to create plans, which are made up of many workouts, for their clients.
        - `CreateQuestionForm` is the form used by clients to ask questions to their Personal Trainer.
        - `CreateAnswerForm` is the form used by the Personal Trainer to answer their client's questions.
    - `models.py`
        - `Consultation` is the model created for all the necessary information from a consultation to be saved to the database.
        - `Exercise` is the model used to store all the information about exercises created by the Personal Trainer and the storage of the training variables for the client.
        - `Workout` is the model for the storage of each workout for each client.
        - `WorkoutExercise` is the model for the connections of each exercise to each workout.
        - `Plan` is the model for the storage of the plans, created by the Personal Trainer, for their clients.
        - `Question` is the model for all the questions from clients to be stored in the database.
        - `Answer` is the model for all the answers to all the questions from clients to be stored in the database.
    - `urls.py`
        - contains all of the applications URL's and the necessary API's for all the fetch methods.
    - `views.py`
        - Function `index` which displays all plans for the user/client on their login and all completed consultations for the PT on their login. Pagination is also used on this page.
        - Function `login_view` which allows users to login to the web application.
        - Function `logout_view` which allows users to logout of the web application.
        - Function `register` which allows users to register to the web application.
        - Function `consultation` which renders the consultation form for clients to fill out.
        - Function `create_exercise` for the Personal Trainer to create exercises that are unique for each user and their workouts.
        - Function `create_workout` for the Personal Trainer to create workouts for users as part of a plan.
        - Function `create_workout_exercise` for the Personal Trainer to group exercises and workouts together.
        - Function `create_plan` for the Personal Trainer to create a plan, which is a group of workouts based on information from the client's consultation form.
        - Function `client_workouts` displays all the workouts and exercises for each user. Pagination is also present on this page.
        - Function `get_exercise` to be able to 'GET' all exercises via fetching in Javascript.
        - Function `update_exercise` to be able to update exercise variables in workouts via Javascript and 'PUT' method.
        - Function `question` for clients to ask questions about plans, workouts, exercises or anything else. All answers to those questions are rendered on the questions page and pagination is used so as not to clog the webpage.
        - Function `answer` for the Personal Trainer to answer client's questions. All questions are rendered on the answers page and pagination is used so as not to clog the webpage.
- `README.md` file describing the whole project.
- `requirements.txt` list of all the Python packages that need to be installed in order to run the web application.

## How to Run

cd into the project directory

Make sure all dependencies are installed from the requirements.txt with `pip install -r requirements.txt`

Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate` in the terminal.

Run `python manage.py runserver` to run the project.

## Any other additional information the staff should know

This was a challenging project and a lot of fun. I am a fully qualified personal trainer and have been for over a decade, later becoming a master trainer. This provided me with the insights to create this application. It allows a single trainer to create exercises, workouts and plans for their clients. For clients they can track the progress of their exercises and workouts. A one stop shop personal trainer client management system. This is something that would have been very helpful to me as a personal trainer.