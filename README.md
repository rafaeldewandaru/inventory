# # Nama  : Rafael Bismo Dewandaru
# NPM   : 2206824666
# Kelas : PBP - F
---
# Tautan aplikasi Adaptable: https://pacilinks.adaptable.app 
-- 

# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, saya membuat sebuah lokal direktori bernama inventory yang kemudian saya melakukan semua steps dalam tutorial untuk menyusun project tersebut, lalu menginstall virtual environment dan mengaktifkannya untuk direktori yang sedang saya kerjakan, kemudian setelah semua setup awal selesai, barulah saya melakukan git init dan membuat repository baru dalam GitHub dengan nama yang sama dengan project saya, lalu menghubungkannya dan melakukan git add commit push.

Kemudian, saya membuat direktori di dalam 'main' dengan nama 'templates' dan membuat file 'main.html' sebagai file yang dapat dilihat oleh user, dan melakukan routing pada proyek dengan menambahkan aplikasi 'main' pada 'settings.py' pada list INSTALLED_APPS

Saya melakukan perubahan pada 'models.py' yang ada di direktori 'main' yaitu :
~~~
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=256)
    amount = models.IntegerField()
    description = models.TextField()
~~~

dan tidak lupa saya melakukan migration agar model beserta atributesnya tersimpan di dalam database
(NOTE: karena keterbatasan waktu maka saya hanya melakukan bare minimum untuk bagian ini, tentu saja nanti akan saya adjust untuk tugas-tugas kemudian)

Lalu  saya mengubah isi dari 'views.py' akan membuat fungsi show_main yang menunjukan data kepada 'main.html' sebagai berikut :
~~~
from django.shortcuts import render

def show_main(request):
    context = {
        'name' : "Rafael Bismo Dewandaru,
        'class' : "PBP F"
    }
    return render(request, "main.html", context)
~~~

Dengan fungsi ini, maka ketika user menggunakan variabel berupa 'name' atau 'class' pada 'main.html' akan diubah menjadi value dari keys tersebut yang ada di dictionary context. 

Terakhir, saya membuat 'urls.py' pada direktori 'main' sehingga dapat memetakan fungsi pada 'views.py' 

# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.



# 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual Environment digunakan dalam proyek Django untuk menciptakan lingkungan yang stabil, dapat direproduksi, dan mudah dipindahkan. Keuntungan-keuntungannya adalah sebagai berikut:

- Stabilitas Lingkungan:
Virtual environment mampu mengisolasi dependensi (paket yang diinstal) proyek Django dari sistem yang digunakan. Dengan demikian, perubahan dalam sistem atau proyek lain di sistem tidak akan memengaruhi proyek Django yang sedang dikerjakan.

- Kemampuan Reproduksi Lingkungan
Dengan virtual environment, lingkungan proyek dapat dengan mudah diperbanyak di sistem lain pada waktu yang berbeda. Hal ini memastikan bahwa proyek Django akan berjalan dengan konsisten tanpa masalah yang berkaitan dengan lingkungan yang digunakan.

- Portabilitas Lingkungan
Virtual environment memungkinkan proyek Django untuk dibagikan dengan mudah kepada orang lain tanpa adanya batasan terkait dengan dependensi atau proyek lain yang ada di sistem.

Meskipun aplikasi berbasis Django masih bisa berjalan tanpa menggunakan virtual environment, penggunaan virtual environment sangat dianjurkan. Tanpa virtual environment, ada risiko konflik dengan proyek lokal di sistem saat melakukan instalasi paket, dan juga sistem tidak akan terorganisir dengan baik serta tidak akan mengikuti praktik terbaik dalam pengembangan perangkat lunak.


# 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC (Model-View-Controller):
Pada pola arsitektur MVC, ada pemisahan yang jelas antara komponen-komponen yang memudahkan pengembang dalam pengelolaan dan pengujian masing-masing komponen. Perubahan pada model atau tampilan tidak akan saling memengaruhi karena perubahannya akan melalui kontrol. MVC umumnya digunakan dalam aplikasi web dan desktop.
- Model: Bertanggung jawab atas representasi data dan logika bisnis aplikasi, termasuk pengambilan, pengelolaan, dan penyimpanan data.
- View: Menjadi antarmuka pengguna dan bertugas menampilkan data dari model serta menerima input dari pengguna.
- Controller: Menghubungkan model dan view, berperan dalam menangani input, memprosesnya, dan memperbarui model dan tampilan.

MVT (Model-View-Template):
Pada pola arsitektur MVT, terdapat pemisahan yang jelas antara logika bisnis (Model), antarmuka pengguna (View), dan logika presentasi (Template). Biasanya digunakan dalam kerangka kerja web seperti Django.
- Model: Merepresentasikan data dan logika bisnis aplikasi.
- View: Menjadi antarmuka pengguna dan fokus pada tampilan.
- Template: Bagian ini adalah ciri khas MVT. Template digunakan untuk mengontrol tampilan dari Model ke View.

MVVM (Model-View-ViewModel):
MVVM bertujuan untuk menyederhanakan hubungan antara Model dan View sehingga aplikasi memiliki antarmuka pengguna yang lebih responsif dan dinamis, seperti yang biasa ditemui dalam aplikasi ponsel dan desktop.
- Model: Bertanggung jawab atas representasi data dan logika bisnis aplikasi.
-- View: Menjadi antarmuka pengguna dan fokus pada presentasi.
- ViewModel: Berfungsi sebagai penghubung antara Model dan View. ViewModel dapat mengubah data dari model sesuai dengan format atau aturan yang akan ditampilkan dalam tampilan.

Lalu perbedaan dari ketiganya adalah:
- MVT menggunakan Template untuk merender file HTML, sementara MVC dan MVVM menggunakan View untuk merender.
- MVVM biasanya terkait dengan User Interface Framework yang lebih modern dan interaktif, sementara MVC dan MVT lebih cocok digunakan dalam berbagai jenis aplikasi