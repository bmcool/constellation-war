import sys
import os
import djcelery

djcelery.setup_loader()

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# for project's apps
sys.path.append(PROJECT_ROOT)

# for settings.py
sys.path.append(os.path.dirname(PROJECT_ROOT))

# Name of the directory for the project.
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings" % PROJECT_DIRNAME)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
