import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from users.forms import RegisterForm
from django.contrib.auth.views import LogoutView
from users.models import CustomUser


class CustomLoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        if user:
            login(self.request, user)
        return HttpResponseRedirect('/')


class RegisterView(FormView):
    template_name = 'registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy("list_view")

    def form_valid(self, form):
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = CustomUser.objects.create(username=username,password=password)
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.first_name = form.cleaned_data.get('surname')
        user.save()
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


class LoginValidation(View):
    def post(self, request, **kwargs):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        auth = authenticate(username=username, password=password)

        if auth:
            user = CustomUser.objects.get(username=username)
            login(request, user=user)
            return JsonResponse({"status": "ok"})
        return JsonResponse({"status": "failed",
                             "username_errors": "Ошибка логина или пароля"})


class RegistrationValidation(View):
    def post(self, request, **kwargs):
        data = json.loads(request.body)
        username = data.get('username')
        try:
            CustomUser.objects.get(username=username)
            return JsonResponse({"status": "invalid",
                                 "registration_errors": "Пользователь с таким именем уже существует"})
        except CustomUser.DoesNotExist:
            return JsonResponse({"status": "ok"})
