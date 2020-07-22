from django.contrib import admin

from . import models

# Register your models here.
# admin.site.register(x for x in models)
# admin.site.register(for x in models.models)
# [x for x in models])

# for model in apps.get_models():# (get_app('subordinates')):
#    admin.site.register(model)

# admin.site.register(x for x in models)
admin.site.register([models.Main, models.Subordinate, models.Role])
# admin.site.register(models.Role)
# admin.site.register(models.Subordinate)
