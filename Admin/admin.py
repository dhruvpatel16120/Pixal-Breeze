from django.contrib import admin
from Admin.models import Contact,Team,Social_Links,Service,Feature,Card ,Portfolio
# Register your models here.

class contact(admin.ModelAdmin):
    list_display = ('name','email','phone','subject','desc')

class social(admin.ModelAdmin):
    list_display = ('title','link','icon','date')

class service(admin.ModelAdmin):
    list_display = ('title','desc','icon','date')

class feature(admin.ModelAdmin):
    list_display = ('title','desc','img','date')

class team(admin.ModelAdmin):
    list_display = ('name','post','desc','img','twitter','facebook','instagram','linkedin')

class card(admin.ModelAdmin):
    list_display = ('title','desc','img')

class portfolio(admin.ModelAdmin):
    list_display = ('title','img','cat')


admin.site.register(Portfolio,portfolio)
admin.site.register(Contact, contact)
admin.site.register(Team,team)
admin.site.register(Social_Links, social)
admin.site.register(Service,service)
admin.site.register(Feature, feature)
admin.site.register(Card,card)

