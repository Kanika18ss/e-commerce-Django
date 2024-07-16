from django import forms
from store.models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'street_address', 'apartment_number', 'building_name', 'floor_number', 
            'gate_code', 'city', 'state', 'country', 'postal_code', 'phone_number', 
            'contact_name', 'company_name', 'delivery_instructions', 'address_type', 
            'latitude', 'longitude', 'is_default', 'label'
        ]
