import sys, os

app_root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(app_root, 'virtualenv.bundle'))

import sae
from mysite import wsgi
application = sae.create_wsgi_app(wsgi.application)
