from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, NewPostForm, AddCommunityForm,ProfileUpdateForm,UserUpdateForm, CreateBusinessForm,CommentForm
from django.contrib.auth.models import User
from .models import Neighbourhood, User, Business, Profile, Posts

@login_required(login_url='/accounts/login/')
def home(request):        
    hoods = Neighbourhood.objects.all()

    try:
        image = Neighbourhood.objects.get(pk=request.user.profile.neighbourhood.id)
        images = Posts.objects.filter(neighbourhood=image)
        business = Neighbourhood.objects.get(pk=request.user.profile.neighbourhood.id)
        businesses = Business.objects.filter(neighbourhood=business)
        users = User.objects.all()
    except:
        message ='No posts yet'
    return render(request,'index.html',locals())

def join(request,new_community):
   # get_usr = get_object_or_404(User,pk=request.user.id)
   try:
       new_communit = get_object_or_404(Neighbourhood, pk=new_community)

       request.user.profile.neighbourhood = new_communit
       request.user.profile.save()
       print('pppppppppppp')
       return redirect('home')

   except:
       return redirect('home')

def left(request):
   location = get_object_or_404(Neighbourhood, pk=request.user.profile.neighbourhood.id)
   if request.user.profile.neighbourhood == location:
       request.user.profile.neighbourhood= None
       request.user.profile.save()
   return redirect('home')

@login_required(login_url='/accounts/login/')
def hoods(request):
    current_user = request.user
    neighbourhoods = Neighbourhood.objects.all()
    print(neighbourhoods)
    return render(request,'navbar.html',{"neighbourhoods":neighbourhoods})


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

#views for commenting
@login_required(login_url='/accounts/login')
def comment_on(request, image_id):
    image = get_object_or_404(Business, pk=image_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user.profile
            comment.image = image
            comment.save()
    return redirect('home')


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