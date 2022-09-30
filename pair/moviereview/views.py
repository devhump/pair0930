from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Review

# Create your views here.
def index(request):

    reviews = Review.objects.all()

    context = {"reviews": reviews}

    return render(request, "moviereview/index.html", context)


def new(request):

    return render(request, "moviereview/new.html")


def create(request):

    title = request.GET.get("title_")
    content = request.GET.get("content_")

    Review.objects.create(title=title, content=content)

    return redirect("index")
