# Nama  : Rafael Bismo Dewandaru
# NPM   : 2206824666
# Kelas : PBP - F
---
# Tautan aplikasi Adaptable: https://pacilinks.adaptable.app 
---

<details>
<summary>TUGAS 2</summary>

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
 </details>


<details>
<summary>TUGAS 3</summary>

### 1. Apa perbedaan antara form POST dan form GET dalam Django?
POST dan GET, keduanya merupakan sebuah request method yang ada dalam http protocol. Secara umum GET digunakan untuk mengambil data dari server, sementara POST digunakan untuk mengirim data ke server.

GET Request:
- Bertujuan untuk mengambil data dari server untuk read-only operation
- Data digunakan dalam URL sebagai parameter yang dapat terlihat dalam browser history, bookmark, dll. sehingga kurang aman untuk data yang bersifat sensitif

POST Request:
- Bertujuan untuk mengirim data baru ke server dalam sebuah request body, dan cocok untuk penggunaan seperti mengirim form atau upload file
- Data dikirm dalam sebuah request body sehingga tidak terlihat dalam URL dan lebih aman untuk data yang bersifat sensitif


### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML:
- Menyimpan data dalam sebuah tree yang kompleks, lalu syntaxnya lebih bertele-tele dan berbasis tag yang berarti data dalam XML diapit oleh tag-tag yang mendefinisikan elemen dan hierarki
- Karena format yang lebih kompleks, maka XML memakan lebih banyak space tetapi XML mendukung lebih banyak tipe data dari JSON

JSON:
- Menyimpan data dalam bentuk pasangan key-value sehingga syntaxnya lebih mudah untuk dipahami dan dibaca oleh manusia
- Format yang lebih sederhana membuat JSON memiliki ukuran file yang lebih kecil dan transmisi data yang lebih cepat

HTML:
Berbeda dengan XML dan JSON, HTML secara umum bukan digunakan untuk pertukaran data, namun sebagai bahasa markup yang digunakan untuk mengatur dan menampilkan konten dari web sehingga lebih cocok digunakan untuk merender halaman web


### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Dalam aplikasi web modern, JSON lebih sering digunakan dalam pertukaran data karena:
- Menggunakan format/syntax yang ringkas dan mudah dibaca sehingga mudah dimengerti oleh manusia
- Dalam JSON, kita dapat menyusun data dalam objek, array, dan campuran keduanya, sehingga lebih fleksibel dan memungkinkan pemodelan data yang sangat dinamis.
- Mudah diintegrasikan ke dalam berbagai lingkungan dan platform karena support yang luas dari hampir semua bahasa pemrograman untuk parsing dan serializing data dalam format JSON
- Ukuran data yang lebih kecil dibandingkan data dalam format lain sehingga mengurangi beban network untuk transfer data dan pemrosesannya lebih efisien


### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama saya membuat sebuah file baru pada direktori main bernama forms.py, kemudian menambahkan class ProductForm. Untuk fields saya menggunakan name, amount, dan description karena itu adalah field yang dimiliki oleh object product yang akan saya buat.

Lalu saya membuka views.py dan mengimport ProductForm yang sudah saya buat tadi untuk membuat function create_product yang dapat menambahkan product ketika data di submit. Kemudian saya juga menambahkan perintah baru pada function show_main sehingga dia bisa menampilkan product yang sudah ditambahkan.

Pada direktori main/templates, saya membuat file baru bernama create_product.html yang berfungsi sebagai tampilan untuk user ketika mereka ingin menambahkan product. Dan pada main.html juga saya tambahkan kode yang dapat menampilkan data product dalam bentuk table.

Kembali pada file views.py, saya menambahkan 4 buah function yaitu show_xml, show_json, show_xml_by_id, show_json_by_id. Masing-masing dari function tersebut berguna untuk mengembalikan data ke user dalam format yang berbeda-beda.

Setelah membuat semua function tersebut, maka kita perlu mengimportnya pada urls.py. File urls.py berfungsi agar ketika user memasukkan path, maka kita dapat direct mereka ke function yang sesuai dan menampilkan page yang sesuai. Path akan kita masukkan kedalam urlpatterns.


### 5. Screenshot dari hasil akses URL pada POSTMAN
![Screenshot 2023-09-20 111936](https://github.com/rafaeldewandaru/inventory/assets/112395930/85d099d6-b1f7-47d3-ab34-2e0011c300e2)
![Screenshot 2023-09-20 112020](https://github.com/rafaeldewandaru/inventory/assets/112395930/9d835b7d-14ba-4a91-8a4d-922a4c0cdb16)
![Screenshot 2023-09-20 112104](https://github.com/rafaeldewandaru/inventory/assets/112395930/e92066d2-a354-4bed-b1e4-59861e3d29c4)
![Screenshot 2023-09-20 112154](https://github.com/rafaeldewandaru/inventory/assets/112395930/f1a804d6-7595-4ae4-92c4-80d2359d308e)
![Screenshot 2023-09-20 112246](https://github.com/rafaeldewandaru/inventory/assets/112395930/57a3ee23-a69a-4c4f-8622-1f5658ae1bfd)

</details>


<details>
<summary>TUGAS 4</summary>

 ### 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
 Django UserCreationForm adalah komponen bawaan Django yang menyediakan form untuk user registration dalam pengembangan aplikasi web. Form ini memudahkan pengembang untuk mengumpulkan data yang diperlukan untuk membuat akun pengguna, seperti username, password, dan informasi lainnya. UserCreationForm terintegrasi dengan baik dengan model pengguna Django, yang memungkinkan penyimpanan dan manajemen data pengguna dengan mudah. Kelebihannya mencakup kemudahan penggunaan, validasi otomatis, dan customizability. Namun, kekurangannya termasuk ketergantungan pada Django, tampilan standar yang mungkin perlu disesuaikan, serta pembatasan dalam hal fungsionalitas untuk aplikasi web yang lebih kompleks.

 ### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
 Autentikasi merujuk pada proses verifikasi pengguna (yang biasanya menggunakan username dan password), sementara otorisasi berkaitan dengan proses menentukan hak akses yang diberikan kepada pengguna setelah berhasil autentikasi. Oleh karena itu, keduanya penting karena autentikasi memverifikasi penggunanya yang ingin mengakses web django, sedangkan otorisasi memutuskan izin (apa saja yang diperbolehkan dan tidak diperbolehkan) kepada pengguna yang terautensikasi tersebut.

 ### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
 Cookies dalam konteks aplikasi web adalah file kecil yang disimpan di browser pengguna dan digunakan untuk menyimpan data sesi, seperti ID sesi atau informasi login. Selanjutnya, browser akan menyimpan cookie yang akan secara otomatis disertakan dalam setiap request berikutnya kepada situs web tersebut. Django menggunakan cookies untuk mengelola data sesi pengguna dengan aman, memungkinkan penyimpanan dan pengambilan informasi sesi seperti status login atau preferensi pengguna dengan cara yang efisien, serta menyediakan mekanisme keamanan bawaan untuk melindungi integritas data sesi.

 ### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Dalam kondisi default, cookie tidak dapat mentransfer malware atau virus karena data dalam cookie bersifat statis, namun pengguna tetap perlu waspada terhadap risiko-risiko seperti pencurian cookie yang bisa mengizinkan akses tanpa otorisasi dan modifikasi data jika cookie tidak dienkripsi. Karena cookie tersimpan di sisi client, keamanannya sangat bergantung pada aktivitas pengguna, yang juga berarti informasi sensitif harus dihindari dari tampilan cookie seperti password karena cookie dapat dilihat, disalin, dan ditiru dengan mudah.

 ### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama saya mengaktifkan virtual environment, kemudian import semua library yang diperlukan pada views.py
Kemudian saya menambahkan ketiga functions berikut

Function untuk register user baru
~~~
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
~~~
dan menambahkan file html baru bernama register.html yang ditampilkan ke user

Function agar user yang sudah register dapat login
~~~
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
~~~
dan menambahkan file html baru bernama login.html yang ditampilkan ke user

Function agar user yang sedang login dapat logout
~~~
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
</details>
~~~
dan menambahkan kode html berikut pada main.html untuk tombol logout
~~~
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
~~~

Lalu mengimport semua function yang sudah saya buat tadi ke urls.py dan menambahkan path seperti berikut
~~~
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
~~~

Saya juga menambahkan kode berikut pada function show_main agar tidak error saat tidak ada cookie
~~~
if 'last_login' in request.COOKIES:
    last_login = request.COOKIES['last_login']
else:
    last_login = 'N/A'
~~~

Kemudian saya mengimport user di file models.py dan menambahkan kode berikut untuk menghubungkan model products dengan user

Pada class products menjadi seperti berikut
~~~
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
~~~

Lalu fungsi create_product menjadi seperti berikut
~~~
def create_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
~~~



Untuk bagian bonus saya menambahkan ketiga function berikut

Function untuk menambahkan jumlah dari suatu product
~~~
def plus_product_amount(request, id):
    product = Product.objects.get(id=id)
    product.amount += 1
    product.save()
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response
~~~

Function untuk mengurangi jumlah dari suatu product
~~~
def minus_product_amount(request, id):
    product = Product.objects.get(id=id)
    if (product.amount > 0):
        product.amount -= 1
        product.save()
    else :
        messages.info(request, f'Jumlah {product.name} sudah bernilai 0!')
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response
~~~

Function untuk menghilangkan suatu product sepenuhnya
~~~
def remove_product(request, id):
    Product.objects.filter(pk=id).delete()
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response
~~~

Import function yang sudah dibuat pada urls.py lalu menambahkan path berikut
~~~
path('plus_product_amount/<int:id>', plus_product_amount, name='plus_product_amount'),
path('minus_product_amount/<int:id>', minus_product_amount, name='minus_product_amount'),
path('remove_product/<int:id>', remove_product, name='remove_product'),
~~~

Tambahkan kode berikut pada main.html untuk menunjukkan buttons yang akan menjalankan function-function yang sudah dibuat
~~~
<td class="d-flex align-items-center">
    <form method="post" action="{% url 'main:plus_product_amount' product.id %}">
        {% csrf_token %}
        <button class="btn btn-primary mx-1">+</button>
    </form>
    <form method="post" action="{% url 'main:minus_product_amount' product.id %}">
        {% csrf_token %}
        <button class="btn btn-primary mx-1">-</button>
    </form>
    <form method="post" action="{% url 'main:remove_product' product.id %}">
        {% csrf_token %}
        <button class="btn btn-primary mx-1">Delete</button>
    </form>
</td>
~~~

</details>

<details>
<summary>TUGAS 5</summary>

### 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Element Selector
Digunakan untuk memilih semua elemen HTML dengan jenis tertentu, misalnya p, h1, div, dll. Ini adalah selector paling umum dan sederhana. Biasanya digunakan ketika ingin mengatur gaya untuk semua elemen dengan jenis yang sama di seluruh halaman web.
~~~
p {
    font-size: 16px;
}
~~~

Class Selector
Digunakan untuk memilih elemen berdasarkan nilai atribut class yang diberikan kepada mereka. Selector kelas digunakan ketika ingin mengatur gaya untuk sekelompok elemen yang memiliki karakteristik atau fungsi yang serupa.
~~~
<p class="highlight">Ini adalah teks yang di-highlight.</p>
~~~

~~~
.highlight {
    background-color: yellow;
}
~~~

ID Selector
Digunakan untuk memilih elemen berdasarkan nilai atribut id. Setiap ID harus unik di seluruh halaman, sehingga selector ini cocok untuk mengidentifikasi elemen tertentu. Berguna ketika kita ingin mengatur kaya kepada elemen tertentu dengan id unik.
~~~
<div id="header">Ini adalah header.</div>
~~~

~~~
#header {
    font-size: 24px;
    background-color: #333;
    color: white;
}
~~~

Descendant Selector
Memungkinkan kita untuk memilih elemen yang merupakan turunan atau anak dari elemen lain. Ini berguna untuk mengatur gaya elemen dalam konteks tertentu seperti sebuah div tertentu
~~~
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>
~~~

~~~
ul li {
    list-style-type: square;
}
~~~

Pseudo-class Selector
Selector pseudo-class digunakan untuk menggabungkan gaya ke elemen berdasarkan keadaan atau aksi tertentu, seperti saat elemen sedang dihover atau aktif sebagai respon terhadap interaksi pengguna.
~~~
a:hover {
    text-decoration: underline;
}
~~~

### 2. Jelaskan HTML5 Tag yang kamu ketahui.
~~~
<td> Berguna untuk membuat sel dalam sebuah tabel HTML.
<tr> Digunakan untuk membuat baris dalam tabel.
<th> Membuat sel header dalam tabel, biasanya digunakan untuk judul kolom.
<style> Digunakan untuk menyertakan informasi gaya (CSS) dalam dokumen HTML.
<canvas> merupakan elemen yang digunakan untuk menciptakan gambar, grafik, dan animasi melalui penggunaan JavaScript.
<video> adalah elemen yang berguna untuk menampilkan video di dalam laman web.
<nav> digunakan untuk membuat bagian yang berfungsi sebagai navigasi untuk situs web.
<audio> adalah elemen yang memungkinkan kita untuk menampilkan file audio di dalam halaman web.
<img> adalah elemen yang digunakan untuk menampilkan gambar pada halaman web.
<a> berguna untuk membuat tautan atau hyperlink ke laman web lain, file, dan sumber daya lainnya.
~~~

### 3. Jelaskan perbedaan antara margin dan padding.
Margin
Ruang yang terletak di luar batas elemen. Margin digunakan untuk menambahkan ruang di antara elemen dengan elemen lain di sekitarnya dan tidak memiliki latar belakang atau warna (area kosong di sekitar elemen).
Jika dua elemen memiliki margin yang saling bersentuhan, maka margin tersebut tidak akan digabungkan (menggunakan margin-collapse), tetapi margin yang lebih besar akan diambil sebagai jarak antara keduanya.
~~~
.box {
    margin: 10px;
}
~~~
Dalam contoh di atas, elemen dengan kelas "box" akan memiliki margin 10 piksel di sekelilingnya.


Padding
Ruang yang terletak di dalam batas elemen, di antara batas elemen dan kontennya. Padding digunakan untuk menambahkan ruang di antara konten elemen dan batasnya sendiri, kita dapat memberikan latar belakang atau warna pada padding, sehingga padding adalah area yang dapat dilihat.
~~~
.box {
    padding: 10px;
}
~~~


### 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Tailwind CSS adalah framework CSS "utility-first" yang memberikan kelas-kelas utilitas yang bisa langsung digunakan untuk mengatur gaya elemen. Ini memberikan tingkat kustomisasi yang tinggi.
Tailwind CSS sebaiknya digunakan ketika:
- kita ingin tingkat kustomisasi yang tinggi dan kontrol penuh atas tampilan elemen.
- kita ingin desain yang unik dan tidak konvensional.
- kita ingin menghindari pembengkakan ukuran file CSS.

Bootstrap adalah framework CSS yang menyediakan komponen dan gaya prasetel yang siap pakai, cocok untuk pengembangan cepat dengan tampilan konsisten
Bootstrap sebaiknya digunakan ketika:
- Proyek memerlukan pembuatan cepat dan tampilan konsisten.
- Terbatas waktu dalam pengembangan.


### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Saya membuat 5 file css baru yang digunakan untuk styling halaman login, reigister, main, edit_product, dan create_product

File login.css
~~~
/* static/css/login.css */

.login {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f7f7f7;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.login h1 {
    text-align: center;
    margin-bottom: 20px;
}

form {
    margin-top: 20px;
}

form table {
    width: 100%;
}

form table tr td {
    padding: 10px;
}

.form-control {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.btn.login_btn {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.btn.login_btn:hover {
    background-color: #0056b3;
}

ul {
    list-style: none;
    padding: 0;
}

ul li {
    color: #ff0000;
}
~~~

File register.css
~~~
/* static/css/register.css */

.login {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f7f7f7;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.login h1 {
    text-align: center;
    margin-bottom: 20px;
}

form {
    margin-top: 20px;
}

form table {
    width: 100%;
}

form table tr td {
    padding: 10px;
}

form input[type="text"],
form input[type="password"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form input[type="submit"] {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form input[type="submit"]:hover {
    background-color: #0056b3;
}

ul {
    list-style: none;
    padding: 0;
}

ul li {
    color: #ff0000;
}
~~~

File main.css
~~~
/* static/css/main.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

h1 {
    text-align: center;
    margin-top: 20px;
}

h5 {
    font-size: 16px;
    margin-top: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

table th, table td {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #ccc;
}

table th {
    background-color: #007bff;
    color: #fff;
}

table td {
    background-color: #fff;
}

table tr:last-child td {
    background-color: #becddc;
    color: #160323;
    font-weight: 500;
  }

.d-flex {
    display: flex;
    align-items: center;
}

.btn {
    padding: 5px 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.btn-primary {
    background-color: #007bff;
}

.btn-primary:hover {
    background-color: #0056b3;
}

a button {
    text-decoration: none;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 5px 10px;
    cursor: pointer;
    margin-left: 5px;
}

a button:hover {
    background-color: #0056b3;
}

button {
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 5px 10px;
    cursor: pointer;
    margin-top: 10px;
}

button:hover {
    background-color: #0056b3;
}
~~~

File edit_product.css
~~~
/* static/css/edit_product.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

h1 {
    text-align: center;
    margin-top: 20px;
}

form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

table {
    width: 100%;
}

table tr td {
    padding: 10px;
}

input[type="text"],
input[type="number"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

input[type="submit"] {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #0056b3;
}

~~~

File create_product.css
~~~
/* static/css/create_product.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

h1 {
    text-align: center;
    margin-top: 20px;
}

form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

table {
    width: 100%;
}

table tr td {
    padding: 10px;
}

input[type="text"],
input[type="number"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

input[type="submit"] {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #0056b3;
}
~~~

Kemudian di setiap template html saya tambahkan kode berikut agar mengimplementasi css yang sudah saya buat
~~~
{% block meta %}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'css/nama_file.css' %}">
    <title>Judul halaman</title>
{% endblock meta %}
~~~

 </details>