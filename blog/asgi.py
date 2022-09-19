"""
Refer site:
https://channels.readthedocs.io/en/latest/introduction.html
"""

import os
import django
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

django.setup()

application = get_default_application()