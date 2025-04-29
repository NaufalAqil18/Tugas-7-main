from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request) :
    #return HttpResponse("<h1>Selamat Datang di Homepage!</h1><p>Ini adalah halaman utama.</p>")
    return render(request, 'main/homepage.html')

def produk_list(request):
    #return HttpResponse("<h1>Daftar Produk</h1><p>Ini adalah daftar semua produk.</p>")
    return render(request, 'main/produk_list.html')
    
def produk_detail(request, produk_id) :
    # return HttpResponse(f"<h1>Detail Produk {produk_id}</h1><p>Ini detail untuk produk dengan ID {produk_id}.</p>")
    return render(request, 'main/produk_detail.html', {'produk_id': produk_id})

def kontak(request) :
    # return HttpResponse("<h1>Kontak Kami</h1><p>Hubungi kami di kelompok4@gmail.com</p>")
    return render(request, 'main/kontak.html')
