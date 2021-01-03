from django.contrib import admin

from .models import Language
from .models import Snippet

admin.site.register(Language)
admin.site.register(Snippet)