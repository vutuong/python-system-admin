from django.shortcuts import render
# Create your views here.
from ip_addresses.models import *
from django.http import HttpResponse, HttpResponseRedirect
def display(request, address=None):
    if not address:
        parent = None
    else:
        ip, net_size = address.split('/')
        parent = NetworkAddress.objects.get(address=ip, network_size=int(net_size))
    addr_list = NetworkAddress.objects.filter(parent=parent)
    return render(None, 'display.html', {'parent': parent, 'addresses_list': addr_list})

def delete(request, address=None):
    ip, net_size = address.split("/")
    try: 
        parent = NetworkAddress.objects.get(address=ip,network_size=int(net_size)).parent
        NetworkAddress.objects.get(address=ip, network_size=int(net_size)).delete()
    except:
        parent = NetworkAddress.objects.filter(address=ip,network_size=int(net_size)).first().parent
        NetworkAddress.objects.filter(address=ip, network_size=int(net_size)).first().delete()
    redirect_to = '../../../'
    if parent:
        redirect_to += '%s/%s/' % (parent.address, int(parent.network_size))
    return HttpResponseRedirect(redirect_to)

def add(request, address=None):
    if request.method == 'POST':
        parent = None
        if address:
            ip, net_size = address.split('/')
            parent = NetworkAddress.objects.get(address=ip,network_size=int(net_size))
        new_address = NetworkAddress(parent=parent)
        form = NetworkAddressAddForm(request.POST, instance=new_address)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("..")
    else:
        form = NetworkAddressAddForm()
    return render(None, 'add.html', {'form': form,})

def modify(request, address=None):
    if request.method == 'POST':
        # submitting changes
        ip, net_size = address.split('/')
        address_obj = NetworkAddress.objects.get(address=ip,network_size=int(net_size))
        form = NetworkAddressModifyForm(request.POST, instance=address_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("..")
    else:
        # first time display
        ip, net_size = address.split('/')
        address_obj = NetworkAddress.objects.get(address=ip,network_size=int(net_size))
        form = NetworkAddressModifyForm(initial={ 'description':address_obj.description, })
    return render(None, 'add.html', {'form': form,})