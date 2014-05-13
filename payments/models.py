from django.db import models
from accounts.models import TimtecUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from paypal.standard.ipn.signals import (payment_was_successful, subscription_signup,
						payment_was_flagged, payment_was_refunded,
						payment_was_reversed)


class UserPayments (models.Model):
	payment_id = models.CharField(_('Payment ID'), max_length=30, blank=False, unique=True)
	user = models.ForeignKey(TimtecUser)
	payment_date = models.DateTimeField(_('Payment Date'), default=timezone.now)
	payment_status = models.CharField(_('Payment Status'), max_length=30, blank=False)
	class Meta:
        	verbose_name = _('Payment')
	        verbose_name_plural = _('Payments')

class Plans(models.Model):
	name =  models.CharField(_('Plan Name'), max_length=30, blank=False)
	description =  models.TextField(max_length=300, blank=False)
	description_markdown = models.TextField(_('Plan Description'), blank=True)
	period = models.IntegerField(_('Period'), null=True)

	def save(self):
		import markdown
		self.description = markdown.markdown(self.description_markdown)
	        super(Plans, self).save() # Call the "real" save() method.

	class Meta:
        	verbose_name = _('Plan')
	        verbose_name_plural = _('Plans')

	def __unicode__(self):
		return self.name

class UserPlanData (models.Model):
	user = models.ForeignKey(TimtecUser)
	plan = models.ForeignKey(Plans, verbose_name=_("Plan"))
	expiration_date = models.DateTimeField(_('Expiration Date'), null=True)
	last_payment = models.ForeignKey(UserPayments, null=True)
	user_status = models.BooleanField()

	class Meta:
        	verbose_name = _('User Plan and Data')
	        verbose_name_plural = _('User Plans and Data')

	def __unicode__(self):
		return self.plan.name

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
	send_mail("Uepa subscription!", "=)", "contato@mupi.me", ["virgilio.santos@gmail.com"])

payment_was_successful.connect(paypal_signal_was_successful)
subscription_signup.connect(paypal_signal_subscription_signup)
#payment_was_flagged.connect(paypal_signal_was_successful)
#payment_was_refunded.connect(paypal_signal_was_successful)
#payment_was_reversed.connect(paypal_signal_was_successful)



