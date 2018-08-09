from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=200, blank=True, null=True, default=None)
    description = models.TextField(max_length=1000, blank=True, null=True, default=None)


    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImg(models.Model):

    product = models.ForeignKey(Product) # link on product object or link on cell of table in database
    img = models.ImageField(upload_to='/')
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.id

    class Meta:

        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'