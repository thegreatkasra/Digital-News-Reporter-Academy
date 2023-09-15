from django.shortcuts import render ,get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator  import Paginator ,EmptyPage ,PageNotAnInteger
from taggit.models import Tag


def blog_view(request, author_username=None, **kwargs):
    current_time = timezone.now()  
    posts = Post.objects.filter(published_date__lte=current_time, status=1).order_by('-published_date')

    if author_username:
        posts = posts.filter(author__username=author_username)

    if kwargs.get('tag_name') is not None:
        # Use filter instead of Post.filter
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    # Pagination (next-previous page)
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    all_tags = Tag.objects.all()

    context = {'posts': posts, 'all_tags': all_tags}
    return render(request, 'blog/blog.html', context)
    

def blog_single(request, pid):
    current_time = timezone.now() 
    all_posts = Post.objects.all()
     #status=1 فقط به منتشر شده ها دسترسی نمایش میده
     #get_object_or_404 :  یعنی اگر نبود پیام 404 
    post = get_object_or_404(all_posts, pk=pid, status=1 ,published_date__lte=current_time)
    #هر با دیده شود یکی اضافه کند
    post.counted_views += 1
    post.save()

    prev_post = all_posts.filter(pk__lt=pid,status=1).last()
    next_post = all_posts.filter(pk__gt=pid,status=1).first()

    all_tags = Tag.objects.all()

    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
        'all_tags': all_tags,
    }
    return render(request,'blog/blog-single.html',context)

#make url for categories
def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/categories-posts.html',context)

#SEARCH function
def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        posts = posts.filter(content__contains = request.GET.get('s'))
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)

