from django.shortcuts import render, redirect
from .models import Movie, Review
from .forms import MovieForm, ReviewForm

# Create your views here.
def index(request):
    return render(request, "reviews/index.html")


def detail(request, pk):
    info = Movie.objects.get(pk=pk)
    review = Review.objects.get(movie_name=info.title)
    context = {
        "info": info,
        "review": review,
    }
    return render(request, "movies/detail.html", context)


def movie_register(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("reviews:index")
    else:
        movie_form = MovieForm()
    context = {
        "movie_form": movie_form,
    }
    return render(request, "reviews/register.html", context)
