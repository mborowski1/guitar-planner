from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Band, Exercise, Month, Song, Back_log
import pytest
from .views import AddBand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your tests here.

User = get_user_model()

@pytest.mark.django_db
def test_band_add(client):

    # Tests whether it is possible to create a 'Band' object.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)


    response = client.post(reverse('add_band'), {
            'name': 'Iron Maiden',
            'year_of_creation': 1975,
    })



    band = Band.objects.filter(name='Iron Maiden')
    assert (len(band)==1)


@pytest.mark.django_db
def test_band_add_fail(client):

    # Tests whether is is possible to create a band object without 'year_of_creation' attribute.


    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)


    response = client.post(reverse('add_band'), {
            'name': 'Judas Priest',

    })



    band = Band.objects.filter(name='Judas Priest')
    assert (len(band)==0)



@pytest.mark.django_db
def test_exercise_add(client):

    # Tests whether it is possible to create an 'Exercise' object.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)


    response = client.post(reverse('add_exercise'), {
            'name': 'Chromatyka',
            'description': 'Cztery pierwsze dźwięki na szóstej strunie, potem to samo na piątej itd.',
            'speed': 118
    })

    exercise = Exercise.objects.filter(name='Chromatyka')
    assert (len(exercise)==1)

@pytest.mark.django_db
def test_exercise_add_fail(client):

    # Tests whether is is possible to create a 'Band' object without 'description' and 'speed' attributes.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)


    response = client.post(reverse('add_exercise'), {
            'name': 'Dwie struny',

    })

    exercise = Exercise.objects.filter(name='Dwie struny')
    assert (len(exercise)==0)

@pytest.mark.django_db
def test_month_add(client):

    # Tests whether it is possible to create a 'Month' object.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)


    response = client.post(reverse('add_month'), {
            'name': 'Maj',
            'year': 2021

    })

    month = Month.objects.filter(name='Maj')
    assert (len(month)==1)

@pytest.mark.django_db
def test_month_add_fail(client):

    # Tests whether it is possible to create a 'Month' object without 'year' attribute.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)


    response = client.post(reverse('add_month'), {
            'name': 'Kwiecień'


    })

    month = Month.objects.filter(name='Maj')
    assert (len(month)==0)

@pytest.mark.django_db
def test_song_add(client):

    # Tests whether it is possible to create a 'Song' object.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_band'), {
        'name': 'Metallica',
        'year_of_creation': 1981,
    })

    response = client.post(reverse('add_song'), {
            'name': 'Master of Puppets',
            'genre': 'Thrash Metal',
            'band': 'Metallica'

    })

    song = Song.objects.filter(name='Master of Puppets')
    assert (len(song)==1)

@pytest.mark.django_db
def test_song_add_fail(client):

    # Tests whether it is possible to create a 'Song' object without 'name' attribute.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_band'), {
        'name': 'Metallica',
        'year_of_creation': 1981,
    })

    response = client.post(reverse('add_song'), {

            'band': 'Metallica'

    })

    song = Song.objects.filter(name='Enter Sandman')
    assert (len(song)==0)



@pytest.mark.django_db
def test_back_log_add(client):

    # Tests whether it is possible to create a 'Backlog' object.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('addbacklog'), {
            'name': 'Zaległość 100',
            'description': 'Jeżeli nie grałem 100 minut w ciągu dnia, odejmuję ilość minut gry of 100 i dopisuję do zaległości.',
            'value': 0

    })

    back_log = Back_log.objects.filter(name='Zaległość 100')
    assert (len(back_log)==1)

@pytest.mark.django_db
def test_back_log_add_fail(client):

    # Tests whether it is possible to create a 'Backlog' object without 'description' attribute.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('addbacklog'), {
            'name': 'Zaległość 50',
            'value': 0

    })

    back_log = Back_log.objects.filter(name='Zaległość 50')
    assert (len(back_log)==0)

@pytest.mark.django_db
def test_exercise_delete(client):

    # Tests whether it is possible to delete an 'Exercise' object.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_exercise'), {
        'name': 'Przeskakiwanie między strunami',
        'description': 'Jeden dźwięk na szóstej strunie, potem jeden na piątej itd.',
        'speed': 101
    })

    response = client.post(reverse('deleteexercise'), {
            'name': 'Przeskakiwanie między strunami'


    })

    exercise = Exercise.objects.filter(name='Przeskakiwanie między strunami')
    assert (len(exercise)==0)

@pytest.mark.django_db
def test_exercise_delete_second_one(client):

    # Tests whether it is possible to delete one of two 'Exercise' objects.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_exercise'), {
        'name': 'Skipping',
        'description': 'Jeden dźwięk na szóstej strunie, potem jeden na czwartej, potem próg dalej to samo itd.',
        'speed': 101
    })

    response = client.post(reverse('add_exercise'), {
        'name': 'Szybkie granie na pojedynczej strunie',
        'description': 'Jeden dźwięk na szóstej strunie, szybko.',
        'speed': 135
    })

    response = client.post(reverse('deleteexercise'), {
            'name': 'Szybkie granie na pojedynczej strunie'


    })

    exercise = Exercise.objects.filter(name='Skipping')
    assert (len(exercise)==1)

@pytest.mark.django_db
def test_backlog_delete(client):

    # Tests whether it is possible to delete a 'Backlog' object.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('addbacklog'), {
        'name': 'Zaległość 200',
        'description': 'Jeżeli nie grałem 200 minut w ciągu dnia, odejmuję ilość minut gry of 200 i dopisuję do zaległości.',
        'value' : 0
    })

    response = client.post(reverse('deletebacklog'), {
            'name': 'Zaległość 200'


    })

    back_log = Back_log.objects.filter(name='Zaległość 200')
    assert (len(back_log)==0)

@pytest.mark.django_db
def test_backlog_delete_second_one(client):

    # Tests whether it is possible to delete one of two 'Backlog' objects.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('addbacklog'), {
        'name': 'Zaległość 400',
        'description': 'Jeżeli nie grałem 400 minut w ciągu dnia, odejmuję ilość minut gry of 400 i dopisuję do zaległości.',
        'value': 0
    })

    response = client.post(reverse('addbacklog'), {
        'name': 'Zaległość 500',
        'description': 'Jeżeli nie grałem 500 minut w ciągu dnia, odejmuję ilość minut gry of 500 i dopisuję do zaległości.',
        'value': 0
    })

    response = client.post(reverse('deletebacklog'), {
            'name': 'Zaległość 400'


    })

    back_log = Back_log.objects.filter(name='Zaległość 500')
    assert (len(back_log)==1)

@pytest.mark.django_db
def test_song_delete(client):

    # Tests whether it is possible to delete a 'Song' object.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_band'), {
        'name': 'Black Label Society',
        'year_of_creation': 1998

    })

    response = client.post(reverse('add_song'), {
        'name': 'Stoned and Drunk',
        'genre': 'Heavy Metal',
        'band' : 'Black Label Society'
    })

    response = client.post(reverse('deletesong'), {
            'name': 'Stoned and Drunk'


    })

    song = Song.objects.filter(name='Stoned and Drunk')
    assert (len(song)==0)

@pytest.mark.django_db
def test_song_delete_second_one(client):

    # Tests whether it is possible to delete one of two 'Song' objects.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_band'), {
        'name': 'Black Label Society',
        'year_of_creation': 1998

    })

    response = client.post(reverse('add_song'), {
        'name': 'Stoned and Drunk',
        'genre': 'Heavy Metal',
        'band' : 'Black Label Society'
    })

    response = client.post(reverse('add_song'), {
        'name': 'In this River',
        'genre': 'Heavy Metal',
        'band': 'Black Label Society'
    })

    response = client.post(reverse('deletesong'), {
            'name': 'Stoned and Drunk'


    })

    song = Song.objects.filter(name='In this River')
    assert (len(song)==1)

@pytest.mark.django_db
def test_band_delete(client):

    # Tests whether it is possible to delete a 'Band' object.


    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_band'), {
        'name': 'Slayer',
        'year_of_creation': 1981

    })




    response = client.post(reverse('deleteband'), {
            'name': 'Slayer'


    })

    band = Band.objects.filter(name='Slayer')
    assert (len(band)==0)

@pytest.mark.django_db
def test_band_delete_second_one(client):

    # Tests whether it is possible to delete one of two 'Band' objects.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_band'), {
        'name': 'Slayer',
        'year_of_creation': 1981

    })

    response = client.post(reverse('add_band'), {
        'name': 'Sepultura',
        'year_of_creation': 1984

    })


    response = client.post(reverse('deleteband'), {
            'name': 'Slayer'


    })

    band = Band.objects.filter(name='Sepultura')
    assert (len(band)==1)

@pytest.mark.django_db
def test_month_delete(client):

    # Tests whether it is possible to delete a 'Month' object.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_month'), {
        'name': 'Maj',
        'year': 2021

    })




    response = client.post(reverse('deletemonth'), {
            'name': 'Maj',
            'year': 2021


    })

    month = Month.objects.filter(name='Maj')
    assert (len(month)==0)

@pytest.mark.django_db
def test_month_delete_second_one(client):

    # Tests whether it is possible to delete one of two 'Month' objects.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_month'), {
        'name': 'Maj',
        'year': 2021

    })

    response = client.post(reverse('add_month'), {
        'name': 'Kwiecień',
        'year': 2021

    })


    response = client.post(reverse('deletemonth'), {
            'name': 'Maj',
            'year': 2021


    })

    month = Month.objects.filter(name='Kwiecień')
    assert (len(month)==1)

@pytest.mark.django_db
def test_back_log_modify(client):

    # Tests whether it is possible to modify a 'Backlog' object.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('addbacklog'), {
            'name': 'Zaległość 50',
            'description': 'Jeżeli nie grałem 50 minut w ciągu dnia, odejmuję ilość minut gry of 50 i dopisuję do zaległości.',
            'value': 25

    })

    response = client.post(reverse('modifybacklog'), {
        'name': 'Zaległość 50',
        'value': 0

    })

    back_log = Back_log.objects.filter(name='Zaległość 50', value=0)
    assert (len(back_log)==1)

@pytest.mark.django_db
def test_back_log_modify_second_one(client):

    # Tests whether, after a modification of 'Backlog' object, there is no object with the old value.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('addbacklog'), {
            'name': 'Zaległość 10',
            'description': 'Jeżeli nie grałem 10 minut w ciągu dnia, odejmuję ilość minut gry of 10 i dopisuję do zaległości.',
            'value': 10

    })

    response = client.post(reverse('modifybacklog'), {
        'name': 'Zaległość 10',
        'value': 0

    })

    back_log = Back_log.objects.filter(name='Zaległość 10', value=10)
    assert (len(back_log)==0)

@pytest.mark.django_db
def test_month_modify(client):

    # Tests whether it is possible to modify a 'Month' object by creating a relation with an 'Exercise' object.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)



    response = client.post(reverse('add_exercise'), {
        'name': 'Co drugi próg',
        'description': 'Granie co drugiego progu.',
        'speed': 60

    })

    response = client.post(reverse('add_month'), {
            'name': 'Lipiec',
            'year': 2021,



    })

    response = client.post(reverse('modifymonth'), {
        'name': 'Lipiec',
        'year': 2021,
        'exercise': 'Co drugi próg'

    })


    month = Month.objects.get(name='Lipiec')
    exercise_thing = Exercise.objects.get(name='Co drugi próg')

    assert month.exercise.get(name='Co drugi próg') == exercise_thing

@pytest.mark.django_db
def test_month_modify_second_one(client):

    # Tests whether it is possible to modify a 'Month' object by creating a relation with a 'Song' object.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_band'), {
        'name': 'Metallica',
        'year_of_creation': 1981,
    })

    response = client.post(reverse('add_song'), {
        'name': 'Master of Puppets',
        'genre': 'Thrash Metal',
        'band': 'Metallica'

    })



    response = client.post(reverse('add_month'), {
            'name': 'Lipiec',
            'year': 2021,



    })

    response = client.post(reverse('modifymonth'), {
        'name': 'Lipiec',
        'year': 2021,
        'song': 'Master of Puppets'

    })


    month = Month.objects.get(name='Lipiec')
    song_thing = Song.objects.get(name='Master of Puppets')

    assert month.song.get(name='Master of Puppets') == song_thing

@pytest.mark.django_db
def test_exercise_modify(client):

    # Tests whether it is possible to modify an 'Exercise' object.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_exercise'), {
            'name': '2 plus 1',
            'description': 'Dwa dźwięki na jednej strunie, jeden na drugiej.',
            'speed': 106

    })

    response = client.post(reverse('modifyexercise'), {
        'name': '2 plus 1',
        'speed': 120

    })

    exercise = Exercise.objects.filter(name='2 plus 1', speed=120)
    assert (len(exercise)==1)

@pytest.mark.django_db
def test_exercise_modify_second_one(client):

    # Tests whether, after a modification of an 'Exercise' object, there is no object with the old value.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_exercise'), {
            'name': 'Szybko na jednej strunie',
            'description': 'Szybka melodia na jednej strunie.',
            'speed': 100

    })

    response = client.post(reverse('modifyexercise'), {
        'name': 'Szybko na jednej strunie',
        'speed': 125

    })

    exercise = Exercise.objects.filter(name='Szybko na jednej strunie', speed=100)
    assert (len(exercise)==0)

@pytest.mark.django_db
def test_display_band(client):

    # Tests whether created 'Band' object is displayed in the list.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_band'), {
        'name': 'Soulfly',
        'year_of_creation': 1997,
    })



    response = client.get(reverse('bandsdisplay'))

    band = Band.objects.get(name='Soulfly')

    assert response.context['bands'][0] == band

@pytest.mark.django_db
def test_display_band_second_one(client):

    # Tests whether second created 'Band' object is displayed in the list.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_band'), {
        'name': 'Soulfly',
        'year_of_creation': 1997,
    })

    response = client.post(reverse('add_band'), {
        'name': 'Limp Bizkit',
        'year_of_creation': 1994,
    })



    response = client.get(reverse('bandsdisplay'))

    band = Band.objects.get(name='Limp Bizkit')

    assert response.context['bands'][1] == band

@pytest.mark.django_db
def test_display_song(client):

    # Tests whether created 'Song' object is displayed in the list.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_band'), {
        'name': 'Porcupine Tree',
        'year_of_creation': 1987
    })

    response = client.post(reverse('add_song'), {
        'name': 'Anesthetize',
        'genre': 'Progressive Rock',
        'band': 'Porcupine Tree'

    })



    response = client.get(reverse('songsdisplay'))

    song = Song.objects.get(name='Anesthetize')

    assert response.context['songs'][0] == song


@pytest.mark.django_db
def test_display_song_second_one(client):

    # Tests whether second created 'Song' object is displayed in the list.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_band'), {
        'name': 'Porcupine Tree',
        'year_of_creation': 1987
    })

    response = client.post(reverse('add_song'), {
        'name': 'Anesthetize',
        'genre': 'Progressive Rock',
        'band': 'Porcupine Tree'

    })

    response = client.post(reverse('add_song'), {
        'name': 'Sentimental',
        'genre': 'Progressive Rock',
        'band': 'Porcupine Tree'

    })



    response = client.get(reverse('songsdisplay'))

    song = Song.objects.get(name='Sentimental')

    assert response.context['songs'][1] == song

@pytest.mark.django_db
def test_display_exercise(client):

    # Tests whether created 'Exercise' object is displayed in the list.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_exercise'), {
        'name': 'Pierwsza pozycja pentatoniki',
        'description': 'Granie wszystkich dźwięków pierwszej pozycji pentatoniki',
        'speed': 120

    })





    response = client.get(reverse('exercisesdisplay'))

    exercise = Exercise.objects.get(name='Pierwsza pozycja pentatoniki')

    assert response.context['exercises'][0] == exercise

@pytest.mark.django_db
def test_display_exercise_second_one(client):

    # Tests whether second created 'Exercise' object is displayed in the list.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_exercise'), {
        'name': 'Pierwsza pozycja pentatoniki',
        'description': 'Granie wszystkich dźwięków pierwszej pozycji pentatoniki',
        'speed': 120

    })

    response = client.post(reverse('add_exercise'), {
        'name': 'Druga pozycja pentatoniki',
        'description': 'Granie wszystkich dźwięków drugiej pozycji pentatoniki',
        'speed': 120

    })





    response = client.get(reverse('exercisesdisplay'))

    exercise = Exercise.objects.get(name='Druga pozycja pentatoniki')

    assert response.context['exercises'][1] == exercise

@pytest.mark.django_db
def test_display_month(client):

    # Tests whether created 'Month' object is displayed in the list.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_month'), {
        'name': 'Listopad',
        'year': 2021

    })





    response = client.get(reverse('monthdisplay'))

    month = Month.objects.get(name='Listopad')

    assert response.context['months'][0] == month

@pytest.mark.django_db
def test_display_month_second_one(client):

    # Tests whether second created 'Month' object is displayed in the list.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('add_month'), {
        'name': 'Listopad',
        'year': 2021

    })

    response = client.post(reverse('add_month'), {
        'name': 'Październik',
        'year': 2021

    })



    response = client.get(reverse('monthdisplay'))

    month = Month.objects.get(name='Październik')

    assert response.context['months'][1] == month

@pytest.mark.django_db
def test_display_backlog(client):

    # Tests whether created 'Backlog' object is displayed in the list.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('addbacklog'), {
        'name': 'Zaległość 300',
        'description': 'Jeżeli nie grałem 300 minut w ciągu dnia, odejmuję ilość minut gry of 300 i dopisuję do zaległości.',
        'value': 0

    })





    response = client.get(reverse('backlogdisplay'))

    backlog = Back_log.objects.get(name='Zaległość 300')

    assert response.context['back_logs'][0] == backlog

@pytest.mark.django_db
def test_display_backlog_second_one(client):

    # Tests whether second created 'Backlog' object is displayed in the list.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.post(reverse('addbacklog'), {
        'name': 'Zaległość 300',
        'description': 'Jeżeli nie grałem 300 minut w ciągu dnia, odejmuję ilość minut gry od 300 i dopisuję do zaległości.',
        'value': 0

    })

    response = client.post(reverse('addbacklog'), {
        'name': 'Zaległość 1000',
        'description': 'Jeżeli nie grałem 1000 minut w ciągu dnia, odejmuję ilość minut gry od 1000 i dopisuję do zaległości.',
        'value': 0

    })




    response = client.get(reverse('backlogdisplay'))

    backlog = Back_log.objects.get(name='Zaległość 1000')

    assert response.context['back_logs'][1] == backlog

@pytest.mark.django_db
def test_titlescreen(client):

    # Tests whether it is possible to display 'titlescreen' website.

    response = client.get(reverse('titlescreen'))

    assert response.status_code == 200

@pytest.mark.django_db
def test_menu(client):

    # Tests whether it is possible to display 'menu' website.

    response = client.get(reverse('menu'))

    assert response.status_code == 302

@pytest.mark.django_db
def test_start(client):

    # Tests whether it is possible to display 'start' website.

    response = client.get(reverse('start'))

    assert response.status_code == 200

@pytest.mark.django_db
def test_backlog(client):

    # Tests whether it is possible to display 'backlog' website.

    response = client.get(reverse('backlog'))

    assert response.status_code == 200

@pytest.mark.django_db
def test_exercise(client):

    # Tests whether it is possible to display 'exercisemenu' website.

    response = client.get(reverse('exercisemenu'))

    assert response.status_code == 200

@pytest.mark.django_db
def test_song(client):

    # Tests whether it is possible to display 'songs' website.

    response = client.get(reverse('songs'))

    assert response.status_code == 200

@pytest.mark.django_db
def test_band(client):

    # Tests whether it is possible to display 'band' website.

    response = client.get(reverse('band'))

    assert response.status_code == 200

@pytest.mark.django_db
def test_month(client):

    # Tests whether it is possible to display 'month' website.

    response = client.get(reverse('month'))

    assert response.status_code == 200

@pytest.mark.django_db
def test_logout(client):

    # Tests whether it is possible to display 'logout' website.

    response = client.get(reverse('logout'))

    assert response.status_code == 302

@pytest.mark.django_db
def test_start_start(client):

    # Tests whether it is possible to log in.

    user = User.objects.create_user('User_2', email='email_5@thing.pl', password='password_it_is')

    response = client.post(reverse('start'), {
        'username': 'User_2',
        'password': 'password_it_is',
        'email': 'email_5@thing.pl'
    })


    assert response.status_code == 200


@pytest.mark.django_db
def test_start_start_thing(client):

    # Tests whether proper message is displayed after successful logging in process.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    response = client.post(reverse('start'), {
        'username': 'User_1',
        'password': 'password_thing',
        'email': 'email@thing.pl'
    })


    assert response.context['message'] == 'Udało Ci się podać pasujące do siebie hasło i login. Zostałeś zalogowany.'

@pytest.mark.django_db
def test_addloginpassword(client):

    # Tests whether it is possible to add new user.

    response = client.post(reverse('addloginpassword'), {
        'login': 'User_5',
        'password': 'password_it_is_2',
        'repeated_password': 'password_it_is_2',
        'email': 'email_10@thing.pl'

    })


    assert response.status_code == 200

@pytest.mark.django_db
def test_addloginpassword_second_one(client):

    # Tests whether a proper message is displayed after successful creation of a new user.

    response = client.post(reverse('addloginpassword'), {
        'login': 'User_10',
        'password': 'password_it_is_50',
        'repeated_password': 'password_it_is_50',
        'email': 'email_10@thing.pl'

    })


    assert response.context['message'] == 'Utworzono nowego użytkownika.'

@pytest.mark.django_db
def test_addloginpassword_third_one(client):

    # Tests whether a proper message is displayed after an attempt to create a user a username that has already been used.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    response = client.post(reverse('addloginpassword'), {
        'login': 'User_1',
        'password': 'password_it_is_50',
        'repeated_password': 'password_it_is_50',
        'email': 'email_10@thing.pl'

    })


    assert response.context['message'] == 'Taki użytkownik już istnieje.'

@pytest.mark.django_db
def test_addloginpassword_fourth_one(client):

    # Tests whether a proper message is displayed after a failure to provide two identical passwords.

    response = client.post(reverse('addloginpassword'), {
        'login': 'User_1',
        'password': 'password_it_is_50',
        'repeated_password': 'password_it_is_5',
        'email': 'email_10@thing.pl'

    })


    assert response.context['message'] == 'Hasła nie są takie same.'

@pytest.mark.django_db
def test_logout_second_one(client):

    # Tests whether a proper message is displayed after a successful logging out process.

    user = User.objects.create_user('User_1', email='email@thing.pl', password='password_thing')

    client.force_login(user=user)

    response = client.get(reverse('logout'))

    assert response.context['message'] == 'Nastąpiło wylogowanie.'

@pytest.mark.django_db
def test_not_logged(client):

    # Tests whether a proper message is displayed after a logging out attempt without previous successful logging in process.

    response = client.get(reverse('not_logged'))

    assert response.context['message'] == 'Nie byłeś zalogowany w momencie kliknięcia.'

@pytest.mark.django_db
def test_not_logged_second_one(client):

    # Tests whether it is possible to display 'not_logged' website.

    response = client.get(reverse('not_logged'))

    assert response.status_code == 200



