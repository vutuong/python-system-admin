from django.contrib import admin
from ip_addresses.models import NetworkAddress
# Register your models here.
class NetworkAddressAdmin(admin.ModelAdmin):
    pass
admin.site.register(NetworkAddress, NetworkAddressAdmin)