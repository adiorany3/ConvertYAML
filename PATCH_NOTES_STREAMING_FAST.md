# Patch Notes - STREAMING-FAST URL-Test

Perubahan:
- Menambahkan proxy group `STREAMING-FAST` bertipe `url-test`.
- `STREAMING` sekarang memilih `STREAMING-FAST` di urutan pertama.
- `GLOBAL` dan `PROXY` menampilkan `STREAMING-FAST` agar mudah dicek langsung di OpenClash.
- `STREAMING-FAST` memakai `lazy: false`, `interval: 30`, `timeout: 5000`, dan `tolerance: 50`.
- Manual node ikut dimasukkan ke `STREAMING-FAST` melalui post-processor agar node manual juga tetap hangat dan terlihat delay-nya.
- Perubahan diterapkan ke `openclash_auto.yaml`, `openclash_android.yaml`, `sumberyaml_core.py`, `streamlit_app.py`, dan `generate_yaml.py`.

Tujuan:
- Mengurangi kasus grup streaming tidak menampilkan ping hijau karena sebelumnya masih berupa `select`/nested group.
- Membuat panel OpenClash punya hasil health-check langsung untuk jalur streaming.
