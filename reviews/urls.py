from django.urls import path
from . import views

app_name = "reviews"
urlpatterns = [
    path("", views.index, name="index"),
    path("movie_register/", views.movie_register, name="movie_register"),   # 관리자 영화 등록
    # path("<int:pk>", views.detail, name="detail"),  # 영화 상세 페이지
    path("detail/", views.detail, name="detail"),  # 영화 상세 페이지
    # path("<int:pk>/create/", views.create, name="create"),   # 영화 상세 페이지 속 리뷰 작성 페이지
    path("create/", views.create, name="create"),   # 영화 상세 페이지 속 리뷰 작성 페이지
    # path("")
]