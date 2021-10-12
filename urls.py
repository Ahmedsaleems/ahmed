from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create/", views.create, name="createauction"),
    path("<str:name>", views.auction_item, name="auctionitem"),
    path("watchlist/", views.user_watchlist, name="u_watchlist"),
    path("categories/", views.item_categories, name="itemcategories"),
    path("<str:categorynamee>/", views.item_c, name="i_category")
]
