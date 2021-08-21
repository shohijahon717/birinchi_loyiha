from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #UserPassesTestMixin maqolani yozgan odam boshqarishi un # ruxsatnomalar uchun

from django.shortcuts import get_object_or_404, redirect, render # yangi qo'shildi
from django.contrib.auth.decorators import login_required # yangi qo'shildi
from .models import Article, Comment
from django.views.generic import *
from django.urls import reverse_lazy
from .forms import CommentForm


# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    ordering = ['-id']

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login' # login sahifasiga o'tishi uchun
    
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login' # login sahifasiga o'tishi uchun
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def test_func(self):
        return self.request.user.is_superuser 
    
    


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ('title', 'body', 'photo')
    login_url = 'login' # login sahifasiga o'tishi uchun
    def form_valid(self, form):     # avtor avtomatik kiritilishi un
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user # o'ziga tegishli maqolani ozgartirish uchun

    def test_func(self):
        return self.request.user.is_superuser #  agar admin bolmasa tahrirlash ishlamaydi


class ArticleCreateView(UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', 'photo')
    
    def form_valid(self, form):     # avtor avtomatik kiritilishi un
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        return self.request.user.is_superuser #  agar admin bolmasa tahrirlash ishlamaydi


def searchpage(request):
    if request.method == "POST":
        a = request.POST['element'] # qidirilayotgan element nomini a ga yuklaydi 
        topilma = Article.objects.filter(title__contains=a)
        return render(request,"qidiruv.html", {"qidirilayotgan":a, "topilmalar":topilma})
    else:
        return render(request, "qidiruv.html",{})





def add_comment_to_post(request, pk):
    post = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('article_detail', pk=post.pk)
            
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})

    
