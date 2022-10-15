# Online Polls and Surveys Web Application 

![Unit test](https://github.com/jaybjackie/ku-polls/actions/workflows/python-app.yml/badge.svg)
[![codecov](https://codecov.io/gh/jaybjackie/ku-polls/branch/main/graph/badge.svg?token=DUYVPI5GL4)](https://codecov.io/gh/jaybjackie/ku-polls)
Allow KU communities to create and participate in any polls and surveys on **KU Polls**. <br>

The app was built using [Django](https://www.djangoproject.com/). <br>
App created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

# How to Install and Run

1. Clone this project repository to your local machine
````
git clone https://github.com/jaybjackie/ku-polls.git
````
2. Go to  this repository directory<br>
   
   for `MacOS/Linux`
   ````
   cd ku-polls
   ````
   
   for `WindowOS`
   ````
   cd .\ku-polls\
   ````

3. Create a virtual environment. <br>

    ````
    python -m venv venv
    ````

4. Activate the virtual environment.<br>

    - for `MacOS/Linux`<br>
    ````    
    . venv/bin/activate
    ````

    - for `WindowOS`<br>
        
    ````
    .\venv\Scripts\activate
    ````
        
    In case `cannot be loaded because running scripts is disabled on this system`
        
     To enable, on Window PowerShell(Terminal/ Command Prompt) run as administrator this commmand:
     ````
    Set-ExecutionPolicy RemoteSigned
    ````
    
    If you want to disable:
    ````
    Set-ExecutionPolicy Restricted
    ````
    
5. Install required packages.

````
pip install -r requirements.txt
````

6. Create `.env` file in `mysite/` and modify by the following lines:

````
# Create a secret key using ...
# python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

SECRET_KEY = YOUR-SECRET-KEY
DEBUG = False
ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']
````    

7. Migrate the database.

    for `MacOS/Linux`
    ````
    python manage.py migrate
    ````
    
    for `WindowOS`
    ````
    python .\manage.py migrate
    ````
    
8. Initialize data

    for `MacOS/Linux`
    ````
    python manage.py loaddata data/users.json polls.json
    ````
    
    for `WindowOS`
    ````
    python .\manage.py loaddata .\data\users.json .\polls.json
    ````

9. Run the server.
 
   for `MacOS/Linux`
   ````
   python manage.py runserver
   ````
   
   for `WindowOS`
    ````
    python .\manage.py runserver
    ````
 
 Go to the app:
[http://localhost:8000/](http://localhost:8000/)

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Vision Statement](../../wiki/Vision%20Statement)<br>
- [Requirements](../../wiki/Requirements)<br>
- [Development Plan](../../wiki/Development%20Plan)<br>

## DEMO run
You can uses these demo users below to visits the site.

| Username  | Password  |
|-----------|-----------|
|   jay   | Thisis1stuser |
|  jerome | Thisis2nduser |


***
### Useful Link
[django-tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial01/) <br>
[Django Girl Tutorial](https://tutorial.djangogirls.org/en/) Tutorial with really good explanation.
