---

# 🌐 Katalog Produk Sederhana — Website Statis Berbasis Function-Based View

Selamat datang di project **Katalog Produk Sederhana**!  
Project ini bertujuan sebagai latihan dasar bagi pemula yang ingin memahami bagaimana Django bekerja — dari routing, views, hingga template HTML dengan styling sederhana.

---

## 🎯 Fitur

- ✅ Homepage (`/`)
- ✅ Halaman Daftar Produk (`/produk/`)
- ✅ Halaman Detail Produk (`/produk/<id>/`)
- ✅ Halaman Kontak (`/kontak/`)
- ✅ Menggunakan **Function-Based Views**
- ✅ Template HTML dengan styling langsung via `<style>` tag
- ✅ Tidak menggunakan database

---

## 📁 Struktur Folder

```
project/
├── main/
│   ├── templates/
│   │   └── main/
│   │       ├── homepage.html
│   │       ├── produk_list.html
│   │       ├── produk_detail.html
│   │       └── kontak.html
│   ├── views.py
│   ├── urls.py
│   └── ...
├── project/
│   ├── urls.py
│   └── settings.py
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## 🚀 Cara Menjalankan Project

Ikuti langkah-langkah ini untuk menjalankan project secara lokal:

### 1. Clone Repo
```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
```

### 3. Aktifkan Virtual Environment
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Jalankan Server
```bash
python manage.py runserver
```

Akses di browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧾 Contoh URL

| URL                 | Fungsi                        |
|---------------------|-------------------------------|
| `/`                 | Homepage                      |
| `/produk/`          | Daftar Produk                 |
| `/produk/1/`        | Detail Produk dengan ID 1     |
| `/kontak/`          | Halaman Kontak                |

---

## 📦 Requirements

Lihat pada file [`requirements.txt`](./requirements.txt):

```
Django>=4.2
```

Install dengan:

```bash
pip install -r requirements.txt
```

---

## 📄 File Tambahan

### `.gitignore`
Menjaga file lokal seperti `venv`, `.pyc`, dan cache tidak terikut dalam commit Git.

### `requirements.txt`
Mencatat dependency agar bisa diinstall dengan mudah di lingkungan lain.

---

## 🤝 Contributor

1. Naufal Aqil
2. Willy Jonathan Arsyad
3. Muhammad Khalid Al Ghifari

---

## 📫 Kontak

Jika ada pertanyaan atau masukan:
- GitHub: 
[@NaufalAqil18](https://github.com/username)
[@Giant77](https://github.com/username)
[@khalidalghifarii](https://github.com/username)

---

## 🧡 Terima Kasih

Project ini dibuat sebagai media belajar dan eksplorasi teknologi Django untuk pemula.  
Semoga bermanfaat dan selamat belajar! 🚀

---
