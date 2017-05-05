# playing-with-django

To run the app (using mkvirtualenv):
```bash
$> cd StarWarsEncyclopedia
$> mkvirtualenv StarWarsEncyclopedia
$> pip install --upgrade pip
$> pip install -r requirements.txt
$> python manage.py makemigrations
$> python manage.py migrate
$> python manage.py createsuperuser
$> python manage.py runserver
```
And open http://localhost:8000/ in your browser.
