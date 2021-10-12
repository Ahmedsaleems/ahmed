from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def index(request):
    z = []
    y = []
    x = []
    a = auctionlisting.objects.all()
    for i in a:
        k = i.biditemid.all().order_by("bidamount")
        l = k.last()
        if l is None:
            z.append(i)
        y.append(l)
        try:
            win = winner.objects.get(item_id=i)
        except winner.DoesNotExist:
            win = None
        if win is None:
            x.append(i)
    
    return render(request, "auctions/index.html", {
        "auction": x, "y": y, "z": z
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        startingprice = request.POST["startingbid"]
        category = request.POST["category"]
        image = request.POST["image"]
        x = auctionlisting(title=title, description=description, startingbid=startingprice, category=category, image=image)
        x.save()
        a = request.user.username
        b = User.objects.get(username=a)
        creatoritem = listingcreator(item_id=x, user_id=b)
        creatoritem.save()
        if len(category) > 0:
            abc = categories(categoryname=category, items=x)
            abc.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/create.html")

def auction_item(request, name):
    try:
        a = auctionlisting.objects.get(title=name)
    except auctionlisting.DoesNotExist:
        return render(request, "auctions/error2.html")
    x = request.user.username
    if request.user.is_authenticated:
        user = User.objects.get(username=x)
    else:
        user = None
    bid = bids.objects.filter(itemid=a).order_by("bidamount")
    bi = bid.last()
    try:
        creator = listingcreator.objects.get(item_id=a)
    except listingcreator.DoesNotExist:
        creator = None
    try:
        itemwinner = winner.objects.get(item_id=a)
    except winner.DoesNotExist:
        itemwinner = None
    #all the comments querysets from model comments
    try:
        commentsmade = comments.objects.filter(item_id=a)
    except comments.DoesNotExist:
        commentsmade = None
    if request.user.is_authenticated:
        y = watchlist.objects.filter(itemid=a, username=user)
        bid = bids.objects.filter(itemid=a).order_by("bidamount")
        bi = bid.last()
        if request.method == "POST":
            close = request.POST.get("closelisting")
            if close is not None:
                itemwinner = winner(user_id=bi.username, item_id=a)
                itemwinner.save()
                return render(request, "auctions/item.html", {
                    "item": a, "bid": bi, "creator": creator, "user": user, "winner": itemwinner, "comments": commentsmade
                })
        if request.method == "POST":
            comment = request.POST.get("comment")
            if comment is not None:
                z = comments(item_id=a, user_id=user, comment=comment)
                z.save()
                return render(request, "auctions/item.html", {
                    "item": a, "bid": bi, "creator": creator, "user": user, "winner": itemwinner, "comments": commentsmade
                        })
        if y.exists():
            if request.method == "POST":
                bid = bids.objects.filter(itemid=a).order_by("bidamount")
                bi = bid.last()
                xyz = request.POST.get("removewatchlist")
                if xyz is not None:
                    ab = watchlist.objects.filter(itemid=a, username=user)
                    ab.delete()
                    bid = bids.objects.filter(itemid=a).order_by("bidamount")
                    bi = bid.last()
                    return render(request, "auctions/add.html", {
                        "item": a, "bid": bi, "creator": creator, "user": user, "winner": itemwinner, "comments": commentsmade
                    })
                abc = request.POST.get("bid")
                if abc is not None:
                    if not float(abc) > bi.bidamount:
                        return render(request, "auctions/error.html", {
                            "item": a, "creator": creator, "user": user, "winner": itemwinner, "comments": commentsmade
                        })
                    bb = request.user.username
                    bc = User.objects.get(username=bb)
                    bd = bids(itemid=a, username=bc, bidamount=abc)
                    bd.save()
                    bid = bids.objects.filter(itemid=a).order_by("bidamount")
                    bi = bid.last()
                    return render(request, "auctions/remove.html", {
                        "item": a, "bid": bi, "creator": creator, "user": user, "winner": itemwinner, "comments": commentsmade
                    })
            return render(request, "auctions/remove.html", {
                "item": a, "bid": bi, "creator": creator, "user": user, "winner": itemwinner, "comments": commentsmade
            })
        else:
            bid = bids.objects.filter(itemid=a).order_by("bidamount")
            bi = bid.last()
            if request.method == "POST":
                xyz = request.POST.get("addwatchlist")
                if xyz is not None:    
                    ad = watchlist(username=user, itemid=a)
                    ad.save()
                    bid = bids.objects.filter(itemid=a).order_by("bidamount")
                    bi = bid.last()
                    return render(request, "auctions/remove.html", {
                        "item": a, "bid":bi, "creator": creator, "user": user, "winner": itemwinner, "comments": commentsmade
                    })
                abc = request.POST.get("bid")
                if abc is not None:
                    if bi is not None:
                        if not float(abc) > bi.bidamount:
                            return render(request, "auctions/error.html", {
                                "item": a, "creator": creator, "user": user, "winner": itemwinner, "comments": commentsmade
                            })
                    bb = request.user.username
                    bc = User.objects.get(username=bb)
                    bd = bids(itemid=a, username=bc, bidamount=abc)
                    bd.save()
                    bid = bids.objects.filter(itemid=a).order_by("bidamount")
                    bi = bid.last()
                    return render(request, "auctions/add.html", {
                        "item": a, "bid": bi, "creator": creator, "user": user, "winner": itemwinner, "comments": commentsmade
                    })
                close = request.POST.get("closelisting")
            return render(request, "auctions/add.html", {
                "item": a, "bid": bi, "creator": creator, "user": user, "winner": itemwinner, "comments": commentsmade 
            })
    return render(request, "auctions/item.html", {
        "item": a, "bid": bi, "creator": creator, "user": user, "winner": itemwinner, "comments": commentsmade
    })    


def user_watchlist(request):
    y = []
    x = request.user.username
    user = User.objects.get(username=x)
    userwatchlist = watchlist.objects.filter(username=user)
    for i in userwatchlist:
        abc = i.itemid
        xyz = abc.title
        y.append(xyz)
    return render(request, "auctions/watchlist.html", {
        "watchlist": y
    })

def item_categories(request):
    abc = []
    d = []
    categoriess = categories.objects.all()
    for i in categoriess:
        if i.categoryname not in abc:
            d.append(i)
            abc.append(i.categoryname)
    return render(request, "auctions/categories.html", {
        "x": d
    })

def item_c(request, categorynamee):
    c = []
    d = []
    b = []
    lmn = categories.objects.filter(categoryname=categorynamee)
    for i in lmn:
        try:
            xx = winner.objects.get(item_id=i.items)
        except winner.DoesNotExist:
            xx = None
        if xx is not None:
            pass
        else:
            cc = i.items
            b.append(cc)
    for j in b: 
        x = j.biditemid.all().order_by("bidamount")
        y = x.last()
        if y is None:
            c.append(j)
        d.append(y)
    return render(request, "auctions/itemcategory.html", {
        "itemsss": b, "notbid": c, "bid": d
    })
