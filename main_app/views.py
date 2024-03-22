from django.shortcuts import render, redirect
from django.views.generic import DeleteView, DetailView, UpdateView
from .models import Report, User, Scan
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# List of reports
def home(request):
    return render(request, 'home.html')

def user(request):
    return render(request, 'user.html')

def base(request):
    return render(request, 'base.html')


def reports_index(request):
    try:
        reports = Report.objects.filter(user=request.user)
    except Exception as e:
        # Handle any exceptions that may occur during the query
        print("Error fetching reports:", e)
        reports = []

    return render(request, 'reports.html', {'reports': reports})


def reports_detail(request, report_id):
    report = Report.objects.get(id=report_id)
    return render(request, 'reports/detail.html', {
        'report': report
    })



def generate_reports(request, user_id):
    parsed_results = Scan.objects.all()

    for parsed_result in parsed_results:
        json_data = parsed_result.json_data
        ip_address = json_data.get('ip_address')
        mac_address = json_data.get('mac_address')
        device_type = json_data.get('device_type')
        description = json_data.get('description')
    
        report = Report.objects.create(
            ip_address=ip_address, 
            mac_address=mac_address, 
            device_type=device_type, 
            description=description
        )
        report.user_id = user_id
        report.save()
    return redirect('reports_index', user_id=user_id )



class ReportDelete(LoginRequiredMixin, DeleteView):
    model = Report
    success_url = '/reports'


def profile_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'users/profile_detail.html', {'user': user})


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username']
    success_url = '/profile/'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('reports')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

