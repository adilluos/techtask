from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Profile, ProfileHistory
from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken

def index(request):
    if request.user.is_authenticated:
        return redirect('profilepage')
    return render(request, 'main/index.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('registration')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('registration')
            elif len(password) < 8:
                messages.info(request, 'Password must be at least 8 characters long')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, email=user_model.email)
                new_profile.save()

                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return redirect('settings')
        else:
            messages.info(request, 'Password dismatch')
            return redirect('registration')
    else:
        return render(request, 'main/registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            user_profile = Profile.objects.get(user=request.user)
            update_history(user_profile, 'login', "Login")
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return redirect('profilepage')
        else:
            messages.info(request, 'Invalid login')
            return redirect('login')
    else:
        return render(request, 'main/login.html')

@login_required(login_url='login')
def logout(request):
    user_profile = Profile.objects.get(user=request.user)
    update_history(user_profile, 'logout', "Logout")
    refresh_token = request.COOKIES.get('refresh_token')
    if refresh_token:
        try:
            RefreshToken(refresh_token).blacklist()
        except Exception as e:
            # Handle exception (e.g., token not found, token already blacklisted)
            pass
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def profilepage(request):
    user_profile = Profile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'main/profilepage.html', context)

@login_required
def activity(request):
    user_profile = Profile.objects.get(user=request.user)
    history_entries = ProfileHistory.objects.filter(user_profile=user_profile).order_by('-timestamp')
    return render(request, 'main/activity.html', {'history_entries': history_entries})

def update_history(user_profile, activity_type, details=""):
    ProfileHistory.objects.create(
        user_profile=user_profile,
        activity_type=activity_type,
        details=details
    )

@login_required(login_url='login')
def settings(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user_profile.save()
            messages.success(request, "Profile settings successfully updated.")
            update_history(user_profile, 'update', "Changed profile settings")
            return redirect('settings')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'main/settings.html', {'form': form, 'user_profile': user_profile})
