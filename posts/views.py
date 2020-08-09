from django.shortcuts import render, get_object_or_404, redirect
from taggit.models import Tag
from django.db.models import Q, Count
from django.core.paginator import Paginator

from .models import Post, Comment
from .forms import CommentForm, UploadForm

def PostView(request):
    # In order to test the pagination, i'll set a post limit for each page. 2 posts each page
    posts = Post.objects.order_by('-published')
    tag = Post.tags.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = []
    for t in page_obj:
        tags.append(t.tags.all)

    return render(request, 'main/index.html', {'posts':posts, 'page_obj':page_obj, 'tag':tags})

def DetailView(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    tags = []
    for t in post.tags.all():
        tags.append(t)

    comments = post.comments
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'posts/post_detail.html', {'post':post, 'tag':tags, 'comments':comments, 'new_comment':
                                                        new_comment, 'comment_form':comment_form})

def TagView(request, tags):
    tags = Tag.objects.filter(slug=tags).values_list('name', flat=True)
    posts = Post.objects.filter(tags__name__in=tags)
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    tag_name = []
    for post in page_obj:
        for tag in post.tags.all():
            if tag in tag_name:
                pass
            else:
                tag_name.append(tag)

    return render(request, 'posts/tag_specific.html', {'posts':posts, 'tag':tag_name, 'page_obj':page_obj})