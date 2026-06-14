# SumberYAML GitHub Action 6 Jam + Android No Rule + Manual Group

Versi ini membuat YAML otomatis setiap 6 jam dan menambahkan node dari `manual_nodes.txt` ke group khusus `MANUAL`.

## Output

Workflow akan membuat/update file berikut:

```text
openclash_auto.yaml
openclash_android.yaml
openclash_auto_report.csv
akun.txt
akun_manual.txt
manual_nodes.txt
manual_nodes_skipped.txt
last_update.txt
```

## Perilaku node otomatis

Node dari subscription publik tetap diproses ketat:

- target utama 20 node otomatis,
- prioritas WS,
- wajib SNI/servername,
- wajib WebSocket Upgrade 101,
- `akun.txt` memakai bug server `104.17.3.81:443`,
- nama node memakai provider original server jika terdeteksi.

## Perilaku node manual

Isi `manual_nodes.txt`:

```text
vless://...
vmess://...
trojan://...
ss://...
```

Node manual:

- server pada link manual otomatis dinormalisasi ke `104.17.3.81:443` sebelum diparse,
- file `manual_nodes.txt` ikut di-update/commit jika masih berisi server original,
- SNI/Host/path/UUID/password tetap dipertahankan,
- tidak ikut proses strict SNI/WS,
- tidak dites delay,
- tidak mengurangi kuota 20 node otomatis,
- masuk ke group sendiri bernama `MANUAL`,
- tidak masuk `AUTO-FAST`, `FALLBACK`, atau `LOAD-BALANCE`,
- tetap bisa dipilih manual dari group `GLOBAL` / `PROXY`,
- disimpan terpisah ke `akun_manual.txt` dengan server `104.17.3.81:443`.

Jika ada baris manual yang formatnya tidak bisa diparse, baris tersebut dicatat di:

```text
manual_nodes_skipped.txt
```

## Android no rule

`openclash_android.yaml` dibuat ringan untuk Clash/OpenClash Android:

- tidak ada `rule-providers`,
- tidak ada rule kategori,
- tidak ada `redir-port`,
- tidak ada `tproxy-port`,
- mode `global`,
- ada group `MANUAL` untuk node dari `manual_nodes.txt`.

## Cara pakai

1. Upload semua file ZIP ke repository GitHub.
2. Pastikan workflow berada di:

```text
.github/workflows/update-yaml-6jam.yml
```

3. Isi `manual_nodes.txt` dengan akun tambahan yang ingin dimasukkan tanpa filter. Server boleh masih original; workflow akan mengubahnya ke `104.17.3.81:443`.
4. Buka tab **Actions**.
5. Jalankan **Run workflow** pertama kali.
6. Setelah itu workflow berjalan otomatis setiap 6 jam.

## Catatan penting

Manual node sengaja tidak difilter sesuai permintaan. Server manual otomatis diubah ke bug server `104.17.3.81:443`, tetapi akun tetap bisa timeout jika UUID/SNI/Host/path memang sudah mati. Jika manual node mati atau salah format, OpenClash/Clash Android bisa menampilkan timeout untuk node tersebut. Karena itu manual node dipisahkan di group `MANUAL` agar tidak mengganggu 20 node otomatis di `AUTO-FAST`.
