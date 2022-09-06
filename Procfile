release: python manage.py migrate --no-input
web gunicorn blog_permissions.wsgi:application --log-file -