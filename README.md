# Task Manager Application

## Description

This Task Manager Application, using the 'Model-View-Template' pattern,
allows users to manage their tasks efficiently. Users can:

* View all tasks
* Create new tasks
* Edit existing tasks
* Delete tasks
* View tasks due today
* See past deadlines
* See related categories, deadlines, and priorities

## Getting started

Follow these simple steps to get started with the Task Manager Application:

1. Ensure that Python and Pip are installed on your machine <br />
2. Clone the repository to your local machine <br />
   `git clone `
3. Navigate to the project directory <br />
   `cd `
4. Open Visual Studio Code <br />
   `code .`
5. Set up a virtual environment in Visual Studio Code terminal in a directory that
you want to store your project in <br />

   Using venv:

   `python -m venv venv` <br />
   For Python 3.3 or newer: <br />
   `python3 -m venv venv`

   Using virtualenv:

   ```
   pip install virtualenv
   virtualenv venv
   ```

6. Activate the virtual environment

   Using venv:

   Windows: <br />
   `venv\Scripts\activate` <br />
   Unix\Mac: <br />
   `source venv/bin/activate`

   Using virtualenv: <br />

   Windows: <br />
   `venv\Scripts\activate` <br />
   Unix\Mac: <br />
   `source venv/bin/activate`

7. Ensure project dependencies are installed: <br />

`pip install -r requirments.txt`

8. Run the following command to start the Django server: <br />
   `python manage.py runserver`

   Click on the link that shows in the terminal to open the application in your browser.

## Accessing the Database 📊

To delve into the database, I highly recommend utilising DB Browser for its exceptional
quality and user-friendly visual interface. Plus, it's free!

1. Download DB Browser <br />
If you haven't already, download and install [DB Browser for SQLite](https://sqlitebrowser.org/dl/).

2. Open Database with DB Browser <br />
Locate and open the database file using the 'Open Database' option (located at the top left).
It should be inside the project directory.

3. Explore the Database <br />
Once the database is opened, click on the 'Browse Data' tab and select the table dropdown.
Click on 'tasks_task'.

You're all set! Start managing your tasks efficiently with the Task Manager Application.

## Credits
### Contact

If you have any questions or just want to connect, you can reach me on
[LinkedIn](https://www.linkedin.com/in/andyagyeidwumah/)