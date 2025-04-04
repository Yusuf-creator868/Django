from django.shortcuts import render
from .models import Post

# Create your views here.



def home(request):

    context = {
        "posting": Post.objects.all()
    }

    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})







musics = [
    {
        "can": "I can not lie",
        "miss1": "Miss you much"
    },
    {
        "watch": "Watching everyday that goes by",
        "miss2": "Miss you much"
    }
]


def music(request):

    allsongs = {
        "words": musics
    }

    return render(request, "blog/song.html", allsongs)

