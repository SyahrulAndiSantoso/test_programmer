from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Kategori
from django.contrib import messages

def indexKategori(request):
    kategori = Kategori.objects.all().order_by('-id_kategori')
    context = {
         'kategori':kategori
    }
    return render(request,'halaman/kategori/index.html',context)

def tambahKategori(request):
        return render(request,'halaman/kategori/tambah.html')

def prosesTambahKategori(request):
        nama_kategori = request.POST['nama_kategori']
        if nama_kategori == '':
            messages.error(request,'Gagal Menambahkan Kategori')
            return redirect('tambahKategori')
        else :
            tamabahKategori = Kategori(
             nama_kategori=nama_kategori
            ) 
            tamabahKategori.save() 
            messages.success(request,'Berhasil Menambahkan Kategori')
            return redirect('indexKategori')
        

def editKategori(request,id_kategori):
      kategori = Kategori.objects.get(id_kategori=id_kategori)
      context = {
            'kategori':kategori
      }
      return render(request,'halaman/kategori/edit.html',context)

def prosesEditKategori(request):
      nama_kategori = request.POST['nama_kategori']
      id_kategori = request.POST['id_kategori']
      if nama_kategori == '':
            messages.error(request,'Gagal Mengedit Kategori')
            return redirect('editKategori',id_kategori)
      else:
            kategori = Kategori.objects.get(id_kategori=id_kategori)
            kategori.nama_kategori = nama_kategori
            kategori.save()
            messages.success(request,'Berhasil Mengedit Kategori')
            return redirect('indexKategori')

def prosesHapusKategori(request,id_kategori):
      kategori = Kategori.objects.get(id_kategori=id_kategori).delete()
      messages.success(request,'Berhasil Menghapus Kategori')
      return redirect('indexKategori')
      