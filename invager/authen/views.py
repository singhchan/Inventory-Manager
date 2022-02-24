from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from main.forms import EmployeeCreationForm

# Create your views here.
class Login(LoginView):
    template_name = 'authen/login.html'
    redirect_authenticated_users = True
    def get_success_url(self):
        # write your logic here
        if self.request.user.is_superuser:
            return '/admin'
        return '/'

class Logout(LogoutView):
    template_name = 'authen/logout.html'

def register(requests):
    if requests.method == 'POST':
        form = UserCreationForm(requests.POST)
        emp_form = EmployeeCreationForm(requests.POST)
        if form.is_valid() and emp_form.is_valid():
            user = form.save()
            emp = emp_form.save(commit=False)
            emp.user = user
            emp.save()

            return redirect('login')
        else:
            pass
    else:
        form = UserCreationForm()
        emp_form = EmployeeCreationForm()
    context = {
        'form': form,
        'emp_form': emp_form,
    } 
    return render(requests, 'authen/register.html', context)