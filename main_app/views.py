# main_app/views.py

import nmap3
import xmltodict
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv46_address
from main_app.models import ScanResult
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def user(request):
    return render(request, 'user.html')

def base(request):
    return render(request, 'base.html')

@login_required
def scan_devices(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        
        try:
            # Validate the IP address
            validate_ipv46_address(ip_address)
        except ValidationError:
            return render(request, 'scan_devices.html', {'error': 'Invalid IP address'})

        # Get the currently logged-in user
        user = request.user

        scanner = nmap3.NmapHostDiscovery()
        result = scanner.nmap_no_portscan(ip_address, args="-PR -oX -") # -oX - outputs XML to stdout
        
        # Parse XML result
        root = ET.fromstring(result)
        scan_results = []
        for host in root.findall('.//host'):
            scanned_ip = host.find('address').attrib['addr']
            hostname = host.find('hostnames/hostname').attrib.get('name', '')
            os = host.find('os/osmatch').attrib.get('name', '')
            ports = ','.join(port.attrib['portid'] for port in host.findall('.//port'))
          
        # Create a ScanResult object and save it
            scan_result = ScanResult.objects.create(
                user=user,
                ip_address=scanned_ip,
                hostname=hostname,
                os=os,
                open_ports=ports
            )
        
        # Return JSON response
        return JsonResponse({'scan_results': scan_results})
    
    # Render the scan_devices.html template if request method is not POST
    return render(request, 'scan_devices.html')

@login_required
def reports(request):
    
    user = request.user
    scan_results = ScanResult.objects.filter(user=user)
    
    # Pass the scan results to the template for rendering
    return render(request, 'reports.html', {'scan_results': scan_results})

def detail(request):
    # Placeholder for detail view logic
    return render(request, 'detail.html')

def index(request):
    # Placeholder for index view logic
    return render(request, 'reports.html')

def create_report(request):
    # Placeholder for create report view logic
    return render(request, 'create_report.html')

def delete_report(request):
    # Placeholder for delete report view logic
    return render(request, 'delete_report.html')

def search_devices(request):
    # Placeholder for search devices view logic
    return render(request, 'search_devices.html')
