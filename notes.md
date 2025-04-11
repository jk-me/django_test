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
- Django has sqlite built in, [to add other db](https://docs.djangoproject.com/en/5.1/topics/install/#get-your-database-running)

## Migrations and Models

- `python3 manage.py migrate` to migrate
- initial migrations on setup refer to INSTALLED_APPS in **mysite/settings.py**
- Creating a model
  - myapp/models.py - add model definitions here
  - for first models, need to activate app in project
    - in INSTALLED_APPS in myproject/settings.py file, add `polls.apps.PollsConfig` - class is defined in myapp/apps.py
  - `python3 manage.py makemigrations polls` - detects changes in models and creates migration file
  - `python manage.py sqlmigrate polls 0001` - prints sql in terminal that will be run for that migration number
  - [python manage.py check](https://docs.djangoproject.com/en/5.1/ref/django-admin/#django-admin-check) (System check for errors in entire project w/o touching db or migrations)
- Model defaults
  - default ids are integers and auto created, need to set up separately as uuid and primary key or have another field
  - fields are not null by default. set null=True in definition for otherwise

## Python shell (~ rails console)

- [Tutorial pt 2 - playing with the API](https://docs.djangoproject.com/en/5.1/intro/tutorial02/#playing-with-the-api)
- `python3 manage.py shell`
- manipulating model objects
  - import first `from polls.models import Choice, Question`
  - check tutorial examples. filter by id, property_startswith=”search term”. get(property=searchterm). queryset[0] can manipulate like array
    - [Related Objs Documentation](https://docs.djangoproject.com/en/5.1/ref/models/relations/) can use relationship properties in filter, separate by double underscore (choice, question) `Choice.objects.filter(question__pub_date__year=current_year)`
  - create `q = Question(question_text="What's new?", pub_date=timezone.now())` and then q.save(). or use Question.objects.create()
  - [QuerySet Documentation | Field Lookups](https://docs.djangoproject.com/en/5.2/ref/models/querysets/#field-lookups) - double underscore methods that can be chained onto a field to get more specific data (year of date) or comparisons (greater than, contains)

### Examining views using test tools

```
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client
# create an instance of the client for our use
client = Client()
response = client.get("/") # examine response for content, context, status code, etc.
```

- setup_test_environment installs a template renderer. can examine response context but uses existing db, not a test db. [Advanced Testing Topics](https://docs.djangoproject.com/en/5.1/topics/testing/advanced/#django.test.utils.setup_test_environment)
- [Testing Tools and django.test.Client](https://docs.djangoproject.com/en/5.1/topics/testing/tools/#testing-tools)

## Admin User

- `python manage.py createsuperuser` prompts to create login w email

## Pt 3 - Views and templates

- ROOT_URL_CONF in settings points to urls.py file with available urlpatterns
- TEMPLATES in settings describes how django loads them, by default it looks for templates/ in each INSTALLED_APPS directory. In this case it only searches inside templates/ folders and does not use full paths, so namespacing is helpful.
- Templates
  - [Django Docs | Template Guide](https://docs.djangoproject.com/en/5.1/topics/templates/)
  - [Django Docs | Built in template helpers](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#std-templatetag-for)
    - `extends` from a base template
    - `include` a partial

## Testing

- Naming convetions
  - Django will automatically find test files that begin with `test`. For ex. `polls/tests.py`
  - test methods also should begin with `test`
- Run tests for all INSTALLED_APPS with `python manage.py test` . Can also test an app with `python manage.py test polls`
- When using django.test.TestCase, each test is wrapped in a transaction and rolled back after the test finishes. So db is reset btwn tests
  - [TestCase docs](https://docs.djangoproject.com/en/5.1/topics/testing/tools/#testcase)
- Further reading
  - [Django's LiveServerTestCase for Selenium tests](https://docs.djangoproject.com/en/5.1/topics/testing/tools/#liveservertestcase)
  - [Coverage.py external library for checking test coverage](https://docs.djangoproject.com/en/5.1/topics/testing/advanced/#integration-with-coverage-py)

## Static Files

- [STATICFILES_FINDERS](https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-STATICFILES_FINDERS) in settings (not in standard setup settings)
  - default is to look for `static/` directory in each INSTALLED_APPS folder
  - use namespacing like templates file structure from pt3
  - `{% static 'polls/style.css' %}` static template tag for use in files processed by django (like html templates) not static files themselves. This tag relies on STATIC_URL to generate path urls.
