from django.forms import ModelForm
from .models import Vote

class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ['question_text','option_one_text','option_two_text','option_three_text','option_one_image_url','option_two_image_url','option_three_image_url']