# SumberYAML GitHub Action 6 Jam + akun.txt + Nama Provider Original Server

Versi ini membuat YAML OpenClash otomatis setiap 6 jam dan memberi nama node berdasarkan provider/ASN dari `original_server`, bukan dari bug IP `104.17.3.81`.

## Output otomatis

Setiap workflow berjalan, file ini akan dibuat/update:

- `openclash_auto.yaml`
- `openclash_auto_report.csv`
- `akun.txt`
- `last_update.txt`

## Format nama node

Contoh nama node:

```text
AKUN-001-VULTR-VLESS-WS-18MS
AKUN-002-MELBICOM-VLESS-WS-24MS
AKUN-003-ORACLE-VLESS-WS-35MS
AKUN-004-DIGITALOCEAN-TROJAN-WS-42MS
```

Nama provider diambil dari `original_server` dengan alur:

1. Ambil `original_server` dari akun asli.
2. Jika domain, resolve ke IP.
3. Cek RDAP/ASN dari IP tersebut.
4. Cocokkan provider seperti Vultr, Melbicom, DigitalOcean, OVH, Oracle, Akamai/Linode, Hetzner, AWS, Google, Azure, Cloudflare, dan lainnya.
5. Jika provider tidak terdeteksi, fallback ke domain original server.

> Catatan: karena `server` output di YAML tetap `104.17.3.81`, nama provider tidak diambil dari field `server`, tetapi dari `original_server` akun.

## akun.txt

File `akun.txt` berisi link akun final yang masuk YAML saja:

```text
vless://...
vmess://...
trojan://...
```

Nama fragment/link juga ikut disesuaikan dengan nama node final, misalnya:

```text
#AKUN-001-VULTR-VLESS-WS-18MS
```

## Jadwal update

Workflow berjalan otomatis setiap 6 jam:

```yaml
- cron: "0 */6 * * *"
```

GitHub Actions memakai UTC, jadi jadwalnya 00:00, 06:00, 12:00, dan 18:00 UTC.

## Cara pakai

1. Upload semua isi ZIP ke repository GitHub.
2. Pastikan file workflow berada di:

```text
.github/workflows/update-yaml-6jam.yml
```

3. Buka tab **Actions**.
4. Jalankan manual pertama kali lewat **Run workflow**.
5. Setelah selesai, cek file:

```text
openclash_auto.yaml
akun.txt
openclash_auto_report.csv
last_update.txt
```

## Jika commit gagal

Buka:

```text
Repository > Settings > Actions > General > Workflow permissions
```

Pilih:

```text
Read and write permissions
```

## Tambahan sumber subscription

Tambahkan URL subscription tambahan ke:

```text
subscription_links.txt
```

Satu URL per baris.

## Tambahan node manual

Tambahkan node manual ke:

```text
manual_nodes.txt
```

Bisa berisi:

```text
vless://...
vmess://...
trojan://...
```

## Update akun.txt memakai bug server

Pada versi ini, `akun.txt` dibuat dari akun final yang masuk YAML, tetapi alamat server pada link sudah diganti menjadi bug server:

```text
104.17.3.81:443
```

Contoh hasil:

```text
vless://uuid@104.17.3.81:443?...&sni=domain-asli&type=ws&host=domain-asli&path=/path#AKUN-001-PROVIDER-VLESS-WS-18MS
```

Field SNI/Host/path tetap memakai data akun asli agar koneksi WebSocket tetap sesuai, sedangkan alamat server mengikuti YAML OpenClash.


## Update: filter SNI/servername wajib

Versi ini menolak akun VLESS, VMess, dan Trojan jika link asli tidak memiliki field SNI/servername eksplisit.

Yang diterima sebagai SNI eksplisit:

- `sni=`
- `servername=`
- `serverName=`
- `peer=` sebagai alias SNI pada beberapa format VLESS/Trojan

Akun yang hanya punya `Host` atau hanya original server tanpa SNI/servername tidak akan dipilih, karena sering terlihat hidup saat TLS awal tetapi timeout saat health check OpenClash.

Output tetap:

- `openclash_auto.yaml`
- `openclash_auto_report.csv`
- `akun.txt`
- `last_update.txt`

Pada `akun.txt`, server tetap memakai bug server `104.17.3.81:443`, sedangkan SNI/Host/path tetap mengikuti akun yang lolos.
