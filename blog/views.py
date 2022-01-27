import email
from http.client import HTTPResponse
import imp
from turtle import pos
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . models import Post,Comment
from django.core.paginator import Paginator
from . forms import CommentForm
from taggit.models import Tag
# Create your views here.


def post_list(request,tag_slug=None):
    if tag_slug:
        tag  =get_object_or_404(Tag,slug=tag_slug)
        posts = Post.objects.filter(status="published",tags__in =[tag]   )
    else:
        posts = Post.objects.filter(status="published")
    paginator = Paginator(posts,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj':page_obj,
    }
    return render(request,'post_list.html',context)



def post_detail(request,year,month,day,slug):
    
    post = get_object_or_404(Post,created_date__year=year,
                            created_date__month=month,
                            created_date__day =day,
                            slug = slug,
                            status = 'published')
    
    comment_form =  CommentForm()         
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()  
            
    context = {
        'post':post,
        'comment_form':comment_form ,
        'new_comment':new_comment,
    }
                 
    return render(request,'post_detail.html',context)
    

def contact_us(request):
    return render(request,'contact_us.html')