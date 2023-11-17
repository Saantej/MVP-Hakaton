from regions.models import Address, Country
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    city = serializers.CharField()

    class Meta:
        model = Address
        fields = ('city', 'street', 'building_number', 'building', 'postcode')
