# Panduan Push Praktikum Modul 4 ke GitHub

**Repository:** https://github.com/Zidanes-hub/PSD-SEMESTER_4.git

---

## Step 1: Buka Terminal

Buka **PowerShell** atau **Command Prompt**, lalu masuk ke folder Praktikum Modul 4:

```powershell
cd "d:\SEMESTER 4\Signal Digital\Praktikum\Praktikum Modul 4"
```

## Step 2: Inisialisasi Git

```powershell
git init
```

## Step 3: Tambahkan Remote Repository

```powershell
git remote add origin https://github.com/Zidanes-hub/PSD-SEMESTER_4.git
```

> **Catatan:** Jika muncul error `remote origin already exists`, jalankan perintah berikut:
>
> ```powershell
> git remote set-url origin https://github.com/Zidanes-hub/PSD-SEMESTER_4.git
> ```

## Step 4: Pull Data dari Remote

Tarik data terbaru dari repository agar tidak terjadi konflik:

```powershell
git pull origin main
```

> **Catatan:** Jika branch utama menggunakan `master`, ganti `main` dengan `master`.

## Step 5: Tambahkan Semua File ke Staging

```powershell
git add .
```

## Step 6: Commit Perubahan

```powershell
git commit -m "Menambahkan Praktikum Modul 4 - Rekonstruksi Sinyal"
```

## Step 7: Push ke GitHub

```powershell
git push origin main
```

---

✅ **Selesai!** File Praktikum Modul 4 sekarang sudah ada di repository GitHub kamu.
