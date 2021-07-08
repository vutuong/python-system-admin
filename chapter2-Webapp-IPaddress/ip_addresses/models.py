from django.db import models
from django.forms import ModelForm
# Create your models here.

class NetworkAddress(models.Model):
    address = models.GenericIPAddressField()
    network_size = models.PositiveIntegerField()
    description = models.CharField(max_length=400)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True)

class NetworkAddressAddForm(ModelForm):
    class Meta:
        model = NetworkAddress
        exclude = ('parent', )

class NetworkAddressModifyForm(ModelForm):
    class Meta:
        model = NetworkAddress
        fields = ('description',)