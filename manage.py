#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')
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

"""
Note to self:

create superuser:
python manage.py createsuperuser

need migrations:
python manage.py makemigrations

SQLite for development:
postgres for production'

>>> python manage.py shell
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> post_1 = Post(title='First Post', content='This is the first post content', author=user)
>>> post_2 = Post(title='Second Post', content='This is the second post content', author=user)
>>> post_3 = Post(title='Third Post', content='This is the third post content', author=user)
>>> post_1.save()
>>> post_2.save()
>>> post_3.save()

Part 6: User registration

"""