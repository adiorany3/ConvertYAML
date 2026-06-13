# SumberYAML GitHub Action 6 Jam + Android No Rule

Versi ini membuat YAML otomatis setiap 6 jam dan sekarang menghasilkan **dua file YAML**:

1. `openclash_auto.yaml`  
   Untuk OpenClash/Mihomo biasa. Masih memakai konfigurasi rule ringan.

2. `openclash_android.yaml`  
   Untuk Clash/OpenClash for Android. File ini dibuat lebih ringan dan **tidak memakai rule-provider maupun rule kategori**.

## Output otomatis

Setiap workflow berjalan, file berikut akan dibuat/update:

```text
openclash_auto.yaml
openclash_android.yaml
openclash_auto_report.csv
akun.txt
last_update.txt
```

## Perbedaan file Android

`openclash_android.yaml` dibuat khusus agar lebih ringan untuk Android:

- Tidak ada `rule-providers`.
- Tidak ada rule YouTube, sosial media, iklan, edukasi, atau streaming.
- Tidak ada `redir-port`.
- Tidak ada `tproxy-port`.
- Mode dibuat `global`.
- Hanya memakai grup dasar:
  - `GLOBAL`
  - `AUTO-FAST`
  - `FALLBACK`
  - `DIRECT`
- Tetap memakai node yang sama dengan hasil validasi strict.
- Tetap memakai server bug `104.17.3.81` pada YAML dan `akun.txt`.
- Akun tanpa SNI/servername tetap ditolak.

## akun.txt

`akun.txt` tetap berisi link akun aktif yang masuk YAML:

```text
vless://...
vmess://...
trojan://...
```

Server pada link `akun.txt` sudah diarahkan ke:

```text
104.17.3.81:443
```

Namun SNI, Host, path, UUID/password, dan nama akun tetap mengikuti akun aktif yang lolos.

## Jadwal GitHub Action

Workflow berjalan setiap 6 jam:

```yaml
cron: "0 */6 * * *"
```

GitHub Actions menggunakan waktu UTC.

## Cara pakai

1. Upload semua isi ZIP ini ke repository GitHub.
2. Pastikan workflow berada di:

```text
.github/workflows/update-yaml-6jam.yml
```

3. Buka tab **Actions** di GitHub.
4. Jalankan manual pertama kali dengan **Run workflow**.
5. Setelah selesai, cek file:

```text
openclash_auto.yaml
openclash_android.yaml
akun.txt
openclash_auto_report.csv
last_update.txt
```

## Jika workflow tidak bisa push

Buka:

```text
Repository > Settings > Actions > General > Workflow permissions
```

Lalu pilih:

```text
Read and write permissions
```

## Catatan

`openclash_android.yaml` memang tidak memakai rules. Semua traffic diarahkan ke proxy global/auto-fast sesuai pilihan di aplikasi Android. Jika ingin routing per aplikasi atau per domain, gunakan file `openclash_auto.yaml`, bukan file Android no-rule.
