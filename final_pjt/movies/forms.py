from django import forms
from .models import Review, Comment, Movie, Genre


class MovieForm(forms.ModelForm):
    genre_ids = forms.ModelMultipleChoiceField(
        label = 'Genre',
        queryset = Genre.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Movie
        fields = ["title", "original_title", "release_date", "popularity", "vote_count", "vote_average", "adult", "video", "overview", "original_language", "poster_path", "backdrop_path", "genre_ids",]
        # fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "rank", "content",]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content",]


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'