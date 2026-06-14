# SumberYAML - Handshake Strict

Versi ini dibuat untuk mengurangi akun otomatis yang gagal handshaking saat dites di OpenClash.

## Perubahan utama

- Node otomatis wajib `network: ws`.
- Node otomatis wajib punya `sni/servername`.
- Node otomatis wajib lolos WS Upgrade 101 beberapa kali.
- Default `ATTEMPTS=5` dan `REQUIRE_SUCCESSES=4`.
- Filter handshake rendah:
  - `MAX_HANDSHAKE_MS=250`
  - `MAX_AVG_HANDSHAKE_MS=350`
  - `MAX_JITTER_MS=120`
- Real-check Mihomo tidak hanya 1 kali:
  - `REAL_CHECK_ATTEMPTS=3`
  - `REAL_CHECK_REQUIRE_SUCCESSES=2`
- Node manual dari `manual_nodes.txt` tetap tidak disaring dan tetap masuk group `MANUAL`.
- Server manual tetap dinormalisasi menjadi `104.17.3.81:443`.
- Group `FALLBACK` dimulai dari `MANUAL`, lalu node otomatis.

## Output

- `openclash_auto.yaml`
- `openclash_android.yaml`
- `akun.txt`
- `akun_manual.txt`
- `openclash_auto_report.csv`
- `compatibility_report.txt`
- `last_update.txt`

## Catatan

Jika node otomatis yang lolos kurang dari 20, berarti sumber publik saat itu belum menyediakan 20 akun yang stabil menurut filter strict. Lebih baik hasil sedikit tetapi benar-benar bisa handshake daripada 20 akun tetapi banyak timeout.
