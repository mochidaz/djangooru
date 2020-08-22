# Djangooru
Danbooru-like taggable image board written in django

## Installation
1. Clone the repo
2. run `pip install -r requirements.txt` 
3. Install postgresql
4. Create media directory
5. Create new psql db
6. Set the db in `settings.py`
7. run `python manage.py migrate` (If migrate doesn't work, create migrations folder with `__init__.py` in accounts and posts directory and run `python manage.py makemigrations` then run migrate again)
8. run `python manage.py runserver`

## TO-DOs
- ~~Make the tags query params, not paths~~ (Actually both)
- ~~Make the search bar works~~
- ~~Make the search bar works __Globally__~~
- Create better design (I'd be really happy if someone could contribute to this)
