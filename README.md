# SumberYAML - Real WS Check + Manual Group

Versi ini memperbaiki validasi akun otomatis agar WebSocket benar-benar bekerja, bukan hanya lolos TLS atau WS Upgrade 101.

## Output

GitHub Action menghasilkan:

- `openclash_auto.yaml` untuk OpenClash/Mihomo normal.
- `openclash_android.yaml` untuk OpenClash/Clash Android tanpa rule berat.
- `akun.txt` berisi link akun otomatis yang sudah lolos real-check.
- `akun_manual.txt` berisi link dari `manual_nodes.txt`.
- `openclash_auto_report.csv` berisi laporan lengkap.
- `manual_nodes.txt` akan otomatis dinormalisasi ke server `104.17.3.81:443`.
- `last_update.txt` berisi ringkasan update.

## Perubahan penting

1. Akun otomatis dari subscription tetap disaring strict:
   - wajib `network: ws`,
   - wajib punya SNI/servername,
   - wajib lolos WebSocket Upgrade `101`,
   - wajib lolos real proxy check menggunakan Mihomo.

2. Real proxy check menjalankan Mihomo di GitHub Actions, memilih node otomatis satu per satu, lalu melakukan request ke `generate_204` melalui proxy lokal Mihomo. Node yang gagal tidak masuk 20 akun otomatis.

3. Node manual dari `manual_nodes.txt` tidak disaring dan tidak dites. Node manual tetap masuk group `MANUAL`, di luar kuota 20 akun otomatis.

4. Group `FALLBACK` dimulai dari `MANUAL`, lalu dilanjutkan node akun otomatis.

5. Nama node manual tetap memakai nama sumber/link, hanya diberi prefix `MANUAL-`.

## File manual

Isi node manual di:

```text
manual_nodes.txt
```

Contoh:

```text
vless://uuid@domain-asli.com:443?security=tls&sni=sni.domain.com&type=ws&host=sni.domain.com&path=%2Fws#SG-VIP-01
```

Saat workflow berjalan, server akan otomatis diubah menjadi:

```text
104.17.3.81:443
```

SNI, Host, path, uuid/password, dan fragment nama tetap dipertahankan.

## Pengaturan GitHub Action

Workflow berjalan otomatis setiap 6 jam:

```yaml
- cron: "0 */6 * * *"
```

Workflow juga bisa dijalankan manual dari tab **Actions > Run workflow**.

## Variabel penting

```text
MAX_NODES=20
VALIDATION_POOL_NODES=80
REAL_CHECK=true
MIHOMO_PATH=./mihomo
FORCE_WS_ONLY=true
REQUIRE_WS_UPGRADE=true
REAL_CHECK_TIMEOUT_MS=8000
HEALTH_TIMEOUT_MS=6000
```

Jika hasil akun otomatis kurang dari 20, berarti sumber publik saat itu tidak menyediakan 20 node yang benar-benar lolos WS + real proxy check. Node manual tetap tidak dihitung dalam kuota 20 otomatis.

## Cara pakai

1. Upload semua isi ZIP ke root repository GitHub.
2. Pastikan file workflow berada di:

```text
.github/workflows/update-yaml-6jam.yml
```

3. Buka **Actions > Run workflow**.
4. Setelah selesai, cek file:

```text
openclash_auto.yaml
openclash_android.yaml
akun.txt
akun_manual.txt
openclash_auto_report.csv
last_update.txt
```
