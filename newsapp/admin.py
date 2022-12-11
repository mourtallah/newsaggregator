from django.contrib import admin
from .models import NewsClip, Investor, Deal, Company

admin.site.register(NewsClip)
admin.site.register(Investor)
admin.site.register(Deal)
admin.site.register(Company)
