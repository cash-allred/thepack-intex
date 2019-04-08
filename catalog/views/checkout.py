from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from catalog import models as cmod 
from django import forms
from datetime import datetime
import stripe 

@view_function
def process_request(request):
    cart = request.user.get_shopping_cart()
    cart.save

    #handle form
    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        form.request = request.user.get_shopping_cart()
        if form.is_valid():
            # clean already finalize the sale
            return HttpResponseRedirect('/catalog/receipt/{}/'.format (form.sale.id) )

    return request.dmp.render('checkout.html', {
        'cart': cart,
        'form': form,
    })

class CheckoutForm(forms.Form):
    address = forms.CharField(label='Shipping Address')
    city = forms.CharField(label='Shipping City')
    state = forms.CharField(label = 'Shipping State')
    zipcode = forms.CharField(label = 'Shipping Zip')
    stripeToken = forms.CharField(widget=forms.HiddenInput())
    def clean(self):
        try:
            sale = self.request.user.get_shopping_cart()
            sale.finalize(self.cleaned_data['stripeToken'])
        except Exception as e:
            raise forms.ValidationError('Error processing payment: {}'.format(e))