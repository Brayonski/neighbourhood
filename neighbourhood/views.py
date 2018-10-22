from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, NewPostForm, AddCommunityForm,ProfileUpdateForm,UserUpdateForm, CreateBusinessForm
from django.contrib.auth.models import User
from .models import Neighbourhood, User, Business, Profile, Posts

@login_required(login_url='/accounts/login/')
def home(request):
    image = Neighbourhood.objects.get(pk=request.user.profile.neighbourhood.id)
    images = Posts.objects.filter(neighbourhood=image)
    business = Neighbourhood.objects.get(pk=request.user.profile.neighbourhood.id)
    businesses = Business.objects.filter(neighbourhood=business)
    hood = Neighbourhood.objects.get(pk=request.user.profile.neighbourhood.id)
    hoods = Neighbourhood.objects.filter(Neighbourhood_name=hood)
    users = User.objects.all()
    return render(request,'index.html',{"images":images,'date': myDate,"businesses":businesses,"hoods":hoods,"users":users})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user

    ordering=['-date_posted']
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form":form})

@login_required(login_url='/accounts/login/')
def create_business(request, user_id=None):
    current_user = request.user

    ordering=['-date_posted']
    if request.method == 'POST':
        form = CreateBusinessForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('home')
    else:
        form = CreateBusinessForm()
    return render(request, 'create_business.html', {"form":form})

@login_required(login_url='/accounts/login/')
def location(request, user_id=None):
    current_user = request.user

    ordering=['-date_posted']
    if request.method == 'POST':
        form = AddCommunityForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('home')
    else:
        form = AddCommunityForm()
    return render(request, 'add_community.html', {"form":form})

@login_required(login_url='/accounts/login/')
def profile(request,  user_id=None):
    hood = Profile.objects.all()
    if user_id == None:
        user_id=request.user.id
    current_user = User.objects.get(id = user_id)
    name = current_user
    profile = User.objects.all()

    return render(request, 'profile.html', locals())



@login_required(login_url='/accounts/login/')
def updateprofile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'updateprofile.html', context)
    
@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]: 
        search_term = request.GET.get("business")
        searched_projects = Business.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message, "businesses": searched_projects})        
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})