# main_app/views.py

import nmap3
import xmltodict
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv46_address
from main_app.models import ScanResult
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def user(request):
    return render(request, 'user.html')

@login_required
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
        result = scanner.nmap_no_portscan(ip_address, args="-O -oX -") # Include OS detection and output XML to stdout
        
        # Parse XML result
        try:
            parsed_result = xmltodict.parse(result)
            hosts = parsed_result['nmaprun']['host']
            scan_results = []
            for host in hosts:
                scanned_ip = host['address']['@addr']
                hostname = host.get('hostnames', {}).get('hostname', {}).get('@name', '')
                os = host.get('os', {}).get('osmatch', {}).get('@name', '')
                # Filter out only necessary information for network topology
                relevant_data = {
                    'ip_address': scanned_ip,
                    'hostname': hostname,
                    'os': os,
                }
                scan_result = ScanResult.objects.create(
                    user=user,
                    **relevant_data
                )
                scan_results.append(scan_result)
            
            # Return JSON response
            return JsonResponse({'scan_results': [scan_result.id for scan_result in scan_results]})
        except KeyError:
            return JsonResponse({'error': 'Error parsing XML result'})
    
    # Render the scan_devices.html template if request method is not POST
    return render(request, 'scan_devices.html')

@login_required
def reports(request):
    user = request.user
    scan_results = ScanResult.objects.filter(user=user)
    return render(request, 'reports.html', {'scan_results': scan_results})

