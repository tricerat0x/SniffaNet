from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from .models import Report

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

class ReportCreate(CreateView):
    model = Report 
    fields = ['scan', 'ip_address', 'mac_address', 'device_type', 'description',]
    
class ReportList(ListView):
    model = Report

class ReportDetail(DetailView):
    model = Report

class ReportDelete(DeleteView):
    model = Report
    success_url = '/reports'
