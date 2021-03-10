from django.shortcuts import render
from django import forms
from encyclopedia import util
from django.http import HttpResponseRedirect
import random
# Create your views here.
class editpage(forms.Form):
    edit = forms.CharField(label="edit", widget=forms.Textarea())

def index(request, editname):
    listentries = util.list_entries()
    x = util.get_entry(editname)
    if request.method == "POST":
        formcontent = editpage(request.POST)
        if formcontent.is_valid():
            y = formcontent.cleaned_data["edit"]
            util.save_entry(editname, y)
            return HttpResponseRedirect(f"http://127.0.0.1:8000/wiki/{editname}")
    z = random.choice(listentries)
    return render(request, "editpage/index.html", {
        "editform": editpage(initial={'edit': x}), "random": z
    })