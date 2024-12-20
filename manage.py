#!/usr/bin/env python
import os
import sys
import psycopg2

from dotenv import load_dotenv


load_dotenv()

def check_database_connection():
    """Check Database connection"""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
        )
        conn.close()
        print("Database connection successful")
    except Exception as e:
        print("Database connection error:", e)
        exit(1)

if os.environ.get('RUN_MAIN') != 'true':
    print("Skipping initial execution due to auto-reloader")
else:
    if not os.getenv('VIRTUAL_ENV'):
        print("Warning: It looks like virtual environment is not activated")
    else:
        print("Virtual environment activated")

    check_database_connection()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forum2.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
