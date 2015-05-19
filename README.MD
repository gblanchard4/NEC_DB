# NEC DB
A relational database using Python and Postgres for Ferris Lab

## Setup
After cloning the repo, these steps will compete the setup the the app

You will need virtualenv installed on you machine `pip install virtualenv`

1. VirtualEnv and Django
  * You will need virtualenv installed on you machine `pip install virtualenv`
  * In the root directory run `virtualenv env` to create a new virtual python for this app. 
  * Source the new python with `source ./env/bin/activate`
    * You can check if you are using the virtualenv python with the command `which pip`, it should return `NEC_DB/env/bin/pip`
  * Install Django: `pip install django`


2. Database
  * The SQLite database will automatically be created

3. Migrate the database
   * `python manage.py migrate`

4. Create an admin user
  * `python manage.py createsuperuser`
  * `Username: admin`
  * `Email address: admin@example.com`
  * Enter password

 5. Run Server
   * `python manage.py runserver`

## Pulling New Schemas
### With Changes To Models
`python manage.py makemigrations patients`
`python manage.py migrate`  

#### Apply my changes 
1. `git pull` 
2. `python manage.py migrate`