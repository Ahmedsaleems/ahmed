from django.shortcuts import render
from django import forms
from . import util
from django.http import HttpResponseRedirect
import random

class searchform(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia', 'size': 15}))


def index(request): 
    x = []
    entries = util.list_entries()
    if request.method == "POST":
        searchcont = searchform(request.POST)
        if searchcont.is_valid():
            searchcontent = searchcont.cleaned_data["search"]
            if searchcontent in entries:
                return HttpResponseRedirect(f"http://127.0.0.1:8000/wiki/{searchcontent}")
            for i in entries:
                if searchcontent in i:
                    x.append(i)
            if not searchcontent in entries and len(x) == 0:
                return render(request, "encyclopedia/error.html")
            return render(request, "encyclopedia/xyz.html", {
                "reflist": x 
            })
    x.clear()
    z = random.choice(entries)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), "form": searchform(), "random": z
    })
