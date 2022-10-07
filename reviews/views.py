from django.shortcuts import render, redirect
from .models import Movie, Review
from .forms import MovieForm, ReviewForm

# Create your views here.
def index(request):
    contents = Movie.objects.all()
    context = {
        "contents": contents,
    }
    return render(request, "reviews/index.html", context)


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


# 영화 상세 페이지
def detail(request, movie_pk):
    info = Movie.objects.get(pk=movie_pk)
    review = Review.objects.filter(movie_name=info.title)

    context = {
        "info": info,
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


# 리뷰 작성 페이지
def create(request, movie_pk):
    review_form = ReviewForm(request.POST or None)
    info = Movie.objects.get(pk=movie_pk)
    print(info)
    print(review_form)
    if review_form.is_valid():
        new_review = review_form.save()
        new_review.movie_name = info.title
        new_review.save()
        return redirect("reviews:detail")  # 나중에 댓글 상세보기 페이지로 이동

    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/create.html", context)


# 리뷰 삭제
def delete(request, review_pk):
    Review.objects.get(pk=review_pk).delete()

    return redirect("reviews:detail")
