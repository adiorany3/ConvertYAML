# SumberYAML Fast 10 + URL Test

Versi ini menambahkan **URL test nyata** untuk menyaring akun otomatis yang hidup dan tidak hidup.

## Cara kerja

1. Ambil akun otomatis dari subscription publik.
2. Manual node dari `manual_nodes.txt` tetap dibaca, tetapi **tidak disaring**.
3. Akun otomatis wajib:
   - `network: ws`,
   - punya SNI/servername,
   - lolos WS Upgrade,
   - lolos URL test nyata lewat Mihomo ke `https://www.gstatic.com/generate_204`.
4. Generator berhenti setelah menemukan **10 akun otomatis yang lolos URL test**.
5. Manual node tetap masuk group `MANUAL` dan tidak mengurangi kuota 10 akun otomatis.

## Output

Workflow menghasilkan:

```text
openclash_auto.yaml
openclash_android.yaml
openclash_auto_report.csv
urltest_report.csv
akun.txt
akun_manual.txt
manual_nodes.txt
manual_nodes_skipped.txt
last_update.txt
```

## Pengaturan utama

```text
MAX_NODES=10
URLTEST_POOL_NODES=30
REQUIRE_URL_TEST=true
URL_TEST_URL=https://www.gstatic.com/generate_204
URL_TEST_EXPECTED_STATUS=204,200,301,302
URL_TEST_TIMEOUT_MS=6000
```

Kalau hasil kurang dari 10, artinya dari sumber publik saat itu belum ditemukan 10 akun otomatis yang benar-benar lolos WS + URL test. Node manual tetap masuk group `MANUAL`.

## Catatan manual_nodes.txt

Node manual:

- tidak ikut URL test,
- tidak ikut filter strict,
- server otomatis dinormalisasi ke `104.17.3.81:443`,
- nama tetap mengikuti nama sumber/link dengan prefix `MANUAL-`,
- group `FALLBACK` dimulai dari `MANUAL`, lalu lanjut ke akun otomatis.

## Cara pakai

1. Upload semua isi ZIP ke root repository.
2. Pastikan workflow berada di:

```text
.github/workflows/update-yaml-6jam.yml
```

3. Jalankan manual dari **Actions > Run workflow**.
4. Cek `urltest_report.csv` untuk melihat akun yang lolos/gagal URL test.
