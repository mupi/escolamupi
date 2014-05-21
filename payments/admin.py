from django.contrib import admin

from .models import *

class UserPaymentsAdmin(admin.ModelAdmin):
	list_display = ('user', 'payment_date', 'payment_status',)

class PlansAdmin(admin.ModelAdmin):
	list_display = ('name',)
	fields = ('name', 'description_markdown', 'period', 'payment_methods',)

class UserPlanDataAdmin(admin.ModelAdmin):
	list_display = ('user', 'plan', 'expiration_date', 'last_payment',
			'user_status',)

class PaymentMethodsAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'data',)

admin.site.register(UserPayments, UserPaymentsAdmin)
admin.site.register(Plans, PlansAdmin)
admin.site.register(UserPlanData, UserPlanDataAdmin)
admin.site.register(PaymentMethods, PaymentMethodsAdmin)
