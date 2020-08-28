from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.db.models import Q, Count
from django.views.generic import ListView, TemplateView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from taggit.models import Tag

from .models import Post, Comment
from .forms import CommentForm, UploadForm
from .utils import check_duplicate, filter_tags


class IndexView(ListView):
    model = Post
    paginate_by = 15
    results = model.objects.order_by('-published')
    template_name = 'main/index.html'
    
    # In order to test the pagination, i'll set a post limit for each page. 3 posts each page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(results=self.results, **kwargs)
        paginator = Paginator(self.results, self.paginate_by)
        page = self.request.GET.get('page')
        page_obj = paginator.get_page(page)
        tags = filter_tags(page_obj)

        context['tag'] = tags
        return context

class PostView(ListView):
    model = Post
    paginate_by = 15
    results = model.objects.order_by('-published')
    template_name = 'main/index.html'
    
    # In order to test the pagination, i'll set a post limit for each page. 3 posts each page
    def get_queryset(self):
        self.q = self.request.GET.get('tags')
        self.q2 = self.request.GET.get('user')
        if self.q:
            self.results = Post.objects.all()
            for tag in self.q.split(' '): 
                self.results = self.results.filter(tags__name=tag)

        if self.q2:
            self.results = Post.objects.all()
            self.results = self.results.filter(uploader__id=self.q2)

            self.results = check_duplicate(self.results)

        return self.results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(results=self.results, **kwargs)
        paginator = Paginator(self.results, self.paginate_by)
        page = self.request.GET.get('page')
        page_obj = paginator.get_page(page)
        tags = filter_tags(page_obj)

        context['tag'] = tags
        context['q'] = self.q
        return context

def DetailView(request, post_id):
    
    q = request.GET.get('tags')
    if q:
        for tag in q.split(' '):
            posts = Post.objects.filter(tags__name=tag)

        iterator = iter(posts)
        post = get_object_or_404(posts, post_id=iterator.post_id)
    else:
        post = get_object_or_404(Post, post_id=post_id)
    tags = []
    for t in post.tags.all():
        tags.append(t)


    # Comment is ready. You only need to call it in the template
    comments = post.comments.all()
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
    
    #if q:
     #   for tag in q.split(' '):
      #      posts = Post.objects.all().filter(tags__name=tag)

       # context = {'post':post, 'tag':tags, 'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form, 'q':q, 'posts':posts}

    context = {'post':post, 'tag':tags, 'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form, 'q':q}

    return render(request, 'posts/post_detail.html', context)

def TagView(request, tags):
    q = request.GET.get('tags')
    tags = Tag.objects.filter(slug=tags).values_list('name', flat=True)
    posts = Post.objects.filter(tags__name__in=tags)
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    tag_name = filter_tags(page_obj)

    return render(request, 'posts/tag_specific.html', {'posts':posts, 'tag':tag_name, 'page_obj':page_obj, 'q':q })


@login_required
def upload_view(request):
    uploaded = False
    template_name = 'posts/upload.html'
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form = upload_form.save()
            uploaded = True
        else:
            print(upload_form.errors)
            return HttpResponse('Invalid post details')
    else:
        upload_form = UploadForm()
    return render(request, template_name, {
        'upload_form':upload_form,
        'uploaded':uploaded,
    })
