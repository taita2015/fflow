from website.utils import console
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth.models import User
from space.forms import UserForm

from index.appviews import AppBaseTemplateView
from space.forms import UserProfileForm
from index.models import UserProfile
from space.forms import UserAvatarForm


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import UserForm

from website.utils import console
from website.utils import messages





@method_decorator(login_required,name='dispatch')
class UserDataView(AppBaseTemplateView):
    template_name = "space/userdata.html"
    def get(self, request,context={}, *args, **kwargs):
        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
        user_avatar_form = UserAvatarForm(instance=request.user.userprofile)

        return super(UserDataView, self).get(request,context={"user_form":user_form,"user_profile_form":user_profile_form,"user_avatar_form":user_avatar_form}, *args, **kwargs)


    def post(self,request,context={},*args,**kwargs):

        form_name = request.POST.get('form_name',None)

        if form_name == "user_avatar_form":
            uaf = UserAvatarForm(request.POST,request.FILES,instance=request.user.userprofile)
            if uaf.is_valid():
                uaf.save()
        elif form_name == 'user_data':
            uaf = UserProfileForm(request.POST, instance=request.user.userprofile)
            if uaf.is_valid():
                uaf.save()
            uf = UserForm(request.POST,instance=request.user)
            if uf.is_valid():
                uf.save()
        elif form_name == 'password_changing':
            print('password_changing')
            pass
        elif form_name =='email_changing':
            print('email_changing')
            pass

        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
        user_avatar_form = UserAvatarForm(instance=request.user.userprofile)

        return super(UserDataView, self).post(request,context={"user_form":user_form,"user_profile_form":user_profile_form,"user_avatar_form":user_avatar_form},*args,**kwargs)


class UserHomePageView(AppBaseTemplateView):
    pass























