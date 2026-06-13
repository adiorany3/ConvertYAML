# SumberYAML OpenClash Safe Names Rule Split

Versi sederhana untuk Streamlit Online tanpa GitHub Action.

## Fungsi utama

Aplikasi ini mengambil akun publik dari subscription bawaan, hanya memakai port `443`, mengecek kompatibilitas bug server `104.17.3.81` dengan SNI/Host akun, lalu membuat YAML OpenClash/Mihomo.

## Fitur baru versi ini

1. `GLOBAL` tetap langsung memilih `AUTO-FAST`.
2. Rule dipisah menjadi grup:
   - `SOCIAL-MEDIA`
   - `YOUTUBE`
   - `EDUKASI`
   - `STREAMING`
   - `AUTO-FAST`
   - `FALLBACK`
   - `LOAD-BALANCE`
3. Iklan, tracker, privacy leak, hijacking, dan malware ringan diblokir ke `REJECT`.
4. Menggunakan `rule-providers` agar daftar rule bisa update otomatis dari sumber publik.
5. Nama akun/proxy dari subscription publik otomatis diganti menjadi format aman ASCII seperti `AKUN-001-VLESS-120MS`.
6. Semua nama proxy dibuat unik sehingga tidak bentrok di OpenClash.
7. Nama grup dibuat tanpa emoji agar lebih kompatibel dengan OpenClash lama.
8. YouTube dibuat grup sendiri, tidak digabung dengan streaming umum.
9. Edukasi dibuat grup sendiri untuk domain seperti `.edu`, `.ac.id`, Scholar, GitHub, Coursera, edX, Khan Academy, Udemy, arXiv, dan sejenisnya.

## Output

- `openclash_safe_names_rule_split.yaml`
- `openclash_safe_names_report.csv`

## Catatan OpenClash

Gunakan core OpenClash yang mendukung Clash Meta / Mihomo agar `rule-providers` format `mrs` berjalan normal.

Kalau rule-provider gagal diunduh, buka log OpenClash lalu jalankan update rule provider / restart OpenClash.

## Jalankan lokal

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy ke Streamlit Cloud

1. Upload semua file ke repository GitHub.
2. Buka Streamlit Cloud.
3. Pilih repository tersebut.
4. Main file: `streamlit_app.py`.
5. Deploy.

Tidak perlu GitHub Token dan tidak perlu GitHub Action.


## Perbaikan nama akun error

Jika nama akun dari subscription publik mengandung emoji, tanda kutip, slash, kurung, karakter tersembunyi, atau nama duplikat, aplikasi tidak memakai nama tersebut di YAML. Nama akan otomatis diganti menjadi format aman:

```text
AKUN-001-VLESS-120MS
AKUN-002-TROJAN-135MS
AKUN-003-VMESS-180MS
```

Nama asli tetap dicatat di file report CSV pada kolom `original_name`, sehingga kamu masih bisa melacak sumber akun tanpa membuat OpenClash error saat import YAML.

## Perbaikan akun tidak lengkap

Versi ini menolak akun/node yang field-nya tidak lengkap sebelum masuk proses delay dan sebelum ditulis ke YAML.

Akun akan dibuang dari YAML jika kurang salah satu field penting berikut:

- `uuid` untuk VLESS/VMess.
- `password` untuk Trojan/Shadowsocks.
- `cipher` untuk VMess/Shadowsocks.
- `servername`, `sni`, atau `Host` untuk akun TLS yang memakai bug server.
- `ws-opts.path` dan `ws-opts.headers.Host` untuk WebSocket.
- `grpc-opts.grpc-service-name` untuk gRPC.
- `http-opts.path` dan `http-opts.headers.Host` untuk HTTP/H2.
- `reality-opts.public-key` untuk Reality.
- Port selain `443`.
- Shadowsocks biasa yang tidak kompatibel dengan bug server `104.17.3.81` karena tidak punya SNI/Host.

Akun yang ditolak tetap dicatat di report CSV dengan status `incomplete` dan alasan pada kolom `reason`, tetapi tidak akan muncul di bagian `proxies` YAML.
