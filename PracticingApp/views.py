from django.shortcuts import render



hello = [
    {
        "hello": "Hello",
        "world": "World",
    }
]


def HelloWorld(request):

    Myhello = {
        "myhello": hello
    }

    return render(request, "./testingsall/Test.html", Myhello)

# Create your views here.

