Welcome to the movie-together app!

It is built using Django and various other plugins/packages

How to install:
- Make sure python is installed
    - Download on python's official website
- Make sure pipenv is installed
    - pip install pipenv

- Run pipenv install


To start the backend server for local testing:
- Make sure you are in the main folder
- Run python manage.py runserver

Front-end section:

To run the testing files
- Run pipenv run coverage run --source='.' manage.py test
- To view an html of the report in your browser
    - Run coverage html
- To view in terminal
    - Run coverage report












Notes:
There's 3 type of writing views for the Django REST framework, we went with generic API views in the serializers.py

DONE:
-Create a movie model which could be useless
-Create an api that can do post and get for the movie
NEXT:
