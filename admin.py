from django.contrib import admin
from .models import *
# Register your models here.

class auctionlistingadmin(admin.ModelAdmin):
    pass

admin.site.register(User)
admin.site.register(auctionlisting, auctionlistingadmin)
admin.site.register(watchlist)
admin.site.register(bids)
admin.site.register(listingcreator)
admin.site.register(winner)
admin.site.register(comments)
admin.site.register(categories)