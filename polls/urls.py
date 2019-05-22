from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import polls_detail, polls_list
from .apiviews import (
    PollDetail,
    PollList,
    ChoiceList,
    CreateVote,
    PollViewSet,
)


router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')


urlpatterns = [
    # path("polls/", polls_list, name="polls_list"),
    # path("polls/<int:pk>/", polls_detail, name="polls_detail"),
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    # path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="polls_list"),
]

urlpatterns += router.urls
