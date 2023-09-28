from django.urls import path
from .viewsProduk import indexProduk,tambahProduk,prosesTambahProduk,prosesHapusProduk,editProduk,prosesEditProduk
from .viewsStatus import indexStatus,tambahStatus,prosesTambahStatus,editStatus,prosesEditStatus,prosesHapusStatus
from .viewsKategori import indexKategori,tambahKategori,prosesTambahKategori,editKategori,prosesEditKategori,prosesHapusKategori

urlpatterns = [
    path('',indexProduk, name='indexProduk'),
    path('produk/tambah',tambahProduk, name='tambahProduk'),
    path('produk/proses-tambah',prosesTambahProduk, name='prosesTambahProduk'),
    path('produk/hapus/<int:id_produk>',prosesHapusProduk,name='hapusProduk'),
    path('produk/edit/<int:id_produk>',editProduk,name='editProduk'),
    path('produk/proses-edit',prosesEditProduk,name='prosesEditProduk'),
    path('kategori',indexKategori, name='indexKategori'),
    path('kategori/tambah',tambahKategori, name='tambahKategori'),
    path('kategori/proses-tambah',prosesTambahKategori,name='prosesTambahKategori'),
    path('kategori/edit/<int:id_kategori>',editKategori,name='editKategori'),
    path('kategori/proses-edit',prosesEditKategori,name='prosesEditKategori'),
    path('kategori/hapus/<int:id_kategori>',prosesHapusKategori,name='hapusKategori'),
    path('status',indexStatus,name="indexStatus"),
    path('status/tambah',tambahStatus,name='tambahStatus'),
    path('status/proses-tambah',prosesTambahStatus,name='prosesTambahStatus'),
    path('status/edit/<int:id_status>',editStatus,name='editStatus'),
    path('status/proses-edit',prosesEditStatus,name='prosesEditStatus'),
    path('status/hapus/<int:id_status>',prosesHapusStatus,name='prosesHapusStatus'),
]