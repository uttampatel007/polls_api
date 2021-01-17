from django.urls import path
# from .views import polls_list, polls_detail

# urlpatterns = [
#     path("polls/", polls_list, name="polls_list"),
#     path("polls/<int:pk>/", polls_detail, name="polls_detail")
# ]
from .apiviews import PollViewSet, ChoiceList, CreateVote, UserCreate
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    # path("polls/", PollList.as_view(), name="polls_list"),
    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<pk>/choices/<choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    # path("login/", LoginView.as_view(), name="login"),
    path("login/", views.obtain_auth_token, name="login"),
]
urlpatterns += router.urls