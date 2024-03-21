import nmap3
import xmltodict
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv46_address
import nmap
import os #MAKE SURE TO IMPORT 'os' TO VIEWS.PY
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import ScanResult



#MAKE SURE TO ADD THIS ADDITIONAL CODE FOR DEF HOME(REQUEST): TO THE PRODUCTION APP
def home(request):
    context = {
        'user': request.user,
        'google_client_id': settings.GOOGLE_CLIENT_ID, #change to this in production: os.environ.get('GOOGLE_CLIENT_ID')
        'google_redirect_uri': settings.GOOGLE_REDIRECT_URI, #os.environ.get('GOOGLE_REDIRECT_URI')
    }
    print(request.user.is_authenticated)
    return render(request, 'home.html', context)

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
        result = scanner.nmap_no_portscan(ip_address, args="-PR")  # Scan the specified IP address
        
        for scanned_ip, host_info in result.items():
            hostname = ""
            os = ""
            open_ports = ""
            
            if isinstance(host_info, list):
                for item in host_info:
                    if 'hostname' in item:
                        hostname_list = item['hostname']
                        if hostname_list:
                            hostname = hostname_list[0].get('name', "")
                    
                    if 'osmatch' in item:
                        os_info = item['osmatch']
                        if os_info:
                            os = os_info[0].get('name', "")
                    
                    ports = item.get('ports', [])
                    open_ports = ','.join(str(port['portid']) for port in ports)
                    
                    # Create ScanResult and associate it with the logged-in user
                    ScanResult.objects.create(user=user, ip_address=scanned_ip, hostname=hostname, os=os, open_ports=open_ports)
            else:
                if 'hostname' in host_info:
                    hostname_list = host_info['hostname']
                    if hostname_list:
                        hostname = hostname_list[0].get('name', "")
                
                if 'osmatch' in host_info:
                    os_info = host_info['osmatch']
                    if os_info:
                        os = os_info[0].get('name', "")
                
                ports = host_info.get('ports', [])
                open_ports = ','.join(str(port['portid']) for port in ports)
                
                # Create ScanResult and associate it with the logged-in user
                ScanResult.objects.create(user=user, ip_address=scanned_ip, hostname=hostname, os=os, open_ports=open_ports)
        
        # Redirect to the reports page after successful scan
        return redirect('reports')
    
    # Render the scan_devices.html template if request method is not POST
    return render(request, 'scan_devices.html')

@login_required
def reports(request):
    # Fetch the scan results associated with the logged-in user
    user = request.user
    scan_results = ScanResult.objects.filter(user=user)
    
    # Pass the scan results to the template for rendering
    return render(request, 'reports.html', {'scan_results': scan_results})

def detail(request):
    # Add your logic to fetch and render detail view
    return render(request, 'detail.html')

def index(request):
    # Add your logic to fetch and render list of reports
    return render(request, 'index.html')

def edit_profile(request):
    # Add your logic to edit user profile
    return render(request, 'edit_profile.html')

def create_report(request):
    # Add your logic to create a new report
    return render(request, 'create_report.html')

def delete_report(request):
    # Add your logic to delete a report
    return render(request, 'delete_report.html')

def search_devices(request):
    # Add your logic to search for devices
    return render(request, 'search_devices.html')
