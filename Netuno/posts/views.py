from django.shortcuts import render, HttpResponse,get_object_or_404,redirect
from .models import Post
from .forms import LoginForm,UserRegistration, PostRegistrationForm,UpdatePostForm
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


# Views referentes às publicações postadas
@login_required
def posts_list(request):

    if 'q' in request.GET:
        q = request.GET['q']
        posts_list = Post.objects.filter(titulo__icontains=q).order_by('-publicado')

    else:
        posts_list = Post.objects.all().order_by('-publicado')

    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,'posts.html', {"posts_list":posts, 'page':page})


@login_required
def post_form(request):
    if request.method == 'POST':
        new_post = PostRegistrationForm(request.POST)

        if new_post.is_valid():
            post = new_post.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('posts_list')
    else:
        new_post = PostRegistrationForm()
    return render(request,'conta/add_post.html',{'new_post':new_post})

@login_required
def post_detalhes(request,slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request,'detalhes_post.html',{'post':post})


@login_required
def update_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = UpdatePostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect("posts_list")

    return render(request,'conta/update.html',{'form':form})


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect("posts_list")




#Views referentes a autenticação de login e registro de usuario
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])

            if user is not None:
                login(request,user)

                return HttpResponse("Você está autenticado!")

            else:
                return HttpResponse("Login inválido!")

    else:
        form = LoginForm()

    return render(request,'registration/login.html',{'form':form})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'conta/register_done.html',{'user_form':user_form})

    else:
        user_form = UserRegistration()

    return render(request,'conta/register.html',{'user_form':user_form})




