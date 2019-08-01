#Polls app using Django Framework

**Dependencies**
----------------------------------
1.Python version 3.7.4
2. Django version 2.2
   - pip install django==version
3. Database:
   - Django comes with Sqlite Database by default: *this project use Sqlite3*
   -If you want to use any other Database
      - install the appropriate database buildings
      - you need to provide user,password and host in settings.py file

**Steps to run:**
----------------------------------
1. Make virtaul environment:
   - pip install virtualenv (to install virtual environment)
   - virtaulenv <name_of_virtual_environment>
2. Clone the repository
3. Go to the project folder
4. Run follwing commands:
   - python manage.py makemigrations (for database createion)
   - python manage.py migrate (for coomiting changes in database)
   - python manage.py runserver (to start Django server)
5. open "http://127.0.0.1:8000/polls"

