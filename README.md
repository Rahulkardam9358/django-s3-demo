# Demo: s3 Bucket for django media

## Clone repository
```bash
$ git clone https://github.com/Rahulkardam9358/django-s3-demo.git
$ cd django-s3-demo
```

## Create python virtual environment
```bash
$ python3 -m venv venv
$ # activate virtual environment
$ source venv/bin/activate
$ pip install -r requirements.txt
```
          ---OR if using pipenv---
```bash
$ pipenv --python 3.8
$ pipenv shell
$ pipenv install -r requirements.txt
```

## Create environment file
```bash
$ touch .env
```
### Add following variables and their values in .env file( values will be added without quotes )
    AWS_STORAGE_BUCKET_NAME = bucket_name
    AWS_ACCESS_KEY_ID = access_id
    AWS_SECRET_ACCESS_KEY = secret_access_key

## Running project
```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```


### Thank you