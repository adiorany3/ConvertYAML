# SumberYAML WS Strict 20 Alive + GitHub Action 6 Jam

Versi ini menambahkan generator otomatis untuk membuat dan memperbarui YAML OpenClash/Mihomo dari GitHub Actions setiap 6 jam.

## File penting

- `streamlit_app.py` — aplikasi Streamlit manual.
- `generate_yaml.py` — generator headless untuk GitHub Actions.
- `sumberyaml_core.py` — fungsi inti parsing, validasi, seleksi node, dan build YAML.
- `.github/workflows/update-yaml-6jam.yml` — workflow update otomatis per 6 jam.
- `openclash_auto.yaml` — output YAML otomatis setelah workflow berjalan.
- `openclash_auto_report.csv` — report hasil validasi.
- `last_update.txt` — catatan waktu update terakhir.

## Cara pakai di GitHub

1. Upload semua file/folder ini ke repository GitHub.
2. Pastikan file workflow berada di:
   ```text
   .github/workflows/update-yaml-6jam.yml
   ```
3. Buka tab **Actions** di repository.
4. Jalankan manual pertama kali dengan tombol **Run workflow**.
5. Setelah itu workflow akan berjalan otomatis setiap 6 jam.

## Jadwal

Workflow memakai cron:

```yaml
- cron: "0 */6 * * *"
```

GitHub Actions memakai zona waktu UTC, sehingga jadwalnya adalah 00:00, 06:00, 12:00, dan 18:00 UTC.

## Jika commit gagal karena permission

Buka repository GitHub:

```text
Settings > Actions > General > Workflow permissions
```

Pilih:

```text
Read and write permissions
```

Lalu simpan.

Workflow ini juga sudah memakai:

```yaml
permissions:
  contents: write
```

## Tambah sumber subscription

Masukkan link tambahan ke file:

```text
subscription_links.txt
```

Satu URL per baris. Baris yang diawali `#` akan diabaikan.

## Tambah node manual

Masukkan node manual ke file:

```text
manual_nodes.txt
```

Format yang didukung:

```text
vless://...
vmess://...
trojan://...
ss://...
```

Untuk mode WS Strict, node `ws` akan lebih diprioritaskan.

## Output untuk OpenClash

Setelah workflow berhasil, gunakan file ini di OpenClash:

```text
openclash_auto.yaml
```

Report detail ada di:

```text
openclash_auto_report.csv
```

## Default optimasi GitHub Action

```text
Output node              : 20
Target minimal hidup     : 20
WS only                  : aktif
Wajib WS Upgrade 101     : aktif
Candidate minimum        : 2500
Cadangan internal strict : 120
Health timeout OpenClash : 6000 ms
Rule mode                : Lite
```

Catatan: 20/20 tetap tidak bisa dijamin setiap waktu karena sumber akun publik bisa berubah atau mati. Generator akan mencoba mencari lebih banyak kandidat lalu hanya menulis node terbaik yang lolos validasi strict.


## akun.txt

Setiap workflow selesai berjalan, akun aktif yang masuk YAML juga disimpan ke `akun.txt` dalam format link share `vless://`, `vmess://`, atau `trojan://`. File ini ikut di-commit otomatis bersama `openclash_auto.yaml`, `openclash_auto_report.csv`, dan `last_update.txt`.
