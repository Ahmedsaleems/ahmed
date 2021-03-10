from django.shortcuts import render
from encyclopedia import util
import markdown
from encyclopedia import views
from django.http import HttpResponseRedirect
import random
# Create your views here.


def index(request, name):
    x = []
    listentries = util.list_entries()
    if request.method == "POST":
        searchcont = views.searchform(request.POST)
        if searchcont.is_valid():
            searchcontent = searchcont.cleaned_data["search"]
            if searchcontent in listentries:
                return HttpResponseRedirect(f"http://127.0.0.1:8000/wiki/{searchcontent}")
            for i in listentries:
                if searchcontent in i:
                    x.append(i)
            if not searchcontent in listentries and len(x) == 0:
                return render(request, "encyclopedia/error.html")
            return render(request, "encyclopedia/xyz.html", {
                "reflist": x
            })
    x.clear()
    if not name in listentries:
        return render(request, "entrypage/error.html")
    md = markdown.Markdown()
    content = md.convert(util.get_entry(name))
    z = random.choice(listentries)
    return render(request, "entrypage/index.html", {
        "contents": content, "name": name, "form": views.searchform(), "random": z
    })
        