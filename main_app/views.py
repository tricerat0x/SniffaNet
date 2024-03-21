from django.shortcuts import render, redirect
from django.views.generic import DeleteView, DetailView, UpdateView
from .models import Report, User, Scan

# Create your views here.
# List of reports
def reports_index(request):
    reports = Report.objects.all()
    return render(request, 'reports/index.html', {
        'reports': reports
    })

# Report details
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



class ReportDelete(DeleteView):
    model = Report
    success_url = '/reports'


def profile_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'users/profile_detail.html', {'user': user})


class ProfileUpdate(UpdateView):
    model = User
    fields = ['username']
    success_url = '/profile/'

