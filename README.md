<img title="LapZoneAPI" alt="Header image" src="./header.png">

_API (Django + DRF) for my Internet shop [LapZone](https://lapzone.tech)_

## Purpose

My Internet shop [LapZone](https://lapzone.tech) ([GitHub](https://github.com/Gubchik123/LapZone)) was written using templates, but in our time there are not a lot of projects that use templates. That's why here is API of the "LapZone"

## Project modules

<a href='https://pypi.org/project/Django'><img alt='Django' src='https://img.shields.io/pypi/v/Django?label=Django&color=blue'></a> <a href='https://pypi.org/project/djangorestframework'><img alt='djangorestframework' src='https://img.shields.io/pypi/v/djangorestframework?label=djangorestframework&color=blue'></a> <a href='https://pypi.org/project/django-ckeditor'><img alt='django-ckeditor' src='https://img.shields.io/pypi/v/django-ckeditor?label=django-ckeditor&color=blue'></a> <a href='https://pypi.org/project/django-cors-headers'><img alt='django-cors-headers' src='https://img.shields.io/pypi/v/django-cors-headers?label=django-cors-headers&color=blue'></a> <a href='https://pypi.org/project/django-filter'><img alt='django-filter' src='https://img.shields.io/pypi/v/django-filter?label=django-filter&color=blue'></a> <a href='https://pypi.org/project/django-rest-framework-social-oauth2'><img alt='django-rest-framework-social-oauth2' src='https://img.shields.io/pypi/v/django-rest-framework-social-oauth2?label=django-rest-framework-social-oauth2&color=blue'></a> <a href='https://pypi.org/project/djoser'><img alt='djoser' src='https://img.shields.io/pypi/v/djoser?label=djoser&color=blue'></a> <a href='https://pypi.org/project/drf-social-oauth2'><img alt='drf-social-oauth2' src='https://img.shields.io/pypi/v/drf-social-oauth2?label=drf-social-oauth2&color=blue'></a> <a href='https://pypi.org/project/drf-yasg'><img alt='drf-yasg' src='https://img.shields.io/pypi/v/drf-yasg?label=drf-yasg&color=blue'></a> <a href='https://pypi.org/project/Pillow'><img alt='Pillow' src='https://img.shields.io/pypi/v/Pillow?label=Pillow&color=blue'></a> <a href='https://pypi.org/project/psycopg2'><img alt='psycopg2' src='https://img.shields.io/pypi/v/psycopg2?label=psycopg2&color=blue'></a> <a href='https://pypi.org/project/python-dotenv'><img alt='python-dotenv' src='https://img.shields.io/pypi/v/python-dotenv?label=python-dotenv&color=blue'></a> <a href='https://pypi.org/project/pytz'><img alt='pytz' src='https://img.shields.io/pypi/v/pytz?label=pytz&color=blue'></a> 

> Look at the requirements.txt

## Environment Variables

To run this project, you will need to add the environment variables

> Look at the file_env_example.txt

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/Gubchik123/LapZoneAPI.git
    ```

2. Go to the project directory:

    ```
    cd LapZoneAPI
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```
    python manage.py migrate
    ```

5. Run the development server:
    ```
    python manage.py runserver
    ```

    > **Note:** Don't forget about environment variables