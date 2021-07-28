## Django Showcase

A simple website with learning and practice projects using Django, Python, HTML, CSS, and JavaScript.

* /polls/ is a website made while following the [Django official tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/), with additional comments.

* /calc/ is a simple web calculator made for practice.

* /viz/ is a **data visualization webapp**. It pulls data from BoardGameGeek's database and offers various options for displaying and interacting with the data. Currently visualization is done via Seaborn and returned as static image files.

![ss](https://user-images.githubusercontent.com/69309175/127333744-3c0783db-6542-4d7f-8233-53b6c8c056db.png)

To run locally:
* `git clone https://github.com/erperreault/django-learning`
* From the django-learning directory, `python -m venv venv` to create a new virtual environment
* `source venv/bin/activate` to start the virtual environment
* `pip install -r requirements.txt` to install dependencies
* From then on, `python manage.py runserver` while in your virtual environment to run the project

Access the polls app at http://localhost:8000/polls, calc at http://localhost:8000/calc/, viz at http://localhost:8000/viz/ and admin features at http://localhost:8000/admin/.
