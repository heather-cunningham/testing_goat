from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(
        request, 
        "pages/homepage.html",
        {"new_item_text": request.POST.get("add_todo_item", "")}
    )

