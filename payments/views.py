from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

from django.views.generic.base import TemplateView

from django.conf import settings
from braces.views import LoginRequiredMixin

from django.core.urlresolvers import reverse

class AccountPaymentView(LoginRequiredMixin, TemplateView):
    template_name = "payment.html"
    context_object_name = 'context'
    base_url = "https://escolamupi.com.br"

    if settings.DEBUG:
        base_url = "http://localhost:8000"

    def get(self, request, **kwargs):
	u = self.request.user
	
	settings.PAYPAL_DICT_MONTHLY['custom'] = "user_mail=" + u.email + "&user_id=" + str(u.id)
	settings.PAYPAL_DICT_YEARLY['custom'] = "user_mail=" + u.email + "&user_id=" + str(u.id)
	
	settings.PAYPAL_DICT_MONTHLY['notify_url'] = settings.SITE_URL + reverse('paypal-ipn')
        form_monthly = PayPalPaymentsForm(initial=settings.PAYPAL_DICT_MONTHLY)

	settings.PAYPAL_DICT_YEARLY['notify_url'] = settings.SITE_URL + reverse('paypal-ipn')
        form_yearly = PayPalPaymentsForm(initial=settings.PAYPAL_DICT_YEARLY)

        if settings.DEBUG:
		context = {
        	        "form_monthly": form_monthly.sandbox(),
                	"form_yearly": form_yearly.sandbox()
	        }
	else:
		context = {
        	        "form_monthly": form_monthly.sandbox(),
                	"form_yearly": form_yearly.sandbox()
	        }

        return self.render_to_response(context)

