``` cd builds/ && grunt; cd ..```
### its do run watch node.js, auto:
- compiles .coffee in .js, where detecting js modify;
- so concat Angular Files in a just file;
- and min this file;
- compile less in css, where detecting less modify;

Set configure to Heroku:
manage.py:
``` os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings_heroku") ```

wsgi.py
```
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

# HEROKU
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
```
