from django.db import models

# Create your models here.

class Status(models.Model):
    id_status=models.AutoField(primary_key=True)
    nama_status=models.CharField(blank=False, null=False)

class Kategori(models.Model):
    id_kategori=models.AutoField(primary_key=True)
    nama_kategori=models.CharField(blank=False, null=False)

class Produk(models.Model):
    id_produk=models.AutoField(primary_key=True)
    nama_produk=models.CharField(blank=False, null=False)
    harga=models.IntegerField(blank=False, null=False)
    kategori_id=models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status_id=models.ForeignKey(Status, on_delete=models.CASCADE)
