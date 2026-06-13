# SumberYAML OpenClash Rule Split Auto-Fast

Versi sederhana untuk Streamlit Online tanpa GitHub Action.

## Fungsi utama

Aplikasi ini mengambil akun publik dari subscription bawaan, hanya memakai port `443`, mengecek kompatibilitas bug server `104.17.3.81` dengan SNI/Host akun, lalu membuat YAML OpenClash/Mihomo.

## Fitur baru versi ini

1. `GLOBAL` tetap langsung memilih `⚡ AUTO-FAST`.
2. Rule dipisah menjadi grup:
   - `📱 SOCIAL-MEDIA`
   - `▶️ YOUTUBE`
   - `🎓 EDUKASI`
   - `🎬 STREAMING`
   - `⚡ AUTO-FAST`
   - `🛟 FALLBACK`
   - `🔁 LOAD-BALANCE`
3. Iklan, tracker, privacy leak, hijacking, dan malware ringan diblokir ke `REJECT`.
4. Menggunakan `rule-providers` agar daftar rule bisa update otomatis dari sumber publik.
5. YouTube dibuat grup sendiri, tidak digabung dengan streaming umum.
6. Edukasi dibuat grup sendiri untuk domain seperti `.edu`, `.ac.id`, Scholar, GitHub, Coursera, edX, Khan Academy, Udemy, arXiv, dan sejenisnya.

## Output

- `openclash_rule_split_auto_fast.yaml`
- `openclash_bug_compat_report.csv`

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
