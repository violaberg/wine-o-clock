from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """
    View to display a list of posts.

    Attributes:
        queryset: Queryset of posts filtered by status.
        template_name: Name of the template used to render the list of posts.
        paginate_by: Number of posts per page for pagination.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/post_list.html"
    paginate_by = 3


def post_detail(request, slug):
    """
    Display an individual blog post.

    Args:
        request: HttpRequest object.
        slug: The slug parameter to identify the blog post.

    Returns:
        HttpResponse object rendering the post detail page.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
         },
    )


def comment_edit(request, slug, comment_id):
    """
    Handle editing comments.

    Args:
        request: HttpRequest object.
        slug: The slug parameter to identify the blog post.
        comment_id: The ID of the comment to be edited.

    Returns:
        HttpResponse object redirecting to the post detail page \
        after editing the comment.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Handle deleting comments.

    Args:
        request: HttpRequest object.
        slug: The slug parameter to identify the blog post.
        comment_id: The ID of the comment to be deleted.

    Returns:
        HttpResponse object redirecting to the post detail page \
        after deleting the comment.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
