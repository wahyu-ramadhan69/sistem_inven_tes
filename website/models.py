from django.contrib.auth.models import Permission, User
from django.db import models
from django.db.models import Model
from datetime import datetime, date


class barang(models.Model):
    nama = models.CharField(max_length=250)
    merk = models.CharField(max_length=100, null=True, blank=True)
    kode = models.CharField(max_length=20, null=True)
    tahun_perolehan = models.IntegerField()
    penguasaan = models.CharField(max_length=50)
    keterangan = models.CharField(
        max_length=250, null=True, blank=True, default='-')
    Foto = models.FileField(null=True, blank=True, default='barang.jpg')
    status = models.CharField(max_length=100, default='Tersedia')

    def __str__(self):
        return self.nama


class pegawai(models.Model):
    nama = models.CharField(max_length=250)
    nip = models.CharField(max_length=250, unique=True)
    pangkat_atau_golongan = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=250)
    Foto = models.FileField(null=True, blank=True, default='karyawan.jpg')
    tanggal_terdaftar = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nama


class peminjaman_barang(models.Model):
    nip_peminjam = models.CharField(max_length=250)
    nama_peminjam = models.CharField(max_length=250)
    nama_barang = models.CharField(max_length=250)
    status_peminjaman = models.CharField(
        max_length=100, default='Dipinjam')
    tanggal_pinjam = models.DateField(auto_now_add=True)
    id_barang = models.CharField(max_length=100)
    nama_op = models.CharField(max_length=100)
    kode_pinjam = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nama_peminjam


class pengembalian_barang(models.Model):
    id_transaksi = models.PositiveIntegerField()
    nip_pengembali = models.CharField(max_length=250)
    nama_pengembali = models.CharField(max_length=250)
    nama_barang = models.CharField(max_length=250)
    status_pengembalian = models.CharField(
        max_length=100, default='Dikembalikan')
    tanggal_kembali = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=250, null=True, default='-')
    nama_op = models.CharField(max_length=50)
    kode_pinjam = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nama_pengembali


class keranjang(models.Model):
    nama_barang = models.CharField(max_length=100)
    merk_barang = models.CharField(max_length=100)
    jenis_barang = models.CharField(max_length=100)
    id_barang = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_barang
