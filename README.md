# SmartBusinessBD API with Django and Rest API

SmartBusinessBD API is designed with Django and Restful API. For front end React is used.

## Requirements 
* Python 3.6 or above
* Django 2.0

## Install Dependencies

Create a virtual environment using `pip` or `pip3` before installing dependencies

```
pip3 install virtualenv
```
```
virtualenv venv
```

Activate the virtual environment `venv`

```
source venv/bin/activate
```

For development install `development.txt` inside `requirements` folder

``` 
pip install -r requirements/development.txt
```


## Database Setup

Once a database is created migrate the models

``` 
python manage.py makemigrations
```
``` 
python manage.py migrate
```

Create and configure the `.env` file. You can find a `.env` configuration example in the file called `.env.example` in the project folder

Run the project with

```
python manage.py runserver
```

Create a superuser to get access to admin

```
python manage.py createsuperuser
```


Check the `urls.py` inside `coreapi` folder and navigate to the urls to view the outputs.