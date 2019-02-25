# Project Planning Document

Include this Markdown file in the "Management" folder of your git repository and edit it accordingly.

## List of tasks and high level modules

Based on your project design and prototype, make a list of the modules and tasks to do.

### Architecture

Will be compose of 3 parts:
* Database, in SQL (we will use the DBMS mysql to interact with our backend)
* API Backend with Python (Library Django and Tastypie)
* Front-end web, a website


### Modules

* Login
* Add book
* Edit book
* Delete book
* Archive book

### Tasks

* Try Django and Tastypie to make a basic API
* Try to interact between Python (and Django/Tastypie) with SQL database
* Try to call the basic Python API on the front-end
* Design the SQL database (tables, relationships, ...)
* Development of the API
* Development of the front-end
* Testing (of API and front-end)
* Extra-feature, interact with external API (openlibrary.org) for example to retrieve all the information from one book with just the ISBN



## Gantt Chart

Our Gantt Chart is in a xlsx file in the Management folder this repository

## Research state of the art projects

Go online and search for open source projects written in Python that do what your team want to do.


Complete this table one row for each project. You should list at least one project for each team member (i.e. you should research at four different projects if your team has four team members)

| Project name with URL                               | List of Features                   | Technology                                   | Requirements                       | Researcher           |
|-----------------------------------------------------|------------------------------------|----------------------------------------------|------------------------------------|----------------------|
| [ https://openlibrary.org ]                         | Web based Book catalogue,          | Python, On top of Infogami wiki system       | Web app (all OS),                  | Vincent PICOT gr9185 |
| (https://github.com/internetarchive/openlibrary)    | Add/Edit book                      | (uses web.py framework), PostgreSQL          | list of Python dependencies below* |                      |
|-----------------------------------------------------|------------------------------------|----------------------------------------------|------------------------------------|----------------------|
| [ Library Assistant ]                               | Adds, renews, and issues books,    | JavaFX, JFoenix Library, Apache Derby        | Desktop Application (all OS),      | Hafsa Hussain gh7070 |
| (https://github.com/afsalashyana/Library-Assistant) | calculates fine, overdue reminders | (SARDB*), JavaMail API (email notifications) | JavaFX                             |                      |
|-----------------------------------------------------|------------------------------------|----------------------------------------------|------------------------------------|----------------------|
| [Project name 2](http://URL)                        | feature 1, feature 2, feature 3    | modules, architectures, frameworks, etc...   | OS, modules, versions              | Access ID of student |

*List of all the dependencies for OpenLibrary:
	Babel
	PIL
	argparse
	beautifulsoup4
	DBUtils
	genshi
	gunicorn
	iptools
	lxml
	psycopg2
	pymarc
	pytest
	python-memcached
	pyyaml
	simplejson
	supervisor
	web.py==0.33
	pystatsd
	eventer
	Pygments
	OL-GeoIP
	mockcache
-
*SARDB: StandAlone Relation DataBase
-
If you have difficulties finding projects similar to your project, search for different projects
but related (similar games, CRUD projects for different business, data analysis for different data, etc... ). You can also search for projects written in another language that you master.

[This website can help you to edit Markdown tables](https://www.tablesgenerator.com/markdown_tables#)
