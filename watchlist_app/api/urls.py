from django.urls import path, include
from watchlist_app.api.views import (watchlistAV, watchdetailsAV, streamplatformAV, streamplatformdetailAV,
                                     reviewlist, reviewdetail, reviewcreate)

urlpatterns = [
    path('list', watchlistAV.as_view(), name = 'watchlist'),
    path('<int:pk>', watchdetailsAV.as_view(), name = 'watchdetails'),
    path('stream', streamplatformAV.as_view(), name = 'streamplatform'),
    path('stream/<int:pk>', streamplatformdetailAV.as_view(), name = 'streamplatformdetail'),

    path('stream/<int:pk>/review', reviewlist.as_view(), name = 'reviewlist'),
    path('stream/<int:pk>/review-create', reviewcreate.as_view(), name = 'reviewcreate'),
    path('stream/review/<int:pk>', reviewdetail.as_view(), name = 'reviewdetail'),
    #path('review', reviewlist.as_view(), name = "reviewlist"),
    #path('review/<int:pk>', reviewdetail.as_view(), name = 'reviewdetails')
]
