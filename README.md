## Web Scratchpad

A simple website with learning and practice projects using Django, Python, HTML, CSS, and JavaScript.

* /polls/ is a website made while following the [Django official tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/), with additional comments.

* /calc/ is a simple web calculator made for practice.

* /viz/ is an (in-progress) data visualization webapp. It pulls data from BoardGameGeek's database and offers various options for displaying and interacting with the data. Currently visualization is done via Seaborn and returned as static image files.

To run locally, first ensure that you have Python and Django installed:

```
$ python --version
Python 3.9.5
$ python -m django --version
3.2.3
```

If either is missing, follow the [official installation instructions](https://docs.djangoproject.com/en/3.2/intro/install/). 

Then, `git clone https://github.com/erperreault/` and run `python manage.py runserver` from the base directory. Access the polls app at http://localhost:8000/polls, calc at http://localhost:8000/calc/, and admin features at http://localhost:8000/admin/.
