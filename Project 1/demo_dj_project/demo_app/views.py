from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from demo_app.forms import BankAccountForm
from demo_app.forms import BankAccountModelForm, SignUpForm, LoginForm
from demo_app.models import BankAccount
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from demo_app.models import Article
from demo_app.forms import ArticleForm
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
from django.views.decorators.cache import cache_page
User = get_user_model()

# Create your views here.

# @login_required
@cache_page(60*2)
def welcome_page(request):
    print("Function Called....!")
    return render(request, template_name = "demo_app/welcome.html")

def user_logout(request):
    logout(request)
    return redirect('login')


def bank_account_add(request):
    if request.method == 'POST':
        form = BankAccountModelForm(request.POST or None)
        if form.is_valid():
            print("data----->",form.cleaned_data)
            # ba = BankAccount(**form.cleaned_data)
            # ba.save()
            form.save()


        else:
            print("errors----> ", form.cleaned_data)

    form = BankAccountModelForm()

    return render(request, template_name="demo_app/bank_account_add.html",
                  context={"form":form})



def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)

        if form.is_valid():
            print("data---->", form.cleaned_data)
            form.save()

        else:
            print("errors--->", form.errors)

    form = SignUpForm()

    return render(request, template_name="demo_app/signup.html", context={"form": form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print("data--->", form.cleaned_data)
            user = User.objects.filter(username=form.cleaned_data['username']).first()
            login(request, user=user)
            return redirect(request.GET.get('next', '/demo_app/welcome/'))

        else:
            print("errors--->", form.error_messages)
            error_messages = form.error_messages
            return render(request, template_name="demo_app/login.html",
                context={"form": form, 'error_messages': error_messages})

    form = LoginForm()

    return render(request, template_name="demo_app/login.html", context={"form": form})

def article_list(request):
    articles = Article.objects.all()
    for article in articles:
        print(article.posted_on)
    return render(request, template_name='demo_app/articles.html',
                  context={"articles":articles})
@login_required
def article_add(request):
    print("user--->", request.user)
    if request.method == "POST":
        form = ArticleForm(request.POST or None )
        if form.is_valid():
            print("data--->", form.cleaned_data)
            article_post = form.save(commit=False)
            print("-->title", article_post.title)
            article_post.article_post_by = request.user
            article_post.save()

            return redirect('article-list')

        else:
            print("errors--->", form.error_messages)
            error_messages = form.error_messages
            # return render(request, template_name="demo_app/login.html",
            #     context={"form": form, 'error_messages': error_messages})
    form = ArticleForm()

    return render(request, template_name="demo_app/article_add.html",
              context={"form": form})


@login_required
def article_add(request):
    print("user--->", request.user)
    if request.method == "POST":
        form = ArticleForm(request.POST or None )
        if form.is_valid():
            print("data--->", form.cleaned_data)
            article_post = form.save(commit=False)
            print("-->title", article_post.title)
            article_post.article_post_by = request.user
            article_post.save()

            return redirect('article-list')

        else:
            print("errors--->", form.error_messages)
            error_messages = form.error_messages
            # return render(request, template_name="demo_app/login.html",
            #     context={"form": form, 'error_messages': error_messages})
    form = ArticleForm()

    return render(request, template_name="demo_app/article_add.html",
              context={"form": form})

class ScheduleListView(ListView):
    model = Article
    # queryset = ListView
    template_name = "demo_app/schedule.html"
    paginate_by = 1






