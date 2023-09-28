from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'syahrul riza'
    }
    return render(request,'halaman/produk/index.html',context)