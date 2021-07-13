from django.shortcuts import render
from django.views.generic import View
from .forms import AddExerciseForm, AddBandForm, AddMonthForm, AddSongForm, LoginPasswordForm, NewLoginPasswordForm, BacklogForm, ModifyBacklogForm, DeleteBacklogForm, DeleteExerciseForm, DeleteSongForm, DeleteBandForm, DeleteMonthForm, DeleteMonthForm, ModifyMonthForm, ModifyExerciseForm
from .models import Month, Band, Song, Back_log
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .models import Exercise as ExerciseModel
from .models import Song as SongModel
from .models import Band as BandModel
from .models import Month as MonthModel
from .models import Back_log as Back_logModel
from django.contrib.auth.mixins import LoginRequiredMixin




User = get_user_model()

class AddExercise(View):

    # View making it possible to create an 'Exercise' object.

    template_name = 'templates/exercises_template.html'
    form_class = AddExerciseForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            speed = form.cleaned_data['speed']





            exercise = ExerciseModel.objects.create(name=name, description=description, speed=speed, user=request.user)
            #exercise.month.add(month_thing)
            exercise.save()


        message = 'Dodano ćwiczenie.'

        context = {
            'form': form,
            'message': message
        }

        return render(request, self.template_name, context)

class AddBand(View):

    # View making it possible to create a 'Band' object.

    template_name = 'templates/band_template.html'
    form_class = AddBandForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            year_of_creation = form.cleaned_data['year_of_creation']


            BandModel.objects.create(name=name, year_of_creation=year_of_creation, user=request.user)

        message = 'Dodano wykonawcę.'

        context = {
            'form': form,
            'message': message
        }

        return render(request, self.template_name, context)

class AddMonth(View):

    # View making it possible to create a 'Month' object.

    template_name = 'templates/month_template.html'
    form_class = AddMonthForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']


            MonthModel.objects.create(name=name, year=year, user=request.user)

        message = 'Dodano miesiąc.'

        context = {
            'form': form,
            'message': message
        }

        return render(request, self.template_name, context)

class AddSong(View):

    # View making it possible to create a 'Song' object.

    template_name = 'templates/song_template.html'
    form_class = AddSongForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            genre = form.cleaned_data['genre']
            band = form.cleaned_data['band']

            band_thing = BandModel.objects.filter(name=band, user=request.user).first()

        try:

            SongModel.objects.create(name=name, genre=genre, band=band_thing, user=request.user)


        except:

            message = 'Na Twojej liście nie ma takiego zespołu.'

            context = {
                'form': form,
                'message': message
            }

            return render(request, self.template_name, context)





        message = 'Dodano utwór.'

        context = {
        'form': form,
        'message': message
        }

        return render(request, self.template_name, context)



class Menu(LoginRequiredMixin, View):

    # View displaying menu.

    login_url = '/login/'
    template_name = 'templates/menu_template.html'



    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

class Start(View):

    # View making it possible to log in.

    model = User
    template_name = 'templates/start_template.html'
    form_class = LoginPasswordForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)


            if user is not None:
                login(request, user)

                template_name_2 = 'templates/successful_login_template.html'

                message = 'Udało Ci się podać pasujące do siebie hasło i login. Zostałeś zalogowany.'

                context = {

                    'message': message
                }

                return render(request, template_name_2, context)





            else:

                message = 'Nie udało Ci się podać pasujących do siebie hasła i loginu.'

                context = {
                    'form': form,
                    'message': message
                }

                return render(request, self.template_name, context)

class AddLoginPassword(FormView):

    # View making it possible to create a user.

    model = User
    template_name = 'templates/new_login_password_template.html'
    form_class = NewLoginPasswordForm

    def post(self, request):
        form = self.form_class(request.POST)

        login = request.POST.get("login")
        password = request.POST.get("password")
        repeated_password = request.POST.get("repeated_password")
        email = request.POST.get("email")

        if User.objects.filter(username=login).exists():
            error = 'Taki użytkownik już istnieje.'

            context = {
                'message': error
            }

            return render(request, 'templates/new_login_password_template.html', context)

        if repeated_password != password:

            error = 'Hasła nie są takie same.'

            context = {
                'message': error
            }

            return render(request, 'templates/new_login_password_template.html', context)


        new_user=User.objects.create_user(username=login, email=email, password=password)
        new_user.save()

        message = 'Utworzono nowego użytkownika.'

        context = {
            'message': message
        }

        return render(request, "templates/user_created_template.html", context)

class AddBacklog(View):

    # View making it possible to create a 'Backlog' object.

    template_name = 'templates/add_backlog_template.html'
    form_class = BacklogForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            value = form.cleaned_data['value']


            Back_log.objects.create(name=name, description=description, value=value, user=request.user)


        message = 'Dodano zaległość.'

        context = {
            'form': form,
            'message': message
        }

        return render(request, self.template_name, context)

class Backlog(View):

    # View displaying menu enabling 'Backlog' objects management.

    template_name = 'templates/backlog_template.html'


    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

class ModifyBacklog(View):

    # View making it possible to modify a 'Backlog' object.

    template_name = 'templates/modify_backlog_template.html'
    form_class = ModifyBacklogForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            new_value = form.cleaned_data['value']

            backlog_thing = Back_log.objects.filter(name=name, user=request.user).first()

            if len(name) > 0 and not backlog_thing:
                message = 'Taka zaległość nie znajduje się na Twojej liście.'

                context = {
                    'form': form,
                    'message': message
                }

                return render(request, self.template_name, context)

            backlog_thing.value = new_value
            backlog_thing.save()





            message = 'Zmodyfikowano zaległość.'

            context = {
                'form': form,
                'message': message
            }

            return render(request, self.template_name, context)

class DeleteBacklog(View):

    # View making it possible to delete a 'Backlog' object.

    template_name = 'templates/delete_backlog_template.html'
    form_class = DeleteBacklogForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']


            backlog_thing = Back_log.objects.filter(name=name, user=request.user).first()

            if len(name) > 0 and not backlog_thing:
                message = 'Taka zaległość nie znajduje się na Twojej liście.'

                context = {
                    'form': form,
                    'message': message
                }

                return render(request, self.template_name, context)

            backlog_thing.delete()






        message = 'Usunięto zaległość.'

        context = {
            'form': form,
            'message': message
        }

        return render(request, self.template_name, context)

class Exercise(View):

    # View displaying menu enabling 'Exercise' objects management.

    template_name = 'templates/exercises_menu_template.html'



    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

class DeleteExercise(View):

    # View making it possible to delete an 'Exercise' object.

    template_name = 'templates/delete_exercise_template.html'
    form_class = DeleteExerciseForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']

            exercises_thing = ExerciseModel.objects.filter(name=name, user=request.user).first()

            if len(name) > 0 and not exercises_thing:
                message = 'Takie ćwiczenie nie znajduje się na Twojej liście.'

                context = {
                    'form': form,
                    'message': message
                }

                return render(request, self.template_name, context)

            exercises_thing.delete()






        message = 'Usunięto ćwiczenie.'

        context = {
            'form': form,
            'message': message
        }

        return render(request, self.template_name, context)

class Song(View):

    # View enabling 'Songs' objects management.

    template_name = 'templates/songs_menu.html'


    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)









class DeleteSong(View):

    # View making it possible to delete a 'Song' object.

    template_name = 'templates/delete_song_template.html'
    form_class = DeleteSongForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']




            song_thing = SongModel.objects.filter(name=name, user=request.user).first()

            if len(name) > 0 and not song_thing:
                message = 'Taki utwór nie znajduje się na Twojej liście.'

                context = {
                    'form': form,
                    'message': message
                }

                return render(request, self.template_name, context)

            song_thing.delete()






        message = 'Usunięto utwór.'

        context = {
            'form': form,
            'message': message
        }

        return render(request, self.template_name, context)

class DeleteBand(View):

    # View making it possible to delete a 'Band' object.

    template_name = 'templates/delete_band_template.html'
    form_class = DeleteBandForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']


            band_thing = BandModel.objects.filter(name=name, user=request.user).first()

            if len(name) > 0 and not band_thing:
                message = 'Taki zespół nie znajduje się na Twojej liście.'

                context = {
                    'form': form,
                    'message': message
                }

                return render(request, self.template_name, context)

            band_thing.delete()






        message = 'Usunięto zespół.'

        context = {
            'form': form,
            'message': message
        }

        return render(request, self.template_name, context)

class Band(View):

    # View displaying menu enabling 'Band' objects management.

    template_name = 'templates/bands_template.html'


    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

class DeleteMonth(View):

    # View making it possible to delete a 'Month' object.

    template_name = 'templates/delete_month_template.html'
    form_class = DeleteMonthForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']


            month_thing = MonthModel.objects.filter(name=name, year=year, user=request.user).first()

            if len(name) > 0 and not month_thing:
                message = 'Taki miesiąc nie znajduje się na Twojej liście.'

                context = {
                    'form': form,
                    'message': message
                }

                return render(request, self.template_name, context)

            month_thing.delete()






        message = 'Usunięto miesiąc.'

        context = {
            'form': form,
            'message': message
        }

        return render(request, self.template_name, context)

class Month(View):

    # View enabling 'Month' objects management.

    template_name = 'templates/month_menu_template.html'


    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

class ModifyMonth(View):

    # View enabling 'Month' objects modification.


    template_name = 'templates/modify_month_template.html'
    form_class = ModifyMonthForm



    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']
            new_exercise = form.cleaned_data['exercise']
            new_song = form.cleaned_data['song']
            month_thing = MonthModel.objects.filter(name=name, year=year, user=request.user).first()



            new_exercise_thing = ExerciseModel.objects.filter(name=new_exercise, user=request.user).first()

            if len(new_exercise) > 0 and not new_exercise_thing:


                message = 'Takie ćwiczenie nie znajduje się na liście.'

                context = {
                    'form': form,
                    'message': message
                }

                return render(request, self.template_name, context)


            if not new_exercise_thing:



                new_song_thing = SongModel.objects.filter(name=new_song, user=request.user).first()

                if len(new_song) > 0 and not new_song_thing:
                    message = 'Taki utwór nie znajduje się na liście.'

                    context = {
                        'form': form,
                        'message': message
                    }

                    return render(request, self.template_name, context)

                month_thing.song.add(new_song_thing)
                month_thing.save()

                message = 'Zmodyfikowano miesiąc.'

                context = {
                    'form': form,
                    'message': message
                }

                return render(request, self.template_name, context)







            new_song_thing = SongModel.objects.filter(name=new_song, user=request.user).first()

            if len(new_song) > 0 and not new_song_thing:


                message = 'Taki utwór nie znajduje się na liście.'

                context = {
                    'form': form,
                    'message': message
                }

                return render(request, self.template_name, context)

            if not new_song_thing:



                new_exercise_thing = ExerciseModel.objects.filter(name=new_exercise, user=request.user).first()

                if len(new_exercise) > 0 and not new_exercise_thing:
                    message = 'Takie ćwiczenie nie znajduje się na liście.'

                    context = {
                        'form': form,
                        'message': message
                    }

                    return render(request, self.template_name, context)

                month_thing.exercise.add(new_exercise_thing)
                month_thing.save()

                message = 'Zmodyfikowano miesiąc.'

                context = {
                    'form': form,
                    'message': message
                }

                return render(request, self.template_name, context)



            month_thing.song.add(new_song_thing)
            month_thing.exercise.add(new_exercise_thing)
            month_thing.save()







            message = 'Zmodyfikowano miesiąc.'

            context = {
                'form': form,
                'message': message
            }

            return render(request, self.template_name, context)

class ModifyExercise(View):

    # View enabling 'Exercises' objects modification.

    template_name = 'templates/modify_exercise_template.html'
    form_class = ModifyExerciseForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            new_speed = form.cleaned_data['speed']



            exercise_thing = ExerciseModel.objects.filter(name=name, user=request.user).first()

            if len(name) > 0 and not exercise_thing:

                message = 'Takie ćwiczenie nie znajduje się na Twojej liście.'

                context = {
                    'form': form,
                    'message': message
                }

                return render(request, self.template_name, context)

            exercise_thing.speed = new_speed
            exercise_thing.save()





            message = 'Zmodyfikowano ćwiczenie.'

            context = {
                'form': form,
                'message': message
            }

            return render(request, self.template_name, context)

class TitleScreen(View):

    # View displaying the title screen.

    template_name = 'templates/title_template.html'



    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

class Logout(LoginRequiredMixin, View):

    # View making it possible to log out.

    login_url = '/not_logged/'
    template_name = 'templates/logout_template.html'






    def get(self, request, *args, **kwargs):



        message = 'Nastąpiło wylogowanie.'

        context = {

            'message': message
        }

        logout(request)

        return render(request, self.template_name, context)

class ExercisesDisplay(View):

    # View displaying the list of 'Exercise' objects of a particular user.

    template_name = 'templates/exercises_display_template.html'



    def get(self, request, *args, **kwargs):

        exercises = ExerciseModel.objects.filter(user=request.user)


        context = {
            'exercises': exercises
        }

        return render(request, self.template_name, context)

class SongsDisplay(View):

    # View displaying the list of 'Song' objects of a particular user.

    template_name = 'templates/songs_display_template.html'



    def get(self, request, *args, **kwargs):

        songs = SongModel.objects.filter(user=request.user)


        context = {
            'songs': songs
        }

        return render(request, self.template_name, context)

class BandsDisplay(View):

    # View displaying the list of 'Band' objects of a particular user.

    template_name = 'templates/bands_display_template.html'



    def get(self, request, *args, **kwargs):


        bands = BandModel.objects.filter(user=request.user)


        context = {
            'bands': bands
        }

        return render(request, self.template_name, context)


class MonthsDisplay(View):

    # View displaying the list of 'Month' objects of a particular user.

    template_name = 'templates/months_display_template.html'



    def get(self, request, *args, **kwargs):


        months = MonthModel.objects.filter(user=request.user)
        exercises = ExerciseModel.objects.all()
        songs = SongModel.objects.all()
        user = User.objects.all()



        context = {
            'months': months,
            'exercises': exercises,
            'songs': songs,
            'user': user
        }

        return render(request, self.template_name, context)


class BacklogDisplay(View):

    # View displaying the list of 'Backlog' objects of a particular user.

    template_name = 'templates/backlog_display_template.html'



    def get(self, request, *args, **kwargs):


        back_logs = Back_logModel.objects.filter(user=request.user)


        context = {
            'back_logs': back_logs
        }

        return render(request, self.template_name, context)

class NotLogged(View):

    # View informing that a successful logging in process did not take place before a log out attempt.

    template_name = 'templates/logout_template.html'






    def get(self, request, *args, **kwargs):



        message = 'Nie byłeś zalogowany w momencie kliknięcia.'

        context = {

            'message': message
        }



        return render(request, self.template_name, context)