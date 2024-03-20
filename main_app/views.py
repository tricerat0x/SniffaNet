from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def user(request):
  return render(request, 'user.html')
# main_app/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import ScanResult
import nmap3

def scan_devices(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        
        scanner = nmap3.NmapHostDiscovery()
        result = scanner.nmap_no_portscan(ip_address, args="-PR")  # Scan the specified IP address
        
        for ip_address, host_info in result.items():
            hostname = ""
            os = ""
            open_ports = ""
            
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
            
            ScanResult.objects.create(ip_address=ip_address, hostname=hostname, os=os, open_ports=open_ports)
        
        return JsonResponse({'message': 'Scan completed successfully'})
    
    return render(request, 'scan_devices.html')

def reports(request):
  return render(request, 'reports/index.html')