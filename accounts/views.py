from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
#  needed for sending emails
from django.core.mail import send_mail
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.template.loader import get_template

from contacts.models import Contact


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authentification
        user = auth.authenticate(username=username, password=password)

        # if user is in the Database
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Вы зарегистрированны!')
            return redirect('dashboard')
        # user not Found
        else:
            messages.error(request, "'Введенные данны не совпадают")
            return redirect('login')

    # accessing the login page
    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    user_contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "Вы вышли")
        return redirect('index')


def delete_account(request):
    user = request.user
    if request.method == 'POST' and user.is_authenticated and user.username is not 'ilyas':
        user.delete()
        return redirect('index')

    return render(request, 'accounts/delete_account.html')


def register(request):
    # Get form values
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # if user already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Этот пользователь уже существует.")
                return redirect('register')

            else:
                # if email already used
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Эту почту уже использувают.")
                    return redirect('register')
                # registration successfull!
                else:
                    # create user
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    # Login after registration
                    auth.login(request, user)
                    messages.success(request, "You are now logged in")

                    return redirect('index')

        else:
            # if passwords do not matchs
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
