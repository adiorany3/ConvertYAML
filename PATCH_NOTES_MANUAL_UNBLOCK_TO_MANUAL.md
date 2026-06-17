# Patch Notes — Manual Unblock Domains ke Group MANUAL

Patch ini menambahkan mekanisme agar semua domain yang ditulis di `manual_unblock_domains.txt` otomatis dipaksa berjalan melalui proxy group `MANUAL`.

## Perubahan utama

- Menambahkan file `manual_unblock_domains.txt` sebagai daftar domain prioritas manual.
- Menambahkan parser domain di `sumberyaml_core.py`, `streamlit_app.py`, dan `generate_yaml.py`.
- Menyisipkan rule `DOMAIN-SUFFIX,<domain>,MANUAL` setelah rule LAN/DIRECT dan sebelum rule iklan/sosmed/streaming.
- Mendukung format:
  - `example.com`
  - `*.example.com`
  - `+.example.com`
  - `https://example.com/path`
  - `DOMAIN,sub.example.com`
  - `DOMAIN-SUFFIX,example.com`
  - `DOMAIN-KEYWORD,keyword`
  - `GEOSITE,category`
- Workflow GitHub sekarang ikut menyimpan `manual_unblock_domains.txt`.

## Cara pakai

Isi `manual_unblock_domains.txt`, contoh:

```txt
reddit.com
DOMAIN-SUFFIX,medium.com
DOMAIN,old.reddit.com
DOMAIN-KEYWORD,reddit
```

Lalu jalankan GitHub Action atau generate lokal:

```sh
python3 generate_yaml.py
```

Hasilnya, rule akan muncul di `openclash_auto.yaml` dan `openclash_lite.yaml` seperti:

```yaml
- DOMAIN-SUFFIX,reddit.com,MANUAL
- DOMAIN-SUFFIX,medium.com,MANUAL
- DOMAIN,old.reddit.com,MANUAL
- DOMAIN-KEYWORD,reddit,MANUAL
```

## Catatan

Rule LAN/private tetap `DIRECT` agar akses router dan perangkat lokal tidak terganggu.
