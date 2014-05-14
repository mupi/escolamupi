from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.conf import settings

from paypal.standard.forms import PayPalPaymentsForm
from braces.views import LoginRequiredMixin

from .models import (Plans, UserPlanData)
from accounts.models import TimtecUser

from django.forms import ModelForm

from paypal.standard.ipn.signals import (payment_was_successful, subscription_signup,
						payment_was_flagged, payment_was_refunded,
						payment_was_reversed)
from django.core.mail import send_mail


class AccountPaymentView(LoginRequiredMixin, TemplateView):
	template_name = "payment.html"
	context_object_name = 'context'
	base_url = "https://escolamupi.com.br"

	if settings.DEBUG:
		base_url = "http://localhost:8000"

	def get(self, request, **kwargs):
		# Se chegou aqui, o cara tem plano, entao, vamo renderizar o que ele
		# pode usar pra pagar:
		# Get all possible providers
		# Create forms for each provider
		# Render to response
		return super(AccountPaymentView,
				self).get(request, **kwargs)

	def dispatch(self, *args, **kwargs):
		from django.shortcuts import redirect
		try:
			upd = UserPlanData.objects.get(user_id=self.request.user.id)
		except:
			return redirect('/accounts/plans', *args, **kwargs)
		else:
			if upd.user_status:
				return redirect('/my-courses', *args, **kwargs)
			else:
				return super(AccountPaymentView,
						self).dispatch(*args, **kwargs)


class PlansView(LoginRequiredMixin, CreateView):
	template_name = "plans.html"
	model = UserPlanData
	fields = ['plan']
	success_url = '/accounts/payment'

	def get_context_data(self, **kwargs):
		context = super(PlansView, self).get_context_data(**kwargs)
		plans = Plans.objects.all()
		context['plans'] = plans
		return context

	def form_valid(self, form):
		from datetime import datetime
		import time

		dt = datetime.now()
		p = Plans.objects.get(id=form.data["plan"])
		dt = datetime.fromtimestamp(int(time.mktime(dt.timetuple()))
						+ p.period)
		form.instance.user_id = self.request.user.id
		form.instance.expiration_date = dt
		form.instance.user_status = False

		return super(PlansView, self).form_valid(form)

	def dispatch(self, *args, **kwargs):
		try:
			upd = UserPlanData.objects.get(user_id=self.request.user.id)
		except:
			pass
		else:
			from django.shortcuts import redirect
			if upd.user_status:
				return redirect('/my-courses', *args, **kwargs)
			else:
				return redirect('/accounts/payment', *args, **kwargs)

		return super(PlansView, self).dispatch(*args, **kwargs)

def paypal_signal_was_successful(sender, **kwargs):
	# Verify if the message is from paypal
	# https://www.paypal.com/cgi-bin/webscr?cmd=_notify-validate&mc_gross=19.95&protection_eligibility=Eligible
	# if yes, it will return VERIFIED

	# Verify if the message does not exist already txn_id = 61E67681CH3238416

	send_mail("Uepa", "=)", "contato@mupi.me", ["virgilio.santos@gmail.com"])
	from urlparse import parse_qs
	custom = parse_qs(sender.custom)
	print custom
 	print sender.txn_type + " -- " + custom['user_id'][0] + " -- " + custom['user_mail'][0]
	user = TimtecUser.objects.get(id=custom['user_id'][0])
	print user.email + "--" + custom['user_mail'][0]
	if sender.payment_status == "Completed":
		user.is_staff = True
		user.save()


def paypal_signal_subscription_signup(sender, **kwargs):
	print 'oe'
	send_mail("Uepa subscription!", "=)", "contato@mupi.me", ["virgilio.santos@gmail.com"])

payment_was_successful.connect(paypal_signal_was_successful)
subscription_signup.connect(paypal_signal_subscription_signup)
payment_was_flagged.connect(paypal_signal_was_successful)
#payment_was_refunded.connect(paypal_signal_was_successful)
#payment_was_reversed.connect(paypal_signal_was_successful)


def get_old(self, request, **kwargs):
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

