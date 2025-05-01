from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from pragmatic.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

has_ownership = [profile_ownership_required, login_required]

# Create your views here.
@method_decorator(profile_ownership_required, name='get')
@method_decorator(profile_ownership_required, name='post')
class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        # commit=False 폼에서 생성된 객체를 데이터베이스에 저장하지 않고 "임시 객체"로 먼저 반환해주는 명령
        temp_profile = form.save(commit=False)
        # user 필드는 null=False, 즉 무조건 채워져야 하는 필수 항목
        # 보안상 form에서는 user를 제외함.
        # 이 과정이 없으면 user가 NULL로 저장되며,
        # NOT NULL constraint failed: profileapp_profile.user_id 에러가 납니다.

        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

@method_decorator(profile_ownership_required, name='get')
@method_decorator(profile_ownership_required, name='post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'