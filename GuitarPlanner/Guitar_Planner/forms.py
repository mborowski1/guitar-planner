from django import forms


class AddExerciseForm(forms.Form):

    # Form making it possible to create 'Exercise' object.

    name = forms.CharField(label="Nazwa ćwiczenia", max_length=200)
    description = forms.CharField(label="Opis ćwiczenia", max_length=2000)
    speed = forms.IntegerField(label="Szybkość gry")


class AddMonthForm(forms.Form):

    # Form making it possible to create 'Month' object.

    name = forms.CharField(label="Miesiąc", max_length=20)
    year = forms.IntegerField(label="Rok")


class AddSongForm(forms.Form):

    # Form making it possible to create 'Song' object.

    name = forms.CharField(label="Nazwa utworu", max_length=200)
    genre = forms.CharField(label="Gatunek", max_length=200)
    band = forms.CharField(label="Nazwa zespołu", max_length=200)

class AddBandForm(forms.Form):

    # Form making it possible to create 'Band' object.

    name = forms.CharField(label="Nazwa zespołu", max_length=200)
    year_of_creation = forms.IntegerField(label="Rok utworzenia")

class LoginPasswordForm(forms.Form):

    # Form making it possible to log in.

    username = forms.CharField(label="Podaj nazwę użytkownika", max_length=200)
    password = forms.CharField(label="Podaj hasło")
    email = forms.CharField(label="Podaj adres e-mail")

class NewLoginPasswordForm(forms.Form):

    # Form making it possible to create a user.

    login = forms.CharField(label="Podaj nazwę nowego użytkownika", max_length=200)
    password = forms.CharField(label="Podaj nowe hasło")
    repeated_password = forms.CharField(label="Powtórz nowe hasło")
    email = forms.CharField(label="Podaj adres e-mail")

class BacklogForm(forms.Form):

    # Form making it possible to create a 'Backlog' object.

    name = forms.CharField(label="Podaj nazwę zalegości", max_length=500)
    description = forms.CharField(label="Wprowadź opis zalegości", max_length=2000)
    value = forms.IntegerField(label="Wprowadź wartość zalegości")

class ModifyBacklogForm(forms.Form):

    # Form making it possible to modify 'Backlog' object.

    name = forms.CharField(label="Podaj nazwę zalegości, którą chcesz zmodyfikować", max_length=500)
    value = forms.IntegerField(label="Wprowadź nową wartość zalegości")

class DeleteBacklogForm(forms.Form):

    # Form making it possible to modify 'Backlog' object.

    name = forms.CharField(label="Podaj nazwę zalegości, którą chcesz usunąć", max_length=500)

class DeleteExerciseForm(forms.Form):

    # Form making it possible to delete 'Exercise' object.

    name = forms.CharField(label="Podaj nazwę ćwiczenia, które chcesz usunąć", max_length=500)

class DeleteSongForm(forms.Form):

    # Form making it possible to delete 'Song' object.

    name = forms.CharField(label="Podaj nazwę utworu, który chcesz usunąć", max_length=500)

class DeleteBandForm(forms.Form):

    # Form making it possible to delete 'Band' object.

    name = forms.CharField(label="Podaj nazwę zespołu, który chcesz usunąć", max_length=500)

class DeleteMonthForm(forms.Form):

    # Form making it possible to delete 'Month' object.

    name = forms.CharField(label="Podaj nazwę miesiąca, który chcesz usunąć", max_length=500)
    year = forms.IntegerField(label="Podaj rok miesiąca, który chcesz usunąć")

class ModifyMonthForm(forms.Form):

    # Form making it possible to modify 'Month' object.

    name = forms.CharField(label="Podaj nazwę miesiąca, który ma zostać zmodyfikowany", max_length=20)
    year = forms.IntegerField(label="Podaj rok miesiąca, który ma zostać zmodyfikowany")
    exercise = forms.CharField(label="Podaj nazwę ćwiczenia, które chcesz dodać", max_length=200, required=False)
    song = forms.CharField(label="Podaj nazwę utworu, który chcesz dodać", max_length=200, required=False)

class ModifyExerciseForm(forms.Form):

    # Form making it possible to modify 'Exercise' object.

    name = forms.CharField(label="Podaj nazwę ćwiczenia, które ma zostać zmodyfikowane", max_length=200)
    speed = forms.IntegerField(label="Podaj nową szybkość gry")