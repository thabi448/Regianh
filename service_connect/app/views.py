from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, IssueForm
from .models import Issue


def home(request):
    return render(request, 'home.html')


def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Account created successfully!")
        return redirect('login')
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'login.html')


@login_required
def dashboard(request):
    issues = Issue.objects.filter(user=request.user).order_by('-created_at')[:5]
    return render(request, 'dashboard.html', {'issues': issues})


@login_required
def report_issue(request):
    form = IssueForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        issue = form.save(commit=False)
        issue.user = request.user
        issue.save()
        messages.success(request, "Issue reported successfully!")
        return redirect('dashboard')

    return render(request, 'report.html', {'form': form})


@login_required
def track_issues(request):
    issues = Issue.objects.filter(user=request.user)
    return render(request, 'track.html', {'issues': issues})


@login_required
def view_issues(request):
    issues = Issue.objects.all()
    return render(request, 'view.html', {'issues': issues})


@login_required
def profile(request):
    return render(request, 'profile.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Issue.objects.create(
            name=name,
            email=email,
            message=message
        )

    return render(request, 'contact.html')
def offices(request):
    return render(request, 'offices.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')