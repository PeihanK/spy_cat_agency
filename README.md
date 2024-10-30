### Overview

This task involves building a CRUD application. The goal is to create a system that showcases your understanding in building RESTful APIs, 
interacting with SQL-like databases, and integrating third-party services.

### Requirements

Spy Cat Agency (SCA) asked you to create a management application, so that it simplifies their spying work processes. SCA needs a system to 
manage their cats, missions they undertake, and targets they are assigned to. From cats perspective, a mission consists of spying on targets 
and collecting data. One cat can only have one mission at a time, and a mission assumes a range of targets (minimum: 1, maximum: 3). 
While spying, cats should be able to share the collected data into the system by writing notes on a specific target. 
Cats will be updating their notes from time to time and eventually mark the target as complete. If the target is complete, notes should be 
frozen, i.e. cats should not be able to update them in any way. After completing all of the targets, the mission is marked as completed.

From the agency perspective, they regularly hire new spy cats and so should be able to add them to and visualize in the system. SCA should
be able to create new missions and later assign them to cats that are available. Targets are created in place along with a mission, meaning 
that there will be no page to see/create all/individual targets.

1 Clone the repository 
git clone spy_cat_agency
cd spy_cat_agency
2 Create and activate a virtual environment:
python -m venv .venv
.venv\Scripts\activate
3 Install the project dependencies:
pip install -r requirements.txt
4 Run migrations to set up the database:
python manage.py makemigrations
python manage.py migrate
5 Create a superuser for accessing the Django admin panel:
python manage.py createsuperuser
6 Start the development server:
python manage.py runserver

