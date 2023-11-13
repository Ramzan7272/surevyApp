# surveyApp

<br><br>

## How to start the project:
<br>

### 1. Clone the repository
```
git clone 'https://github.com/gmohmad/surveyApp.git'
```
### 2. Avtivate venv
```
venv\Scripts\activate
```
### 3. Install the dependencies
```
pip install -r requirements.txt
```
#### *You don't have to make migrations and migrate. I pushed the db here too, just so you have the specific questions and user (for customer). If you want to start from scrath, run these commands:
```
rm -f tmp.db db.sqlite3
rm -r my-app/migrations
python manage.py makemigrations
python manage.py migrate
```
### Run the server
```
python manage.py runserver
```
#### *Superuser credentials - username: user | password: qwerty999
