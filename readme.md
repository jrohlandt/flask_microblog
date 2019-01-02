# New Flask Project
1. mkdir myproject && cd myproject
2. python3 -m venv venv (2nd venv is the name of the venv dir)
3. source venv/bin/activate
4. pip install flask


# Start app
1. export FLASK_APP=microblog.py (see python-dotenv to skip this)
2. flask run


# Migrations 
uses: https://github.com/miguelgrinberg/flask-migrate
1. flask db init (to create the migrations directory and Alembic files)
2. flask db migrate (creates the migration files with upgrade and downgrade functions)
3. flask db upgrade (runs the migrations on the database)
4. flask db downgrade (rolls back the last migration)