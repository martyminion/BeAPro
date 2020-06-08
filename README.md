# BeAPro

This is python Web app made with the Django, it enables user to vote on particular projects, based on parameters like Design, Usability and Content

### User Stories:
1. View posted projects and their details
1. Post a project to be rated/reviewed
1. Rate/ review other users' projects
1. Search for projects 
1. View projects overall score
1. View my profile page

### User Journey
1. a new user can view all the projects and search for particular projects
1. On registering the user is prompted to add some more information for their profile
1. from the users profle a user can upload a new project and add the relevant details, eg a description, title and a landing page photo
1. the user can also updat their profile once logged in
1. authenticated users can rate other users projects 


## Set up and Installation
### Prerequisites
The user will require git, django, postgres and python3.6+ installed in their machine.
To install these two, you can use the following commands
```
#git
$ sudo apt install git

#python3.6
$ sudo apt-get install python3.6.

#django
$ pip install django==3.0.6

#postgres
$ pip install psycopg2 
```
### Requirements
1. asgiref==3.2.7
1. astroid==2.4.1
1. beautifulsoup4==4.9.1
1. Django==3.0.6
1. django-bootstrap4==1.1.1
1. isort==4.3.21
1. lazy-object-proxy==1.4.3
1. mccabe==0.6.1
1. Pillow==7.1.2
1. psycopg2==2.8.5
1. pylint==2.5.2
1. pyperclip==1.8.0
1. python-decouple==3.3
1. pytz==2020.1
1. six==1.15.0
1. soupsieve==2.0.1
1. sqlparse==0.3.1
1. toml==0.10.1
1. typed-ast==1.4.1
1. wrapt==1.12.1
 1. use the requirements.txt to get full list of dependencies
### .ENV file
1. SECRET_KEY='<SECRET_KEY>'
1. DEBUG=True #set to false in production
1. DB_NAME='databasename'
1. DB_USER='username'
1. DB_PASSWORD='password'
1. DB_HOST='127.0.0.1'
1. MODE='dev' #set to 'prod' in production
1. ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
1. DISABLE_COLLECTSTATIC=1
1. for cloudinary support add clodinary config fields

### Installation
1. To access this application on your command line, you need to clone it 
`https://github.com/martyminion/BeAPro.git`
1. Create a requirements.txt in the root folder and copy the requirements above.
1. Install the required technologies with
`pip install -r requirements.txt`
1. Create a .env file and copy the .env code above
1. You can then run the server with:
`python3.6 manage.py runserver`
1. You can make changes to the db with
`python3.6 manage.py makemigrations award`
`python3.6 manage.py migrate`
4. You can run tests:
`python3.6 manage.py test award`


### Break down into end to end tests
### Example
  ```
   def test_get_user_profile(self):
    userprof = Profile.get_user_profile(self.user_kim)
    self.assertEqual(userprof.user.username,self.user_kim.username)

  ```
* The above test tests if a user's profile can be retrieved from the database, and if it is the correct profile returned

## API calls
1. Use the following api end point to generate a token
    *Note all end points require authenticated users to access*
    1. for the local environment
        `http://127.0.0.1:8000/api-token-auth`
1. To get user profiles 
    GET: `http://127.0.0.1:8000/api/profiles`
1. To get projects
    GET: `http://127.0.0.1:8000/api/projects`
    
## Bugs
  No  bugs as of yet, if encountered you can get me on *martyminion0@gmail* or log an issue from github


## Deployment

The app can be found live on heroku: 
## Built With

* Python 3.6.9 
* Django Framework 3.0
* JavaScript and JQuery
* HTML and CSS

## Authors

* **Martin Kimani** 

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details
Copyright{ 2020 }
