release: python manage.py migrate --no-input
web gunicorn blogapi.wsgi:application --log-file -