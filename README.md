# SumberYAML Fast 10 Early Stop

Versi ini dibuat untuk mempercepat GitHub Action. Generator tidak lagi mengejar 20 node dan tidak mengetes ribuan kandidat sampai selesai. Generator akan mencari kandidat WS yang bagus, lalu berhenti setelah mendapatkan 10 node otomatis.

## Perubahan utama

- Output otomatis hanya 10 node.
- Manual node dari `manual_nodes.txt` tetap masuk group `MANUAL` dan tidak ikut penyaringan strict.
- Server manual otomatis dinormalisasi ke `104.17.3.81:443`.
- Node manual memakai nama asli sumber dengan prefix `MANUAL-`.
- `FALLBACK` dimulai dari group `MANUAL`, lalu dilanjutkan node akun otomatis.
- Node otomatis wajib WS dan wajib lolos WS Upgrade.
- Generator memakai early-stop: berhenti saat 10 kandidat bagus sudah ditemukan.
- Candidate pool diperkecil agar GitHub Action tidak lebih dari 20 menit.
- Health check memakai `https://www.gstatic.com/generate_204`.
- YAML tidak memakai anchor/alias `&id001` atau `*id001`.

## Output

- `openclash_auto.yaml`
- `openclash_android.yaml`
- `openclash_auto_report.csv`
- `akun.txt`
- `akun_manual.txt`
- `manual_nodes_skipped.txt`
- `last_update.txt`

## Setting default workflow

```text
MAX_NODES=10
MIN_OUTPUT_NODES=10
EARLY_STOP_GOOD_NODES=true
TEST_BATCH_SIZE=80
CANDIDATE_MIN=350
CANDIDATE_MULTIPLIER=35
ATTEMPTS=2
REQUIRE_SUCCESSES=1
TCP_TIMEOUT=2.0
MAX_WORKERS=64
```

Kalau masih terlalu lama, turunkan:

```text
TEST_BATCH_SIZE=50
CANDIDATE_MIN=250
CANDIDATE_MULTIPLIER=25
```

Kalau hasil 10 node sering kurang, naikkan:

```text
CANDIDATE_MIN=600
TEST_BATCH_SIZE=100
```

## Deploy

Upload isi ZIP ke root repository GitHub. Pastikan file workflow berada di:

```text
.github/workflows/update-yaml-6jam.yml
```

Lalu jalankan manual dari tab **Actions > Run workflow**.
