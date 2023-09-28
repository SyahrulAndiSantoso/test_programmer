from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Kategori
from .models import Status
from .models import Produk
from django.contrib import messages

def indexProduk(request):
    produk = Produk.objects.select_related('kategori_id','status_id').filter(status_id__nama_status="bisa dijual").order_by('-id_produk')
    context={
        'produk':produk
    }
    return render(request,'halaman/produk/index.html',context)

def tambahProduk(request):
    kategori = Kategori.objects.all()
    status = Status.objects.all()
    context = {
        'kategori':kategori,
        'status':status
    }
    return render(request,'halaman/produk/tambah.html',context)

def prosesTambahProduk(request):
    nama_produk = request.POST['nama_produk']
    harga = request.POST['harga']
    kategori_id = request.POST['kategori_id']
    status_id = request.POST['status_id']
    if nama_produk == '':
        messages.error(request,'Gagal Menambahkan Produk')
        return redirect('tambahProduk')
    elif harga == '':
        messages.error(request,'Gagal Menambahkan Produk')
        return redirect('tambahProduk')
    elif kategori_id == '':
        messages.error(request,'Gagal Menambahkan Produk')
        return redirect('tambahProduk')
    elif status_id == '':
        messages.error(request,'Gagal Menambahkan Produk')
        return redirect('tambahProduk')
    else:
        kategori = Kategori.objects.get(id_kategori=kategori_id)
        status = Status.objects.get(id_status=status_id)
        tamabahProduk = Produk(
             nama_produk=nama_produk,
             harga=harga,
             status_id = status,
             kategori_id = kategori
            )
        tamabahProduk.save()
        messages.success(request,'Berhasil Menambahkan Produk')
        return redirect('indexProduk')

def prosesHapusProduk(request,id_produk):
    Produk.objects.get(id_produk=id_produk).delete()
    messages.success(request,'Berhasil Menghapus Produk')
    return redirect('indexProduk')

def editProduk(request,id_produk):
    produk = Produk.objects.get(id_produk=id_produk)
    kategori = Kategori.objects.all()
    status = Status.objects.all()
    context = {
        'produk':produk,
        'kategori':kategori,
        'status':status
    }
    return render(request,'halaman/produk/edit.html',context)

def prosesEditProduk(request):
    id_produk = request.POST['id_produk']
    nama_produk = request.POST['nama_produk']
    harga = request.POST['harga']
    kategori_id = request.POST['kategori_id']
    status_id = request.POST['status_id']
    if nama_produk == '':
        messages.error(request,'Gagal Mengupdate Produk')
        return redirect('tambahProduk')
    elif harga == '':
        messages.error(request,'Gagal Mengupdate Produk')
        return redirect('tambahProduk')
    elif kategori_id == '':
        messages.error(request,'Gagal Mengupdate Produk')
        return redirect('tambahProduk')
    elif status_id == '':
        messages.error(request,'Gagal Mengupdate Produk')
        return redirect('tambahProduk')
    else:
        kategori = Kategori.objects.get(id_kategori=kategori_id)
        status = Status.objects.get(id_status=status_id)
        produk = Produk.objects.get(id_produk=id_produk)
        produk.nama_produk = nama_produk
        produk.harga = harga
        produk.kategori_id = kategori
        produk.status_id = status
        produk.save() 
        messages.success(request,'Berhasil Mengupdate Produk')
        return redirect('indexProduk')