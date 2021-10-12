from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class auctionlisting(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)
    startingbid = models.FloatField()
    category = models.CharField(max_length=64, blank=True)
    image = models.URLField(max_length=100000, blank=True)
    def __str__(self):
        return f"{self.title}"

class listingcreator(models.Model):
    item_id = models.ForeignKey(auctionlisting, on_delete=models.CASCADE, related_name="listingid")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    def __str__(self):
        return f"{self.item_id}, {self.user_id}"

class winner(models.Model):
    item_id = models.ForeignKey(auctionlisting, on_delete=models.CASCADE, related_name="winningitem")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winninguser")
    def __str__(self):
        return f"{self.item_id}, {self.user_id}"
    
class watchlist(models.Model):
    itemid = models.ForeignKey(auctionlisting, on_delete=models.CASCADE, related_name="watchlistitem")
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlistuser")
    def __str__(self):
        return f"{self.username}, {self.itemid}"

class bids(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="biduser")
    itemid = models.ForeignKey(auctionlisting, on_delete=models.CASCADE, related_name="biditemid")
    bidamount = models.FloatField()
    def __str__(self):
        return f"{self.itemid} , {self.username}"

class comments(models.Model):
    item_id = models.ForeignKey(auctionlisting, on_delete=models.CASCADE, related_name="commenteditem")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentinguser")
    comment = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.item_id}, {self.user_id}" 


class categories(models.Model):
    categoryname = models.CharField(max_length=64)
    items = models.ForeignKey(auctionlisting, on_delete=models.CASCADE, related_name="categoryitems")
    def __str__(self):
        return f"{self.items}, {self.categoryname}"