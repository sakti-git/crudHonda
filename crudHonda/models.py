from django.db import models


class ProductModel(models.Model):
    nama = models.CharField(max_length=30)
    transmisi = models.CharField(max_length=6)
    warna = models.CharField(max_length=20)
    harga = models.IntegerField()

    class Meta:
        db_table = "motor"
