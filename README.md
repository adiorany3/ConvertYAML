# SumberYAML OpenClash Compatible

Versi ini menambahkan validasi kompatibilitas sebelum hasil di-commit oleh GitHub Actions.

## Output

Workflow membuat file berikut:

- `openclash_auto.yaml` — config OpenClash/router dengan rule Lite.
- `openclash_android.yaml` — config Android/global tanpa rule-provider dan tanpa redir/tproxy.
- `akun.txt` — link akun otomatis yang lolos strict + real proxy check, server sudah `104.17.3.81:443`.
- `akun_manual.txt` — link manual dari `manual_nodes.txt`, server dinormalisasi ke `104.17.3.81:443`.
- `openclash_auto_report.csv` — laporan akun, status, WS check, dan real check.
- `compatibility_report.txt` — laporan validasi struktur YAML untuk OpenClash/Mihomo.
- `last_update.txt` — ringkasan update terakhir.

## Kompatibilitas yang dicek

Sebelum commit, generator akan memastikan:

1. YAML bisa diparse.
2. Tidak ada YAML anchor/alias seperti `&id001` atau `*id001`.
3. Nama proxy unik.
4. Nama proxy-group unik.
5. Semua isi `proxy-groups.proxies` merujuk ke proxy/group yang benar.
6. Rule `RULE-SET` hanya memakai provider yang tersedia.
7. Rule policy mengarah ke group yang tersedia.
8. `openclash_android.yaml` tidak berisi `rule-providers`, `redir-port`, atau `tproxy-port`.
9. Jika ada group `MANUAL`, group `FALLBACK` dimulai dari `MANUAL` lalu dilanjutkan node otomatis.
10. Node WS punya field dasar `ws-opts.path` dan `ws-opts.headers.Host`.

Workflow juga menjalankan:

```bash
./mihomo -t -d . -f openclash_auto.yaml
./mihomo -t -d . -f openclash_android.yaml
```

Jika config tidak valid menurut core Mihomo/OpenClash, workflow akan gagal dan tidak akan push hasil yang rusak.

## Manual nodes

Isi akun manual di:

```text
manual_nodes.txt
```

Node manual:

- tidak disaring strict,
- tidak mengurangi 20 akun otomatis,
- otomatis masuk group `MANUAL`,
- server otomatis diganti menjadi `104.17.3.81:443`,
- nama tetap dari sumber/link dan hanya ditambah prefix `MANUAL-`,
- group `FALLBACK` dimulai dari `MANUAL`, lalu node otomatis.

## Jadwal update

Workflow berjalan setiap 6 jam:

```yaml
cron: "0 */6 * * *"
```

Bisa juga dijalankan manual dari tab **Actions > Run workflow**.
