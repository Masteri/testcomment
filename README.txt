
sudo easy_install pip
sudo apt-get install python-virtualenv or sudo pip install virtualenv
virtualenv env          #creating folder with virtual envoirement scripts
source env/bin/activate
git clone https://github.com/Masteri/testcomment.git
cd testcomment/
sudo pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations appcoment
python manage.py migrate
python manage.py createsuperuser #user:Admin password:
go to 127.0.0.1/admin and authorizing
python manage.py runserver

Click to "Add some random Data" to add some data :)

I want to fix paginating, update like, and scrip that fill database random datas, for example bulk_create()



