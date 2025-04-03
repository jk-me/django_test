## Python env set up

- Set up venv and install django in docs
- To see django version
  - `pip show django` (or pip3)
  - or `python -m django --version`
- Activate venv before starting up a session https://docs.python.org/3/tutorial/venv.html
  - `source ~/.virtualenvs/djangodev/bin/activate`
  - To create a venv:
    - `python3 -m venv ~/.virtualenvs/djangodev`
  - To deactivate:
    - `deactivate`
  - venv is tied to python version

## Start App

- `python3 manage.py runserver`

- auto refresh except for adding files, check runserver ref for running on other ports
- Django has sqlite built in, to add other db https://docs.djangoproject.com/en/5.1/topics/install/#get-your-database-running

## Migrations and Models

- `python3 manage.py migrate`
- initial migrations on setup refer to INSTALLED_APPS in **mysite/settings.py**
- Creating a model
  - myapp/models.py - add model definitions here
  - for first models, need to activate app in project
    - in INSTALLED_APPS in myproject/settings.py file, add `polls.apps.PollsConfig` - class is defined in myapp/apps.py
  - `python3 manage.py makemigrations polls` - detects changes in models and creates migration file
  - `python manage.py sqlmigrate polls 0001` - prints sql in terminal that will be run for that migration number
  - [\*\*`python manage.py check`](https://docs.djangoproject.com/en/5.1/ref/django-admin/#django-admin-check)\*\* https://docs.djangoproject.com/en/5.1/ref/django-admin/#django-admin-check (Checks for errors w/o touching db or migrations)
- Model defaults
  - default ids are integers and auto created, need to set up separately as uuid and primary key or have another field
  - fields are not null by default. set null=True in definition for otherwise

## Python shell (~ rails console)

- [Tutorial pt 2 - playing with the API](https://docs.djangoproject.com/en/5.1/intro/tutorial02/#playing-with-the-api)
- `python3 manage.py shell`
- manipulating model objects
  - import first **`from** **polls.models** **import** Choice, Question`
  - check tutorial examples. filter by id, property_startswith=”search term”. get(property=searchterm). queryset[0] can manipulate like array
    - [Related Objs Documentation](https://docs.djangoproject.com/en/5.1/ref/models/relations/) can use relationship properties in filter, separate by double underscore (choice, question) `Choice**.**objects**.**filter(question__pub_date__year**=**current_year)`
  - create `q **=** Question(question_text**=**"What's new?", pub_date**=**timezone**.**now())` and then q.save(). or use Question.objects.create()
  - QuerySet documentation
    - [QuerySet Documentation | Field Lookups](https://docs.djangoproject.com/en/5.2/ref/models/querysets/#field-lookups) - double underscore methods that can be chained onto a field to get more specific data (year of date) or comparisons (greater than, contains)

## Admin User

- `python manage.py createsuperuser`prompts to create login w email
