from django.contrib import admin

from .models import *

class UserPaymentsAdmin(admin.ModelAdmin):
	list_display = ('user', 'payment_date', 'payment_status')

class PlansAdmin(admin.ModelAdmin):
	list_display = ('name',)
	fields = ('name', 'description_markdown', 'period')

class UserPlanDataAdmin(admin.ModelAdmin):
	list_display = ('user', 'plan', 'expiration_date', 'last_payment',
			'user_status')

admin.site.register(UserPayments, UserPaymentsAdmin)
admin.site.register(Plans, PlansAdmin)
admin.site.register(UserPlanData, UserPlanDataAdmin)
