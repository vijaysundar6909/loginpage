from django.contrib import admin

# Register your models here.


from .models import subject , detail,rank

admin.site.register(subject)
admin.site.register(detail)
admin.site.register(rank)