# Patch Notes - Fix manual_unblock_domains re import

## Masalah
GitHub Action gagal saat menjalankan `python generate_yaml.py` dengan error:

```text
NameError: name 're' is not defined
```

Penyebabnya: fungsi parser `manual_unblock_domains.txt` memakai `re.search(...)`, tetapi `generate_yaml.py` belum mengimpor modul `re` pada level global.

## Perbaikan
- Menambahkan `import re` pada bagian import global `generate_yaml.py`.
- Parser `manual_unblock_domains.txt` sekarang bisa membaca komentar inline seperti `reddit.com # komentar`.
- Rule domain manual tetap diarahkan ke group `MANUAL`.

## Dampak
Workflow GitHub tidak lagi gagal pada tahap `_strip_inline_comment()` saat membaca `manual_unblock_domains.txt`.
