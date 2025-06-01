from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    # Example of a read-only computed field
    total_bookings = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']  # adjust as per your model fields

    def get_total_bookings(self, obj):
        # Return count of bookings related to this listing
        return obj.booking_set.count()

    def validate_price(self, value):
        # Example custom validation: price must be positive
        if value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value


class BookingSerializer(serializers.ModelSerializer):
    listing_detail = ListingSerializer(source='listing', read_only=True)  # nested listing data in booking

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        # Example cross-field validation: end_date > start_date
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data
