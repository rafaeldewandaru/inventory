# Nama  : Rafael Bismo Dewandaru
# NPM   : 2206824666
# Kelas : PBP - F
---
# Tautan aplikasi Adaptable: https://pacilinks.adaptable.app 
---

## TUGAS 2

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.



### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual Environment digunakan dalam proyek Django untuk menciptakan lingkungan yang stabil, dapat direproduksi, dan mudah dipindahkan. Keuntungan-keuntungannya adalah sebagai berikut:

- Stabilitas Lingkungan:
Virtual environment mampu mengisolasi dependensi (paket yang diinstal) proyek Django dari sistem yang digunakan. Dengan demikian, perubahan dalam sistem atau proyek lain di sistem tidak akan memengaruhi proyek Django yang sedang dikerjakan.

- Kemampuan Reproduksi Lingkungan
Dengan virtual environment, lingkungan proyek dapat dengan mudah diperbanyak di sistem lain pada waktu yang berbeda. Hal ini memastikan bahwa proyek Django akan berjalan dengan konsisten tanpa masalah yang berkaitan dengan lingkungan yang digunakan.

- Portabilitas Lingkungan
Virtual environment memungkinkan proyek Django untuk dibagikan dengan mudah kepada orang lain tanpa adanya batasan terkait dengan dependensi atau proyek lain yang ada di sistem.

Meskipun aplikasi berbasis Django masih bisa berjalan tanpa menggunakan virtual environment, penggunaan virtual environment sangat dianjurkan. Tanpa virtual environment, ada risiko konflik dengan proyek lokal di sistem saat melakukan instalasi paket, dan juga sistem tidak akan terorganisir dengan baik serta tidak akan mengikuti praktik terbaik dalam pengembangan perangkat lunak.


### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
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
- View: Menjadi antarmuka pengguna dan fokus pada presentasi.
- ViewModel: Berfungsi sebagai penghubung antara Model dan View. ViewModel dapat mengubah data dari model sesuai dengan format atau aturan yang akan ditampilkan dalam tampilan.

Lalu perbedaan dari ketiganya adalah:
- MVT menggunakan Template untuk merender file HTML, sementara MVC dan MVVM menggunakan View untuk merender.
- MVVM biasanya terkait dengan User Interface Framework yang lebih modern dan interaktif, sementara MVC dan MVT lebih cocok digunakan dalam berbagai jenis aplikasi


## TUGAS 3

### 5. Apa perbedaan antara form POST dan form GET dalam Django?
POST dan GET, keduanya merupakan sebuah request method yang ada dalam http protocol. Secara umum GET digunakan untuk mengambil data dari server, sementara POST digunakan untuk mengirim data ke server.

GET Request:
- Bertujuan untuk mengambil data dari server untuk read-only operation
- Data digunakan dalam URL sebagai parameter yang dapat terlihat dalam browser history, bookmark, dll. sehingga kurang aman untuk data yang bersifat sensitif

POST Request:
- Bertujuan untuk mengirim data baru ke server dalam sebuah request body, dan cocok untuk penggunaan seperti mengirim form atau upload file
- Data dikirm dalam sebuah request body sehingga tidak terlihat dalam URL dan lebih aman untuk data yang bersifat sensitif


### 6. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML:
- Menyimpan data dalam sebuah tree yang kompleks, lalu syntaxnya lebih bertele-tele dan berbasis tag yang berarti data dalam XML diapit oleh tag-tag yang mendefinisikan elemen dan hierarki
- Karena format yang lebih kompleks, maka XML memakan lebih banyak space tetapi XML mendukung lebih banyak tipe data dari JSON

JSON:
- Menyimpan data dalam bentuk pasangan key-value sehingga syntaxnya lebih mudah untuk dipahami dan dibaca oleh manusia
- Format yang lebih sederhana membuat JSON memiliki ukuran file yang lebih kecil dan transmisi data yang lebih cepat

HTML:
Berbeda dengan XML dan JSON, HTML secara umum bukan digunakan untuk pertukaran data, namun sebagai bahasa markup yang digunakan untuk mengatur dan menampilkan konten dari web sehingga lebih cocok digunakan untuk merender halaman web


### 7. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Dalam aplikasi web modern, JSON lebih sering digunakan dalam pertukaran data karena:
- Menggunakan format/syntax yang ringkas dan mudah dibaca sehingga mudah dimengerti oleh manusia
- Dalam JSON, kita dapat menyusun data dalam objek, array, dan campuran keduanya, sehingga lebih fleksibel dan memungkinkan pemodelan data yang sangat dinamis.
- Mudah diintegrasikan ke dalam berbagai lingkungan dan platform karena support yang luas dari hampir semua bahasa pemrograman untuk parsing dan serializing data dalam format JSON
- Ukuran data yang lebih kecil dibandingkan data dalam format lain sehingga mengurangi beban network untuk transfer data dan pemrosesannya lebih efisien


### 8. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama saya membuat sebuah file baru pada direktori main bernama forms.py, kemudian menambahkan class ProductForm. Untuk fields saya menggunakan name, amount, dan description karena itu adalah field yang dimiliki oleh object product yang akan saya buat.

Lalu saya membuka views.py dan mengimport ProductForm yang sudah saya buat tadi untuk membuat function create_product yang dapat menambahkan product ketika data di submit. Kemudian saya juga menambahkan perintah baru pada function show_main sehingga dia bisa menampilkan product yang sudah ditambahkan.

Pada direktori main/templates, saya membuat file baru bernama create_product.html yang berfungsi sebagai tampilan untuk user ketika mereka ingin menambahkan product. Dan pada main.html juga saya tambahkan kode yang dapat menampilkan data product dalam bentuk table.

Kembali pada file views.py, saya menambahkan 4 buah function yaitu show_xml, show_json, show_xml_by_id, show_json_by_id. Masing-masing dari function tersebut berguna untuk mengembalikan data ke user dalam format yang berbeda-beda.

Setelah membuat semua function tersebut, maka kita perlu mengimportnya pada urls.py. File urls.py berfungsi agar ketika user memasukkan path, maka kita dapat direct mereka ke function yang sesuai dan menampilkan page yang sesuai. Path akan kita masukkan kedalam urlpatterns.


### 9. Screenshot dari hasil akses URL pada POSTMAN
![Screenshot 2023-09-20 111936](https://github.com/rafaeldewandaru/inventory/assets/112395930/85d099d6-b1f7-47d3-ab34-2e0011c300e2)
![Screenshot 2023-09-20 112020](https://github.com/rafaeldewandaru/inventory/assets/112395930/9d835b7d-14ba-4a91-8a4d-922a4c0cdb16)
![Screenshot 2023-09-20 112104](https://github.com/rafaeldewandaru/inventory/assets/112395930/e92066d2-a354-4bed-b1e4-59861e3d29c4)
![Screenshot 2023-09-20 112154](https://github.com/rafaeldewandaru/inventory/assets/112395930/f1a804d6-7595-4ae4-92c4-80d2359d308e)
![Screenshot 2023-09-20 112246](https://github.com/rafaeldewandaru/inventory/assets/112395930/57a3ee23-a69a-4c4f-8622-1f5658ae1bfd)

