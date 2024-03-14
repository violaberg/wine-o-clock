from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for creating or updating comments.

    Attributes:
        body (TextField): The textual content of the comment.
    """
    class Meta:
        model = Comment
        fields = ('body',)