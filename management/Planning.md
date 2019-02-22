# Project Planning Document

Include this Markdown file in the "Management" folder of your git repository and edit it accordingly.

## List of tasks and high level modules

Here an example:

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

* Initialize source directory (using Django CLI)
* Create a project template using Marvel, and create HTML and CSS templates modeled after it
* Create the project's primary models: Restaurant, Item, and User
* Create the project's primary views: Dashboard, List of Restaurants, Restaurant Detail, 
    List of Users, Configure)

This is just an example, your tasks should be more detailed.

## Gantt Chart

Assign concrete tasks to each team member and plan your time using a Gantt Chart.

## Research state of the art projects

Go online and search for open source projects written in Python that do what your team want to do.


Complete this table one row for each project. You should list at least one project for each team member (i.e. you should research at four different projects if your team has four team members)


| Project name with URL        | List of Features                | Technology                                 | Requirements          | Researcher                                 |
|------------------------------|---------------------------------|--------------------------------------------|-----------------------|--------------------------------------------|
| [ajax-django-CRUD](https://github.com/nithin-vijayan/ajax-django-CRUD) | Add, modify, and delete books | One page, to manage the list of books. Uses Django and AJAX. Web Application | Django==1.11., django-widget-tweaks==1.4.1, gunicorn==19.7.1, olefile==0.44, Pillow==4.1.1, python-decouple==3.0, pytz==2017.2, whitenoise==3.3.0 | fv6124 |
| [django-todo](https://github.com/shacker/django-todo) | Add, delete, modify tasks. Assing tasks to certain users. Search for tasks. | Django, AJAX | Django 2.0+, Python 3.6+, jQuery (full version, not "slim", for drag/drop prioritization), Bootstrap (to work with provided templates, though you can override them), bleach (pip install bleach) | fv6124 |
| [Gadfly](https://github.com/GiovineItalia/Gadfly.jl) | Renders publication quality graphics to SVG, PNG, Postscript, and PDF. Plotting and data visualization system using plots and graphs with multiple node types for intuitive interface interaction.  | DataFrames.jl, Snap.svg, Jupyter (out of the box). | Latest stable ver. 1.0.1, Python v3.7 | cq7409 |
| [ZODB](https://github.com/zopefoundation/ZODB) | A native object database for Python. Providing no seam between code and database, supporting graphs without joins. | ACID transactions with snapshot isolation, NoSQL databases, BTree support | Python 3.7, pypi v5.5.1 | cq7409 |
| [Project name 4](http://URL) | feature 1, feature 2, feature 3 | modules, architectures, frameworks, etc... | OS, modules, versions | Access ID of student who found this source |
| [Project name 4](http://URL) | feature 1, feature 2, feature 3 | modules, architectures, frameworks, etc... | OS, modules, versions | Access ID of student who found this source |
| [Project name 4](http://URL) | feature 1, feature 2, feature 3 | modules, architectures, frameworks, etc... | OS, modules, versions | Access ID of student who found this source |
| [Project name 4](http://URL) | feature 1, feature 2, feature 3 | modules, architectures, frameworks, etc... | OS, modules, versions | Access ID of student who found this source |

If you have difficulties finding projects similar to your project, search for different projects
but related (similar games, CRUD projects for different business, data analysis for different data, etc... ). You can also search for projects written in another language that you master.

[This website can help you to edit Markdown tables](https://www.tablesgenerator.com/markdown_tables#)
