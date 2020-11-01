from django import forms
import re

from .models import RouterInfo


class RouterForm(forms.Form):
    id = forms.IntegerField(required=False)
    sapid = forms.CharField(max_length=18)
    hostname = forms.CharField(max_length=14)
    loopback = forms.GenericIPAddressField(protocol='IPv4')
    mac_address = forms.CharField(max_length=17)

    def clean(self):
        cleaned_data = super(RouterForm, self).clean()
        mac_add = cleaned_data.get('mac_address', None)
        if not mac_add:
            return cleaned_data
        allowed = re.compile(r"""
                                (
                                    ^([0-9A-F]{2}[-]){5}([0-9A-F]{2})$
                                   |^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$
                                )
                                """,
                             re.VERBOSE | re.IGNORECASE)
        if allowed.match(mac_add) is None:
            raise forms.ValidationError('Entered Mac Address was Wrong!')
        
        sapid = cleaned_data.get('sapid', None)
        id = cleaned_data.get('id', None)
        check_sap_exist = RouterInfo.objects.filter(sapid=sapid,is_active=True).exclude(id=id)
        if check_sap_exist:
            raise forms.ValidationError('Entered Sapid is already exist!')

        hostname = cleaned_data.get('hostname', None)
        check_host_exist = RouterInfo.objects.filter(hostname=hostname,is_active=True).exclude(id=id)
        if check_host_exist:
            raise forms.ValidationError('Entered Hostname is already exist!')

        mac_address = cleaned_data.get('mac_address', None)
        check_macadd_exist = RouterInfo.objects.filter(mac_address=mac_address,is_active=True).exclude(id=id)
        if check_macadd_exist:
            raise forms.ValidationError('Entered Mac Add is already exist!')

        loopback = cleaned_data.get('loopback', None)
        check_ip_exist = RouterInfo.objects.filter(loopback=loopback,is_active=True).exclude(id=id)
        if check_ip_exist:
            raise forms.ValidationError('Entered LoopBack  is already exist!')
        return cleaned_data
