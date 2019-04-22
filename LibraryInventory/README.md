**LIBRARY INVENTORY**

This is a school project having for goal to simulate an university bookstore.

**Installation guide:**

   - Be sure to have `MySql 5.0 or higher installed and running on your platform
    
   - Create a database for the project in MySql, if you don't have another user than root, please consider creating a new user with access to only this project database
  
   - Copy the `.env.example` file and rename it `.env`, then fill the file - `DB_NAME` is for the database name you just created, `DB_USER` and `DB_PASSWORD`is for the user that is going to access the database 
    
   - Install Python 3.6 or higher
    
   - Install python package `Virtualenv` https://virtualenv.pypa.io/en/stable/

   - Create a new virtualenv and activate it (Follow the documentation linked above) **Everything bellow need to be done in the virtualenv**
   
   - Install `Django` 2.1 or higher https://docs.djangoproject.com/en/2.2/topics/install/ be sure to follow all the steps
    
   - If you didn't through the Django installation guide, install `mysqlclient` https://pypi.org/project/mysqlclient/

   - Install `django-bootstrap-customizer` 0.1.4 or higher https://johnfraney.github.io/django-bootstrap-customizer/

   - Be sure to be in the root folder of the project before doing the folowing commands
    
   - run `python3 manage.py migrate`
    
   - run `python3 manage.py createsuperuser` You'll need this user to connect to the admin site, be sure to know the access of this user
    
   - run `python3 manage.py runserver`

   - Go to: http://127.0.0.1:8000/admin/ for the admin site
    
   - Before going to the user site, go to the admin site and create a bootstrap theme and link it to the user site url (Examples in the django-bootstrap-customizer documentation)
   
   - Check the id in the table `django-site` of the user site you linked above. In `settings.py` change `SITE_ID` with this id.
    
   - Go to: http://127.0.0.1:8000 for the user site

   - You're all set, have fun!

   - If you are installing on a server instead of local, go to the documentation of `Django`, there is a tutorial on how to deploy a django project.