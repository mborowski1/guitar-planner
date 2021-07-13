"""GuitarPlanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Guitar_Planner.views import AddExercise, AddBand, AddMonth, AddSong, Menu, Start, AddLoginPassword, AddBacklog, Backlog, ModifyBacklog, DeleteBacklog, Exercise, DeleteExercise, Song, DeleteSong, Band, DeleteBand, Month, DeleteMonth, ModifyMonth, ModifyExercise, TitleScreen, Logout, ExercisesDisplay, SongsDisplay, BandsDisplay, MonthsDisplay, BacklogDisplay, NotLogged

app_name = "Guitar_Planner"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/exercises/add_exercise/', AddExercise.as_view(), name="add_exercise"),
    path('menu/bands/add_band/', AddBand.as_view(), name="add_band"),
    path('menu/months/add_month/', AddMonth.as_view(), name="add_month"),
    path('menu/songs/and_song/', AddSong.as_view(), name="add_song"),
    path('menu/', Menu.as_view(), name="menu"),
    path('login/', Start.as_view(), name="start"),
    path('login/addloginpassword/', AddLoginPassword.as_view(), name="addloginpassword"),
    path('menu/backlog_menu/', Backlog.as_view(), name="backlog"),
    path('menu/backlog_menu/add_backlog/', AddBacklog.as_view(), name="addbacklog"),
    path('menu/backlog_menu/modify_backlogs/', ModifyBacklog.as_view(), name="modifybacklog"),
    path('menu/backlog_menu/delete_backlogs/', DeleteBacklog.as_view(), name="deletebacklog"),
    path('menu/exercises/', Exercise.as_view(), name="exercisemenu"),
    path('menu/exercises/delete_exercise/', DeleteExercise.as_view(), name="deleteexercise"),
    path('menu/songs/', Song.as_view(), name="songs"),
    path('menu/songs/delete_song/', DeleteSong.as_view(), name="deletesong"),
    path('menu/bands/', Band.as_view(), name="band"),
    path('menu/bands/delete_band/', DeleteBand.as_view(), name="deleteband"),
    path('menu/months/', Month.as_view(), name="month"),
    path('menu/months/delete_month/', DeleteMonth.as_view(), name="deletemonth"),
    path('menu/months/modify_months/', ModifyMonth.as_view(), name="modifymonth"),
    path('menu/exercises/modify_exercise/', ModifyExercise.as_view(), name="modifyexercise"),
    path('', TitleScreen.as_view(), name="titlescreen"),
    path('logout/', Logout.as_view(), name="logout"),
    path('menu/exercises/display_exercises/', ExercisesDisplay.as_view(), name="exercisesdisplay"),
    path('menu/songs/display_songs/', SongsDisplay.as_view(), name="songsdisplay"),
    path('menu/bands/display_bands/', BandsDisplay.as_view(), name="bandsdisplay"),
    path('menu/months/display_months/', MonthsDisplay.as_view(), name="monthdisplay"),
    path('menu/backlog_menu/show_backlogs/', BacklogDisplay.as_view(), name="backlogdisplay"),
    path('not_logged/', NotLogged.as_view(), name="not_logged")
]
