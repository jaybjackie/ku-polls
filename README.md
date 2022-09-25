# Online Polls and Surveys Web Application 

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

    you can name virtual environment with any. <br>
    but the 2 common names are `venv` or `env`

    for `venv`
    ````
    python -m venv venv
    ````
    and for `env`<br>
    
       python -m venv env

4. Activate the virtual environment.<br>

    - for `MacOS/Linux`<br>
    ````
    source venv/bin/activate
    ````
    or<br>
    ````    
    . venv/bin/activate
    ````

    - for `WindowOS`<br>

        for virtual environment named `venv`
        ````
        .\venv\Scripts\activate
        ````
        
        for virtual environment named `env`
        ````
        .\env\Scripts\activate
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
DEBUG=True
SECRET_KEY=Your-Secret-Key
ALLOWED_HOSTS=localhost,127.0.0.1
````    

   to generates your `SECRET_KEY`, type following command in the terminal.

   ````
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ````
   
place `Your-Secret-Key` in `.env` file.

7. Migrate the database.

    for `MacOS/Linux`
    ````
    python manange.py migrate
    ````
    
    for `WindowOS`
    ````
    python .\manage.py migrate
    ````
    
8. Initialize data

    for `MacOS/Linux`
    ````
    python manange.py loaddata users polls
    ````
    
    for `WindowOS`
    ````
    python .\manage.py loaddata users polls
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
