To Run server: navigate to the outer pytest_exercise directory then run on cmd line "python manage.py runserver"
  * Navigate to this url on your internet browser http://127.0.0.1:8000/myapp/
  
To Run PyTest test Cases: navigate to the outer pytest_exercise directory then run on cmd line "py.test"
  * The HTML report will be created on htmlcov directory as "index.html"

To see DB changes must navigate to http://127.0.0.1:8000/admin/myapp/
* Go to Bots DB Model
  * user: admin pw: 1
  * if it does not work create a admin user 
      * navigate to the outer pytest_exercise directory then run on cmd line "python manage.py createsuperuser" then create user then run "python manage.py runserver" afterwards
