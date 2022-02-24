from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required

from main import models, forms

# Create your views here.
@login_required
def profile(requests):
    context = {}
    return render(requests, 'main/profile.html', context)

@login_required
def profile_update(requests):
    if requests.method == 'POST':
        form = forms.UpdateUser(requests.POST, instance=requests.user)
        emp_form = forms.UpdateEmployee(requests.POST, requests.FILES, instance=requests.user.employee)
        if form.is_valid() and emp_form.is_valid():
            user = form.save()
            emp = emp_form.save(commit=False)
            emp.user = user
            emp.save()

            return redirect('profile')
    else:
        form = forms.UpdateUser(instance=requests.user)
        emp_form = forms.UpdateEmployee(instance=requests.user.employee)
    context = {
        'form': form,
        'emp_form': emp_form
    } 
    return render(requests, 'main/profileupdate.html', context)

@login_required
def user_dashboard(requests):
    user = requests.user
    emp_details = models.Employee.objects.get(id = user.id)
    assets = emp_details.assets.all()
    assets_info = []
    for asset in assets:
        temp = {}
        temp['id'] = asset.id
        temp['name'] = asset
        obj = models.Possesion.objects.get(employee = user.id, product = asset.id)
        temp['fromdate'] = obj.fromdate
        temp['issueraised'] = obj.issueraised
        temp['underprocess'] = obj.underprocess
        assets_info.append(temp)

    context = {
        'name': emp_details.name,
        'assets': assets_info
    }
    return render(requests, 'main/employee.html', context)

class UserDashboard(DetailView):
    model = models.Employee
    template_name = 'main/dashboard.html'