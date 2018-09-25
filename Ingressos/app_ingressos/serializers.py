from rest_framework import serializers
from app_ingressos.models import Show, Ticket

class TicketSerializer(serializers.ModelSerializer):
    show = serializers.SerializerMethodField()
    buyer = serializers.SerializerMethodField()
    class Meta:
        model = Ticket
        exclude = ('status',)

    def get_show(self, obj):
        return obj.show.name
    
    def get_buyer(self, obj):
        return obj.buyer.get_full_name()


class ShowSerializer(serializers.ModelSerializer):
    total_price  = serializers.SerializerMethodField()
    sold_tickets = serializers.SerializerMethodField()
    unsold_tickets = serializers.SerializerMethodField()
    
    class Meta:
        model = Show
        fields = ('__all__')

    def get_total_price(self, obj):
        return obj.get_ticket_price
    
    def get_sold_tickets(self, obj):
        return obj.get_sold_tickets

    def get_unsold_tickets(self, obj):
        return obj.get_unsold_tickets
    

class ShowFinancialSerializer(ShowSerializer):
    total_revenue = serializers.SerializerMethodField()
    tax_total = serializers.SerializerMethodField()
    net_revenue = serializers.SerializerMethodField()

    def get_total_revenue(self, obj):
        return obj.get_total_revenue
    
    def get_tax_total(self, obj):
        return obj.get_tax_total

    def get_net_revenue(self, obj):
        return obj.get_net_revenue
