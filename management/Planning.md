# Project Planning Document

## List of tasks and high level modules

### Architecture

3 Layers:
* SQLite
* Django Models (Connected to SQLite)
* Business Layer (Users/Admin View)

### Modules

* Dashbord
* List of Restaurants
* Restaurant Detail view
* List of Users
* Configure Restaurants (Add/Delete/Update)
* Search

### Tasks

Completing the following tasks will allow us to begin fulfilling our application's requirements.

* Initialize source directory (using Django CLI)
* Create a project template using Marvel, and create HTML and CSS templates modeled after it
* Create the project's primary models: Restaurant, Item, and User
* Create the project's primary views: Dashboard, List of Restaurants, Restaurant Detail, 
    List of Users, Configure)


## Gantt Chart

Gannt Chart is available in the following directory: "management/Gannt Chart.xlsx"

## Research state of the art projects


| Project name with URL        | List of Features                | Technology                                 | Requirements          | Researcher                                 |
|------------------------------|---------------------------------|--------------------------------------------|-----------------------|--------------------------------------------|
| [ajax-django-CRUD](https://github.com/nithin-vijayan/ajax-django-CRUD) | Add, modify, and delete books | One page, to manage the list of books. Uses Django and AJAX. Web Application | Django==1.11., django-widget-tweaks==1.4.1, gunicorn==19.7.1, olefile==0.44, Pillow==4.1.1, python-decouple==3.0, pytz==2017.2, whitenoise==3.3.0 | fv6124 |
| [django-todo](https://github.com/shacker/django-todo) | Add, delete, modify tasks. Assing tasks to certain users. Search for tasks. | Django, AJAX | Django 2.0+, Python 3.6+, jQuery (full version, not "slim", for drag/drop prioritization), Bootstrap (to work with provided templates, though you can override them), bleach (pip install bleach) | fv6124 |
| [Gadfly](https://github.com/GiovineItalia/Gadfly.jl) | Renders publication quality graphics to SVG, PNG, Postscript, and PDF. Plotting and data visualization system using plots and graphs with multiple node types for intuitive interface interaction.  | DataFrames.jl, Snap.svg, Jupyter (out of the box). | Latest stable ver. 1.0.1, Python v3.7 | cq7409 |
| [ZODB](https://github.com/zopefoundation/ZODB) | A native object database for Python. Providing no seam between code and database, supporting graphs without joins. | ACID transactions with snapshot isolation, NoSQL databases, BTree support | Python 3.7, pypi v5.5.1 | cq7409 |
| [Django CRUD Example Apps](https://github.com/rayed/django_crud) | A Django project that demonstrates CRUD functionality using 3 small applications | Python 3, Django 2 | version 1.8 | gf6643 |
| [School Library Database Application](https://github.com/itskpalusa/School-Library-Database-Application) | A school library database implemented with python and sqlite| Python 3, sqlite 3| version 1.0 | gf6643 |


