from django.forms import *
from tpo.models import *
from django.contrib.auth.models import User


class LeaveForm(ModelForm):
    class Meta:
        model = LeavePage
        fields = '__all__'




class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = '__all__'


