from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from matplotlib.style import context

from histproject.accounts.forms import CustomUserForm, ProfileForm, ProfileDeleteForm
from histproject.accounts.models import Profile

userModel = get_user_model()

class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class EditProfileView(LoginRequiredMixin,  UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_edit.html'

    #def test_func(self):
        #profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        #return self.request.user == profile

    def get_success_url(self):
        return  reverse_lazy(
            'profile_detail',
            kwargs={'pk': self.object.pk}
        )

class DetailProfileView(LoginRequiredMixin, DetailView):
    model = userModel
    template_name = 'accounts/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_count'] =self.object.comment_set.count()
        return context

class DeleteProfileView(LoginRequiredMixin,  DeleteView):
    model = Profile
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('login')
    form_class = ProfileDeleteForm

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile

    def get_initial(self):
        pk= self.kwargs.get(self.pk_url_kwarg)
        profile = Profile.objects.get(pk=pk)
        return profile.__dict__
