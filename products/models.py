from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    online_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductFeature(models.Model):
    name = models.CharField(max_length=254)
    product = models.ManyToManyField(
        'Product')

    def __str__(self):
        return self.name


class GiftVoucher(models.Model):
    CARD_AMOUNTS = (
        (50, '€50.00'),
        (100, '€100.00'),
        (150, '€150.00'),
        (200, '€200.00'),
        (250, '€250.00'),
        (300, '€300.00'),
        (350, '€350.00'),
        (400, '€400.00'),
    )

    category_id = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, default='Gift Voucher')
    select_amount = models.IntegerField(choices=CARD_AMOUNTS, default=0)

    def __str__(self):
        return self.name
