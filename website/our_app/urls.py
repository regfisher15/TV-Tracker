from django.urls import path
from django.views.decorators.cache import cache_page
# from django.views.generic import TemplateView

from . import views




urlpatterns = [
    path("home/", cache_page(60*1)(views.home_view), name='home'),
    # path('', views.index, name='index'),
    # path("db-test-endpt/", cache_page(60*1)(views.DatabaseView.as_view()), name='db-test-view'),
    path('update-fav-movies/<slug:pk>/', views.UpdateFavMoviesView.as_view(), name='update_fav_movies'),
    path('update-fav-movies/', views.RedirectByUserID.as_view(), name='update_movies_redirect'),
    #path('update-fav-shows/<slug:pk>/', views.UpdateFavShowsView.as_view(), name='update_fav_shows'),
    #path('update-fav-shows/', views.RedirectByUserID.as_view(), name='update_shows_redirect'),
    path('shows/', views.show_list, name="all_shows"),
    path('any-show/<slug:pk>/', views.ObjectView.as_view(), name='object_view'),
    # path('any-show/', views.RedirectByObjectID.as_view(), name='object_view_redirect'),

    path('ajax_update_fav_shows/<int:show_id>/', views.AjaxUpdateFavShowsView.as_view(), name='ajax_update_fav_shows'),

    path('ajax_update_comp_shows/<int:show_id>/', views.AjaxUpdateCompShowsView.as_view(), name='ajax_update_comp_shows'),

    path('ajax_update_watch_shows/<int:show_id>/', views.AjaxUpdateWatchShowsView.as_view(), name='ajax_update_watch_shows'),

    path("main/", views.main_view, name='main'),
    path("profile/", views.profile_view, name='profile'),
    path("calendar/", views.calendar_view, name='calendar'),
    path("discover/", cache_page(60*1)(views.discover_view), name='discover'),
    #path("discover/<int:genre_id>/<str:genre_name>/", views.discover_view, name='discover'),
    path("settings/", views.settings_view, name='settings'),
    path("group/", views.group_view, name='group'),
    #path("genre/", views.genre_view, name='genre'),
    path('genre/<int:genre_id>/<str:genre_name>/', cache_page(60*2)(views.genre_view), name='genre'),
    path('showprofile/<int:show_id>/', views.showprofile_view, name='showprofile'),
    path("will/", views.will_view, name='will'),
]

# urlpatterns = [
#     path("home/", views.home_view, name='home'),
#     # path('', views.index, name='index'),
#     # path("db-test-endpt/", cache_page(60*1)(views.DatabaseView.as_view()), name='db-test-view'),
#     path('update-fav-movies/<slug:pk>/', views.UpdateFavMoviesView.as_view(), name='update_fav_movies'),
#     path('update-fav-movies/', views.RedirectByUserID.as_view(), name='update_movies_redirect'),
#     #path('update-fav-shows/<slug:pk>/', views.UpdateFavShowsView.as_view(), name='update_fav_shows'),
#     #path('update-fav-shows/', views.RedirectByUserID.as_view(), name='update_shows_redirect'),
#     path('shows/', views.show_list, name="all_shows"),
#     path('any-show/<slug:pk>/', views.ObjectView.as_view(), name='object_view'),
#     # path('any-show/', views.RedirectByObjectID.as_view(), name='object_view_redirect'),

#     path('ajax_update_fav_shows/<int:show_id>/', views.AjaxUpdateFavShowsView.as_view(), name='ajax_update_fav_shows'),
#     path('ajax_update_fav_top/<int:show_id>/', views.AjaxUpdateFavTopView.as_view(), name='ajax_update_fav_top'),

#     path('ajax_update_comp_shows/<int:show_id>/', views.AjaxUpdateCompShowsView.as_view(), name='ajax_update_comp_shows'),
#     path('ajax_update_comp_top/<int:show_id>/', views.AjaxUpdateCompTopView.as_view(), name='ajax_update_comp_top'),

#     path('ajax_update_watch_shows/<int:show_id>/', views.AjaxUpdateWatchShowsView.as_view(), name='ajax_update_watch_shows'),
#     path('ajax_update_watch_top/<int:show_id>/', views.AjaxUpdateWatchTopView.as_view(), name='ajax_update_watch_top'),


#     path("main/", views.main_view, name='main'),
#     path("profile/", views.profile_view, name='profile'),
#     path("calendar/", views.calendar_view, name='calendar'),
#     path("discover/", views.discover_view, name='discover'),
#     path("settings/", views.settings_view, name='settings'),
#     path("group/", views.group_view, name='group'),
#     path("genre/", views.genre_view, name='genre'),
#     path('showprofile/<int:show_id>/', views.showprofile_view, name='showprofile'),
#     path("will/", views.will_view, name='will'),
# ]


# urlpatterns = [
#     # path('', views.index, name='index'),
#     # path("db-test-endpt/", cache_page(60*1)(views.DatabaseView.as_view()), name='db-test-view'),
#     path('update-fav-movies/<slug:pk>/', views.UpdateFavMoviesView.as_view(), name='update_fav_movies'),
#     path('update-fav-movies/', views.RedirectByUserID.as_view(), name='update_movies_redirect'),
#     path('update-fav-shows/<slug:pk>/', views.UpdateFavShowsView.as_view(), name='update_fav_shows'),
#     path('update-fav-shows/', views.RedirectByUserID.as_view(), name='update_shows_redirect'),
#     path('shows/', views.show_list, name="all_shows"),
#     path('any-show/<slug:pk>/', views.ObjectView.as_view(), name='object_view'),
#     # path('any-show/', views.RedirectByObjectID.as_view(), name='object_view_redirect'),

#     path("main/", views.main_view, name='main'),
#     path("profile/", views.profile_view, name='profile'),
#     path("calendar/", views.calendar_view, name='calendar'),
#     path("discover/", views.discover_view, name='discover'),
#     path("settings/", views.settings_view, name='settings'),
#     path("group/", views.group_view, name='group'),
#     path("genre/", views.genre_view, name='genre'),
#     path("showprofile/", views.showprofile_view, name='showprofile'),
#     path("will/", views.will_view, name='will'),
# ]
