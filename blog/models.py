from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# Post model
class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.

    Attributes:
        title (str): The title of the blog post, unique.
        slug (str): A URL-friendly representation of the title, unique.
        author (User): The user who authored the post, \
        related to the `auth.User` model.
        featured_image (CloudinaryField): An optional image field \
        for the post, with a default placeholder.
        content (str): The main content of the post.
        created_on (datetime): The date and time \
        when the post was created, set automatically.
        status (int): The publication status of the post, \
        defaulting to 'Draft'.
        excerpt (str): A short summary of the post, optional.
        updated_on (datetime): The date and time \
        when the post was last updated, set automatically.

    Meta:
        ordering (list): Orders posts by creation date in descending order.

    Methods:
        __str__(): Returns a string representation of the post, \
        including the title and author.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


# Comment model
class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.

    Attributes:
        post (Post): The blog post that this comment is related to.
        author (User): The user who authored the comment, \
        related to the `auth.User` model.
        body (str): The main content of the comment.
        approved (bool): Whether the comment is approved \
        for display, defaulting to `False`.
        created_on (datetime): The date and time \
        when the comment was created, set automatically.

    Meta:
        ordering (list): Orders comments by creation date in descending order.

    Methods:
        __str__(): Returns a string representation of the comment, \
        including the body and author.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.body} by {self.author}"
