from decimal import Decimal as D
from django.db import models
from django.contrib.auth.models import User

class Show(models.Model):
    name = models.CharField(help_text="Show's Name", max_length=120)
    tickets = models.IntegerField(help_text="Total Tickets")
    price = models.DecimalField(help_text="Ticket Price ", max_digits=5, decimal_places=2)
    tax = models.DecimalField(help_text="", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Show"
        verbose_name_plural = "Shows"

    def __str__(self):
        return "Show: %s" % self.name

    @property
    def get_tax_value(self):
        tax_value = (self.price / 100) * self.tax
        return tax_value

    @property
    def get_ticket_price(self):
        value_ticket = self.price + self.get_tax_value
        return value_ticket.quantize(D('0.00'))

    @property
    def get_sold_tickets(self):
        sold_tickets = self.ticket_show.filter(status=True).count()
        return sold_tickets

    @property
    def get_canceled_tickets(self):
        canceled_tickets = self.ticket_show.filter(status=False).count()
        return canceled_tickets
    
    @property
    def get_unsold_tickets(self):
        unsold_tickets = self.tickets - self.get_sold_tickets
        return unsold_tickets
    
    @property
    def get_total_revenue(self):
        total_revenue = self.get_ticket_price * self.get_sold_tickets
        return total_revenue
    
    @property
    def get_net_revenue(self):
        net_revenue = self.price * self.get_sold_tickets
        return net_revenue

    @property
    def get_tax_total(self):
        tax_total = self.price * self.get_tax_value
        return tax_total

class Ticket(models.Model):
    show = models.ForeignKey(Show, related_name="ticket_show", on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name="ticket_user", on_delete=models.PROTECT)
    status = models.BooleanField(help_text="Ticket Active/Canceled", default=True)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
    
    

    def __str__(self):
        try:
            user = None
        except:
            user = self.buyer.username
        return "Show: %s / Buyer: %s / Status: %s" % (
                                                self.show.name, 
                                                self.buyer.get_full_name(), 
                                                self.get_status
                                                )

    @property
    def get_status(self):
        return "Active" if self.status else "Canceled"


