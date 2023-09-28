import requests
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Status
from django.contrib import messages
from django.http import JsonResponse

def indexStatus(request):
    status = Status.objects.all().order_by('-id_status')
    context = {
        'status':status
    }
    return render(request,'halaman/status/index.html',context)

def tambahStatus(request):
    return render(request,'halaman/status/tambah.html')

def prosesTambahStatus(request):
    nama_status = request.POST['nama_status']
    if nama_status == '':
        messages.error(request,'Gagal Menambahkan Status')
        return redirect('tambahStatus')
    else:
        dataStatus = Status(
        nama_status=nama_status)
        dataStatus.save()
        messages.success(request,'Berhasil Menambahkan Status')
        return redirect('indexStatus')

def editStatus(request,id_status):
    status = Status.objects.get(id_status=id_status)
    context = {
        'status':status
    }
    return render(request,'halaman/status/edit.html',context)

def prosesEditStatus(request):
    id_status = request.POST['id_status']
    nama_status = request.POST['nama_status']
    if nama_status =='':
        messages.error(request,'Gagal Mengedit Status')
        return redirect('editStatus',id_status)
    else:
        status = Status.objects.get(id_status=id_status)
        status.nama_status = nama_status
        status.save()
        messages.success(request,'Berhasil Mengedit Status')
        return redirect('indexStatus')

def prosesHapusStatus(request,id_status):
    Status.objects.get(id_status=id_status).delete()
    messages.success(request,'Berhasil Menghapus Status')
    return redirect('indexStatus')



