# SumberYAML Fast 10 + NekoBox Ready + Anti-Hibernasi

Versi ini membuat YAML OpenClash/Mihomo dan YAML ringan untuk Android, lalu menyaring akun otomatis dengan dua tahap test nyata:

1. **Mihomo URL test** untuk memastikan akun bisa dipakai di OpenClash/Mihomo.
2. **sing-box URL test** untuk memastikan akun lebih siap dipakai di NekoBox/Android.

Node dari `manual_nodes.txt` tetap **tidak disaring** dan tetap masuk group `MANUAL`.

## Output GitHub Action

Workflow akan membuat/update file berikut:

```text
openclash_auto.yaml
openclash_android.yaml
openclash_auto_report.csv
urltest_report.csv
nekobox_test_report.csv
akun.txt
akun_manual.txt
manual_nodes.txt
manual_nodes_skipped.txt
last_update.txt
```

## Perilaku utama

- Target akun otomatis: **10 node**.
- Akun otomatis wajib `network: ws`.
- Akun otomatis wajib punya `sni/servername` valid.
- Akun otomatis wajib lolos WebSocket upgrade.
- Akun otomatis wajib lolos URL test Mihomo.
- Akun otomatis wajib lolos URL test sing-box.
- Generator berhenti ketika sudah menemukan 10 akun yang bagus.
- Manual node tidak mengurangi kuota 10 akun otomatis.
- Manual node tetap masuk group `MANUAL`.
- Group `FALLBACK` sekarang memasukkan node manual satu per satu di depan node otomatis agar ikut di-health-check dan tidak mudah tertahan saat node manual/worker sedang hibernasi.
- Server link di `akun.txt` dan `manual_nodes.txt` dinormalisasi ke `104.17.3.81:443`.


## Mode responsif / anti-hibernasi

Versi ini menambahkan tuning agar node lebih cepat bangun dan tidak terlalu lama diam:

```yaml
URLTEST_INTERVAL: "30"
ANDROID_URLTEST_INTERVAL: "30"
WAKEUP_INTERVAL: "30"
BALANCE_INTERVAL: "60"
KEEP_ALIVE_INTERVAL: "15"
KEEP_ALIVE_IDLE: "600"
HEALTH_TIMEOUT_MS: "5000"
```

Perubahan penting:

- `AUTO-FAST` dan `FALLBACK` dicek setiap 30 detik.
- `LOAD-BALANCE` dicek setiap 60 detik agar tidak terlalu berat.
- `lazy: false` tetap dipertahankan supaya health-check tetap berjalan walau group belum dipilih.
- TCP keep-alive global diaktifkan agar koneksi idle tidak cepat mati.
- Manual node dimasukkan langsung ke `FALLBACK` supaya ikut diuji aktif, bukan hanya lewat group `MANUAL`.
- Workflow GitHub berjalan setiap 3 jam untuk refresh kandidat lebih sering.

## File Android

Gunakan file ini untuk OpenClash/Clash Android/NekoBox-style config sederhana:

```text
openclash_android.yaml
```

File Android dibuat tanpa:

```text
rule-providers
redir-port
tproxy-port
```

## Laporan NekoBox

Cek hasil test NekoBox/sing-box di:

```text
nekobox_test_report.csv
```

Kolom penting:

```text
name
type
network
original_server
bug_sni
mihomo_status
url_test_ms
nekobox_test_ms
nekobox_status
nekobox_ready
```

`nekobox_ready=yes` berarti akun otomatis lolos test sing-box.

## Cara pakai

1. Upload semua isi ZIP ke repository GitHub.
2. Pastikan workflow berada di:

```text
.github/workflows/update-yaml-6jam.yml
```

3. Buka tab **Actions**.
4. Jalankan **Run workflow**.
5. Tunggu sampai selesai.
6. Ambil file:

```text
openclash_auto.yaml
openclash_android.yaml
akun.txt
nekobox_test_report.csv
```

## Setting penting di workflow

```yaml
MAX_NODES: "10"
MIN_OUTPUT_NODES: "10"
URLTEST_POOL_NODES: "35"
NEKOBOX_POOL_NODES: "25"
REQUIRE_URL_TEST: "true"
REQUIRE_NEKOBOX_TEST: "true"
URL_TEST_URL: "https://www.gstatic.com/generate_204"
NEKOBOX_TEST_URL: "https://www.gstatic.com/generate_204"
URL_TEST_TIMEOUT_MS: "5000"
NEKOBOX_TEST_TIMEOUT_MS: "7000"
FORCE_WS_ONLY: "true"
REQUIRE_WS_UPGRADE: "true"
```

Jika proses terlalu lama, turunkan:

```yaml
URLTEST_POOL_NODES: "25"
NEKOBOX_POOL_NODES: "15"
CANDIDATE_MIN: "400"
```

Jika hasil node terlalu sedikit, naikkan:

```yaml
URLTEST_POOL_NODES: "50"
NEKOBOX_POOL_NODES: "35"
CANDIDATE_MIN: "900"
```

## Patch STREAMING-FAST

Versi ini menambahkan grup `STREAMING-FAST` bertipe `url-test` agar menu streaming punya health-check langsung dan lebih sering muncul ping hijau di OpenClash. Grup `STREAMING` sekarang otomatis memilih `STREAMING-FAST` di urutan pertama. `STREAMING-FAST` memakai `lazy: false`, `interval: 30`, `timeout: 5000`, dan `tolerance: 50`, serta memasukkan node manual dan node otomatis yang sudah tersedia.
