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
WARMUP_INTERVAL: "15"
WARMUP_TIMEOUT_MS: "3000"
FAST_HEALTH_TIMEOUT_MS: "3000"
FALLBACK_INTERVAL: "60"
WARMUP_NODE_LIMIT: "7"
WARMUP_MAX_DELAY_MS: "180"
WAKEUP_INTERVAL: "30"
BALANCE_INTERVAL: "90"
KEEP_ALIVE_INTERVAL: "15"
KEEP_ALIVE_IDLE: "600"
HEALTH_TIMEOUT_MS: "5000"
```

Perubahan penting:

- `WARM-UP` dibuat sebagai pool kecil berisi 7 node terbaik dengan interval 15 detik agar node utama selalu siap.
- `GLOBAL`, `PROXY`, kategori sosial, YouTube, edukasi, dan streaming menaruh `WARM-UP` di pilihan awal.
- `AUTO-FAST` tetap mengecek semua node otomatis setiap 30 detik, tetapi timeout dipangkas ke 3000 ms agar node mati tidak menahan koneksi terlalu lama.
- `FALLBACK` menjadi cadangan aman dengan interval 60 detik dan timeout 5000 ms.
- `LOAD-BALANCE` diperlambat ke 90 detik dan hanya memakai pool cepat agar router tidak terlalu berat.
- `lazy: false` tetap dipertahankan supaya health-check tetap berjalan walau group belum dipilih.
- TCP keep-alive global diaktifkan agar koneksi idle tidak cepat mati.
- Manual node dimasukkan langsung ke `FALLBACK` supaya ikut diuji aktif, tetapi tidak lagi dipaksa masuk `STREAMING-FAST` agar health-check tetap ringan.
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

## Patch STREAMING-FAST + WARM-UP

Versi ini mempertahankan `STREAMING-FAST` bertipe `url-test`, lalu menambahkan `WARM-UP` sebagai pool kecil anti-hibernasi. `STREAMING` sekarang mengutamakan `WARM-UP`, lalu `STREAMING-FAST`, `AUTO-FAST`, dan `FALLBACK`. `STREAMING-FAST` tidak lagi berisi semua node/manual; isinya dibuat lebih kecil agar health-check ringan dan ping hijau lebih stabil.


## Smart Stable v2

Versi ini memakai pemisahan pool agar koneksi lebih responsif tanpa membebani router:

- `WARM-UP`: pool utama harian agar node cepat siap.
- `WARM-UP-CF`: pool khusus Cloudflare/Worker dengan endpoint `https://cp.cloudflare.com`.
- `STREAMING-FAST`: pool streaming yang diprioritaskan dari Cloudflare/WS dan warm pool.
- `AUTO-FAST`: fast pool tier-2.
- `FALLBACK`: automatic strict nodes dulu, manual nodes belakangan.
- `openclash_lite.yaml`: mode ringan untuk router RAM/CPU kecil.
- `node_quality_report.md`: laporan tier dan kualitas node terakhir.

Rekomendasi import:

- Router normal: `openclash_auto.yaml`
- Router ringan: `openclash_lite.yaml`
- Android: `openclash_android.yaml`
