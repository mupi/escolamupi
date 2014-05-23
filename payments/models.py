from django.db import models
from accounts.models import TimtecUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class PaymentMethods (models.Model):
    name = models.CharField(_('Payment Type Name'), max_length=30, blank=False)
    description =  models.TextField(max_length=300, blank=True)
    description_markdown = models.TextField(_('Description'), blank=True)
    data = models.TextField(max_length=500, blank=False, help_text='A dictionary with data (FIXME)')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Payment Method')
        verbose_name_plural = _('Payment Methods')

    def save(self):
        import markdown
        self.description = markdown.markdown(self.description_markdown)
        super(PaymentMethods, self).save() # Call the "real" save() method.


class UserPayments (models.Model):
    payment_id = models.CharField(_('Payment ID'), max_length=60, blank=False, unique=True)
    user = models.ForeignKey(TimtecUser)
    payment_date = models.DateTimeField(_('Payment Date'), default=timezone.now)
    payment_status = models.CharField(_('Payment Status'), max_length=30, blank=False)

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')

    def __unicode__(self):
        return str(self.payment_date)

class Plans(models.Model):
    name =  models.CharField(_('Plan Name'), max_length=30, blank=False)
    description =  models.TextField(max_length=300, blank=False)
    description_markdown = models.TextField(_('Plan Description'), blank=True)
    period = models.IntegerField(_('Period'), null=True)
    payment_methods = models.ManyToManyField(PaymentMethods)

    def save(self):
        import markdown
        self.description = markdown.markdown(self.description_markdown)
        super(Plans, self).save() # Call the "real" save() method.

    class Meta:
        verbose_name = _('Plan')
        verbose_name_plural = _('Plans')

    def __unicode__(self):
        return self.name

    def __str__(self):
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


