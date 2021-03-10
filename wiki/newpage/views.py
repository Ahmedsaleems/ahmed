from django.shortcuts import render
from encyclopedia import util
import markdown
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
# Create your views here.
class newentry(forms.Form):
    title = forms.CharField(label="Title")
    contents = forms.CharField(label="Contents", widget=forms.Textarea(attrs={"rows":5, "cols":5}))

def index(request):
    entries = util.list_entries()
    if request.method == "POST":
        formcontents = newentry(request.POST)
        if formcontents.is_valid():
            formtitle = formcontents.cleaned_data["title"]
            formcontent = formcontents.cleaned_data["contents"]
            if formtitle in entries:
                return render(request, "newpage/error.html")
            util.save_entry(formtitle, formcontent)
            return HttpResponseRedirect(f"http://127.0.0.1:8000/wiki/"+formtitle)
    z = random.choice(entries)
    return render(request, "newpage/index.html", {
        "formm": newentry(), "random": z
    })