pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations appcoment
python manage.py migrate
python manage.py createsuperuser #user:Admin password:
go to 127.0.0.1/admin and authorizing
python manage.py runserver

Click to "Add some random Data" to add some data :)



