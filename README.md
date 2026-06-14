# SumberYAML Fast 10 + NekoBox Ready

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
- Group `FALLBACK` dimulai dari `MANUAL`, lalu dilanjutkan node otomatis.
- Server link di `akun.txt` dan `manual_nodes.txt` dinormalisasi ke `104.17.3.81:443`.

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
URL_TEST_TIMEOUT_MS: "6000"
NEKOBOX_TEST_TIMEOUT_MS: "8000"
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
