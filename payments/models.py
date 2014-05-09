from django.db import models
from paypal.standard.ipn.signals import (payment_was_successful, subscription_signup, 
						payment_was_flagged, payment_was_refunded, 
						payment_was_reversed)


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
#payment_was_flagged.connect(paypal_signal_was_successful)
#payment_was_refunded.connect(paypal_signal_was_successful)
#payment_was_reversed.connect(paypal_signal_was_successful)

subscription_signup.connect(paypal_signal_subscription_signup)


