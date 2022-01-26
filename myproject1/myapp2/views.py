from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



def create_user(request):
    user = User.objects.create_user('aaaaa', 'aaa@gmail.com', 'password')

    user.last_name = 'Aza'
    user.save()


def my_view(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            pass
    # Return a 'disabled account' error message
    else:
        pass