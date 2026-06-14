# SumberYAML OpenClash - Low Handshake Filter

Versi ini menambahkan filter **low handshake** untuk akun otomatis hasil subscription publik.

## Inti perubahan

- Akun otomatis hanya dipilih jika handshake rendah.
- Default filter:
  - `MAX_HANDSHAKE_MS=250`
  - `MAX_AVG_HANDSHAKE_MS=0` atau off
- Untuk node `ws`, handshake yang dipakai adalah hasil **WebSocket Upgrade 101** melalui bug server `104.17.3.81`.
- Untuk non-WS, handshake yang dipakai adalah TLS handshake ke bug server.
- Node dari `manual_nodes.txt` tetap **tidak disaring** dan tetap masuk group `MANUAL`.
- `FALLBACK` tetap dimulai dari `MANUAL`, lalu dilanjutkan akun otomatis.
- `akun.txt` berisi akun otomatis yang lolos; server pada link tetap memakai `104.17.3.81:443`.
- `akun_manual.txt` berisi akun manual dari `manual_nodes.txt`.
- `openclash_android.yaml` tetap versi ringan tanpa rule-provider/rule kategori.

## File output

Workflow akan membuat/update:

```text
openclash_auto.yaml
openclash_android.yaml
openclash_auto_report.csv
akun.txt
akun_manual.txt
manual_nodes.txt
manual_nodes_skipped.txt
compatibility_report.txt
last_update.txt
```

## Setting penting di workflow

```yaml
MAX_HANDSHAKE_MS: "250"
MAX_AVG_HANDSHAKE_MS: "0"
```

Rekomendasi:

```text
MAX_HANDSHAKE_MS 150-250 = sangat ketat/cepat, hasil bisa sedikit
MAX_HANDSHAKE_MS 300-500 = lebih longgar, peluang 20 akun lebih besar
MAX_HANDSHAKE_MS 0       = filter handshake dimatikan
```

Jika ingin handshake benar-benar rendah, gunakan:

```yaml
MAX_HANDSHAKE_MS: "200"
MAX_AVG_HANDSHAKE_MS: "350"
```

Jika ingin mengejar jumlah akun 20, gunakan:

```yaml
MAX_HANDSHAKE_MS: "500"
MAX_AVG_HANDSHAKE_MS: "0"
```

## Cara pakai

1. Upload semua isi ZIP ke repository GitHub.
2. Pastikan file workflow ada di:

```text
.github/workflows/update-yaml-6jam.yml
```

3. Buka tab **Actions**.
4. Jalankan **Run workflow**.
5. Ambil hasil dari:

```text
openclash_auto.yaml
openclash_android.yaml
akun.txt
```

## Catatan

Filter low handshake hanya berlaku untuk akun otomatis dari subscription publik. Akun manual tetap tidak disaring sesuai permintaan sebelumnya.
