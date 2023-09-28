from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util
import random


def convert_md(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
    
def entry(request, title):
    html_content = convert_md(title)
    if html_content is not None:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content,
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page does not exist..."
        })
        

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        entries = util.list_entries()
        results = []

        for entry in entries:
            if entry_search.lower() in entry.lower():
                results.append(entry)

        if not results:
            return redirect('entry', title=entry_search) 


        return render(request, "encyclopedia/results.html", {
            "results": results
        })
    else:
        return render(request, "encyclopedia/search_form.html")

            
            
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist != None:
            return render(request, "encyclopedia/error.html", {
                "message": "Page already exists!"
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content,
            })
        

def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content,
        })


def save_page(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content,
        })


def random_page(request):
    all_entries = util.list_entries()
    random_entry = random.choice(all_entries)
    html_content = convert_md(random_entry)
    return render(request, "encyclopedia/entry.html", {
        "title": random_entry,
        "content": html_content,
    })