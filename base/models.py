from django.db import models

# from rest_framework.authtoken.models import Token
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.
class BaseProduct(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)


    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    def get_discount(self):
        return "%.2f" %(float(self.price) * 0.2)




# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created = False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
        