# ConvertYAML Smart Stable AutoPilot

ConvertYAML adalah project untuk membuat konfigurasi **OpenClash/Mihomo** dan konfigurasi ringan untuk Android/NekoBox dari kumpulan akun/proxy. Versi ini sudah dilengkapi mode **Smart Stable**, **AutoPilot Self-Healing**, dan **Router ↔ GitHub Sync** agar koneksi lebih stabil, responsif, dan otomatis.

Fokus utama project ini:

- Mengambil dan menyaring node otomatis.
- Menghasilkan YAML OpenClash yang siap import.
- Membuat pool node cepat dan stabil seperti `WARM-UP`, `WARM-UP-CF`, `AUTO-FAST`, `STREAMING-FAST`, dan `FALLBACK`.
- Mengurangi waktu tunggu saat node hibernasi.
- Menjalankan AutoPilot di OpenWrt untuk memilih jalur sehat otomatis.
- Membuat OpenWrt dan GitHub saling mengisi: GitHub generate config, router mengirim feedback, router pull config terbaru, dan rollback otomatis jika config gagal.

---

## 1. Output utama

Setelah workflow GitHub selesai, project akan menghasilkan/update file berikut:

```text
openclash_auto.yaml                 # Config utama OpenClash/Mihomo, performa penuh
openclash_lite.yaml                 # Config ringan untuk router RAM/CPU kecil
openclash_android.yaml              # Config ringan untuk Android/NekoBox-style
openclash_safe_names_rule_split.yaml # Config kompatibilitas/aman
openclash_auto_report.csv           # Laporan node output
urltest_report.csv                  # Laporan hasil URL test Mihomo
nekobox_test_report.csv             # Laporan kompatibilitas sing-box/NekoBox
node_quality_report.md              # Ringkasan tier/kualitas node
akun.txt                            # Link akun otomatis hasil generate
akun_manual.txt                     # Link akun manual
manual_nodes.txt                    # Input node manual
manual_nodes_skipped.txt            # Node manual yang dilewati
compatibility_report.txt            # Laporan kompatibilitas
last_update.txt                     # Stempel waktu update terakhir
router_feedback/                    # Feedback router OpenWrt ke GitHub
```

Rekomendasi pemakaian:

```text
Router normal        : openclash_auto.yaml
Router spek ringan   : openclash_lite.yaml
Android/NekoBox      : openclash_android.yaml
Cadangan/kompatibel  : openclash_safe_names_rule_split.yaml
```

---

## 2. Fitur utama

### 2.1 Smart Stable YAML

Config dibuat dengan beberapa proxy group khusus:

```text
WARM-UP          = pool kecil node harian yang selalu dipanaskan
WARM-UP-CF       = pool Cloudflare/Worker dengan endpoint Cloudflare
AUTO-FAST        = fast pool tier-2
STREAMING-FAST   = pool streaming cepat
FALLBACK         = jalur cadangan otomatis
LOAD-BALANCE     = untuk browsing/download, dibuat sticky agar lebih stabil
MANUAL           = node manual dari manual_nodes.txt
GLOBAL/PROXY     = selector utama
```

Tujuannya bukan membuat semua node dicek terlalu agresif, tetapi membuat node terbaik tetap siap pakai dan node cadangan tetap tersedia tanpa membebani router.

### 2.2 Anti-hibernasi node

Tuning penting yang digunakan:

```text
WARMUP_INTERVAL           = 15 detik
WARMUP_TIMEOUT_MS         = 3000 ms
CF_WARMUP_INTERVAL        = 20 detik
CF_WARMUP_TIMEOUT_MS      = 3000 ms
FAST_HEALTH_TIMEOUT_MS    = 3000 ms
FALLBACK_INTERVAL         = 60 detik
BALANCE_INTERVAL          = 90 detik
KEEP_ALIVE_INTERVAL       = 15 detik
KEEP_ALIVE_IDLE           = 600 detik
HEALTH_TIMEOUT_MS         = 5000 ms
```

`WARM-UP` dibuat kecil agar node utama tetap hidup tanpa membuat semua node gratis terkena health-check berlebihan.

### 2.3 AutoPilot Self-Healing

AutoPilot adalah script runtime di OpenWrt yang mengakses Mihomo/OpenClash External Controller. Ia akan:

- Mengecek group utama secara berkala.
- Memilih group paling sehat.
- Memindahkan selector seperti `GLOBAL`, `PROXY`, `STREAMING`, `SOCIAL-MEDIA`, `YOUTUBE`, dan `EDUKASI`.
- Memberi cooldown pada group yang gagal berulang.
- Menutup koneksi lama saat pindah jalur jika opsi `--close-connections` aktif.
- Membantu mengurangi kasus node sudah mati tetapi masih dipilih.

File penting:

```text
scripts/mihomo_autopilot.py
scripts/install_autopilot_openwrt.sh
scripts/run_autopilot_once.sh
README_AUTOPILOT.md
```

### 2.4 Router ↔ GitHub Sync

Fitur ini membuat OpenWrt dan GitHub saling mengisi:

```text
GitHub → OpenWrt
Generate config baru → router pull config → backup → validasi → restart OpenClash → rollback jika gagal

OpenWrt → GitHub
Router baca status Mihomo → kirim feedback JSON → trigger workflow rebuild → GitHub generate ulang
```

File penting:

```text
scripts/openwrt_pull_config.sh
scripts/openwrt_report_status.py
scripts/trigger_github_rebuild.sh
scripts/rollback_openclash_config.sh
scripts/install_router_github_sync_openwrt.sh
openwrt_github.env.example
.github/workflows/router-feedback.yml
README_ROUTER_GITHUB_SYNC.md
```

---

## 3. Struktur folder

```text
ConvertYAML-main/
├─ .github/workflows/
│  ├─ update-yaml-6jam.yml
│  └─ router-feedback.yml
├─ router_feedback/
│  └─ .gitkeep
├─ scripts/
│  ├─ mihomo_autopilot.py
│  ├─ install_autopilot_openwrt.sh
│  ├─ run_autopilot_once.sh
│  ├─ openwrt_pull_config.sh
│  ├─ openwrt_report_status.py
│  ├─ trigger_github_rebuild.sh
│  ├─ rollback_openclash_config.sh
│  └─ install_router_github_sync_openwrt.sh
├─ generate_yaml.py
├─ sumberyaml_core.py
├─ streamlit_app.py
├─ requirements.txt
├─ subscription_links.txt
├─ manual_nodes.txt
├─ openwrt_github.env.example
├─ README.md
├─ README_AUTOPILOT.md
├─ README_ROUTER_GITHUB_SYNC.md
└─ PATCH_NOTES_*.md
```

---

## 4. Cara pakai di GitHub

### 4.1 Upload project ke repository

1. Extract ZIP project.
2. Upload semua isi folder `ConvertYAML-main` ke repository GitHub.
3. Pastikan workflow berada di:

```text
.github/workflows/update-yaml-6jam.yml
.github/workflows/router-feedback.yml
```

4. Buka tab **Actions**.
5. Jalankan workflow **Update OpenClash YAML responsif setiap 3 jam** dengan tombol **Run workflow**.

Workflow utama akan berjalan otomatis setiap 3 jam.

### 4.2 File workflow utama

Workflow utama:

```text
.github/workflows/update-yaml-6jam.yml
```

Fungsinya:

- Checkout repo.
- Install dependency Python.
- Download Mihomo core untuk test OpenClash/Mihomo.
- Download sing-box untuk test kompatibilitas NekoBox.
- Generate YAML.
- Validasi YAML.
- Commit hasil generate ke repo.

### 4.3 Setting penting workflow

Nilai penting yang dipakai:

```yaml
MAX_NODES: "10"
MIN_OUTPUT_NODES: "10"
URLTEST_POOL_NODES: "35"
NEKOBOX_POOL_NODES: "25"
REQUIRE_URL_TEST: "true"
REQUIRE_NEKOBOX_TEST: "true"
URL_TEST_URL: "https://www.gstatic.com/generate_204"
NEKOBOX_TEST_URL: "https://www.gstatic.com/generate_204"
CF_TEST_URL: "https://cp.cloudflare.com"
STREAMING_TEST_URL: "https://cp.cloudflare.com"
URL_TEST_TIMEOUT_MS: "5000"
NEKOBOX_TEST_TIMEOUT_MS: "7000"
FORCE_WS_ONLY: "true"
REQUIRE_WS_UPGRADE: "true"
MIHOMO_SECRET: "reyre"
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

---

## 5. Cara import YAML ke OpenClash

1. Masuk ke LuCI OpenWrt.
2. Buka:

```text
Services / VPN → OpenClash → Config Manage
```

3. Upload salah satu file:

```text
openclash_auto.yaml
```

atau untuk router kecil:

```text
openclash_lite.yaml
```

4. Jadikan config tersebut sebagai config aktif.
5. Restart OpenClash.

Pastikan config memiliki External Controller dan secret:

```yaml
external-controller: 127.0.0.1:9090
secret: "reyre"
```

Kalau ingin dashboard bisa diakses dari LAN, boleh memakai:

```yaml
external-controller: 0.0.0.0:9090
secret: "reyre"
```

Namun untuk keamanan, jangan kosongkan `secret` jika memakai `0.0.0.0`.

---

## 6. Install AutoPilot di OpenWrt

### 6.1 Install dependency

SSH ke router:

```sh
ssh root@192.168.1.1
```

Install paket:

```sh
opkg update
opkg install python3 curl ca-certificates
```

### 6.2 Upload scripts ke router

Upload folder `scripts` ke router, misalnya:

```text
/root/scripts
```

Struktur minimal:

```text
/root/scripts/mihomo_autopilot.py
/root/scripts/install_autopilot_openwrt.sh
/root/scripts/run_autopilot_once.sh
```

### 6.3 Tes AutoPilot sekali jalan

```sh
MIHOMO_SECRET='reyre' python3 /root/scripts/mihomo_autopilot.py --once --close-connections
```

Jika sudah terinstall ke `/etc/mihomo-autopilot`:

```sh
MIHOMO_SECRET='reyre' python3 /etc/mihomo-autopilot/mihomo_autopilot.py --once --close-connections
```

Output sehat biasanya seperti:

```text
[GLOBAL] current=WARM-UP selected=WARM-UP checks=[WARM-UP:66ms]
[PROXY] current=WARM-UP selected=WARM-UP checks=[WARM-UP:64ms]
[STREAMING] current=STREAMING-FAST selected=STREAMING-FAST checks=[STREAMING-FAST:141ms]
```

### 6.4 Install AutoPilot otomatis

Dari folder `/root/scripts`:

```sh
sh /root/scripts/install_autopilot_openwrt.sh
```

Installer akan:

- Menyalin script ke `/etc/mihomo-autopilot/mihomo_autopilot.py`.
- Menambahkan cron setiap 2 menit.
- Memasang `MIHOMO_SECRET='reyre'` otomatis.
- Menyimpan log ke `/tmp/mihomo_autopilot.log`.

Cek cron:

```sh
crontab -l | grep mihomo_autopilot
```

Cek log:

```sh
tail -f /tmp/mihomo_autopilot.log
```

### 6.5 Urutan jalur AutoPilot

Untuk `GLOBAL` dan `PROXY`:

```text
WARM-UP → WARM-UP-CF → AUTO-FAST → FALLBACK → DIRECT
```

Untuk `STREAMING`:

```text
WARM-UP-CF → STREAMING-FAST → WARM-UP → AUTO-FAST → FALLBACK → DIRECT
```

Jika group gagal dua kali, group masuk cooldown sekitar 15 menit agar tidak dipilih berulang saat sedang buruk.

---

## 7. Install Router ↔ GitHub Sync di OpenWrt

### 7.1 Install helper sync

Upload folder `scripts` ke router, lalu jalankan:

```sh
opkg update
opkg install python3 curl ca-certificates
sh /root/scripts/install_router_github_sync_openwrt.sh
```

Installer akan membuat folder:

```text
/etc/mihomo-autopilot
/etc/mihomo-autopilot/backups
```

Dan membuat template env:

```text
/etc/mihomo-autopilot/github.env
```

### 7.2 Isi konfigurasi GitHub

Edit file:

```sh
vi /etc/mihomo-autopilot/github.env
```

Isi minimal:

```sh
GITHUB_REPO='username/repo'
GITHUB_BRANCH='main'
GITHUB_TOKEN='isi_token_github_kamu'
ROUTER_NAME='openwrt-home'

MIHOMO_API='http://127.0.0.1:9090'
MIHOMO_SECRET='reyre'
OPENCLASH_CONFIG_DIR='/etc/openclash/config'
CONFIG_NAME='openclash_auto.yaml'
```

Ganti `username/repo` sesuai repo kamu, misalnya:

```sh
GITHUB_REPO='marcusthornework/ConvertYAML-main'
```

Amankan file token:

```sh
chmod 600 /etc/mihomo-autopilot/github.env
```

### 7.3 Token GitHub yang dibutuhkan

Gunakan **Fine-grained Personal Access Token** dengan akses hanya ke repo project ini.

Permission minimal:

```text
Repository access: Only selected repositories
Contents: Read and Write
Actions: Read and Write
Metadata: Read-only
```

Token dipakai untuk:

- Upload feedback router ke `router_feedback/*.json`.
- Trigger workflow rebuild melalui `repository_dispatch`.
- Pull config dari private repo jika repo tidak public.

Jangan simpan token di YAML OpenClash. Simpan hanya di:

```text
/etc/mihomo-autopilot/github.env
```

### 7.4 Tes token GitHub dari OpenWrt

```sh
. /etc/mihomo-autopilot/github.env
curl -H "Authorization: Bearer $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github+json" \
     https://api.github.com/repos/$GITHUB_REPO
```

Jika benar, keluar JSON data repo. Jika `401`, token salah/expired. Jika `404`, repo salah atau token belum diberi akses ke repo itu.

### 7.5 Tes kirim feedback router ke GitHub

```sh
. /etc/mihomo-autopilot/github.env
python3 /etc/mihomo-autopilot/openwrt_report_status.py --upload
```

Hasilnya akan membuat/update file:

```text
router_feedback/<nama-router>_latest_status.json
```

### 7.6 Tes trigger rebuild GitHub

```sh
. /etc/mihomo-autopilot/github.env
sh /etc/mihomo-autopilot/trigger_github_rebuild.sh "manual-test"
```

Jika berhasil, workflow `router-feedback.yml` akan menerima dispatch lalu memicu workflow generate YAML.

### 7.7 Tes pull config dari GitHub

```sh
. /etc/mihomo-autopilot/github.env
sh /etc/mihomo-autopilot/openwrt_pull_config.sh
```

Script akan:

1. Download config dari GitHub.
2. Validasi dasar YAML.
3. Test syntax dengan Mihomo core jika binary ditemukan.
4. Backup config lama.
5. Replace config OpenClash.
6. Restart OpenClash.
7. Cek API Mihomo.
8. Rollback otomatis jika config baru gagal.

### 7.8 Cron otomatis Router ↔ GitHub Sync

Installer memasang cron:

```text
*/2 * * * * AutoPilot self-healing
*/15 * * * * Kirim feedback router ke GitHub
5 */3 * * * Pull config terbaru dari GitHub ke OpenWrt
```

Cek:

```sh
crontab -l
```

Log:

```sh
tail -f /tmp/mihomo_autopilot.log
tail -f /tmp/router_github_sync.log
```

---

## 8. Rollback manual

Jika config baru bermasalah:

```sh
sh /etc/mihomo-autopilot/rollback_openclash_config.sh
```

Backup berada di:

```text
/etc/mihomo-autopilot/backups
```

Script akan mengambil backup terbaru untuk `CONFIG_NAME` lalu restart OpenClash.

---

## 9. Cara membaca log AutoPilot

Contoh log normal:

```text
[GLOBAL] current=WARM-UP selected=WARM-UP checks=[WARM-UP:66ms]
[PROXY] current=WARM-UP selected=WARM-UP checks=[WARM-UP:64ms]
[SOCIAL-MEDIA] current=WARM-UP selected=WARM-UP checks=[WARM-UP:52ms]
[YOUTUBE] current=WARM-UP selected=WARM-UP checks=[WARM-UP:52ms]
```

Artinya group sehat dan AutoPilot tidak perlu pindah jalur.

Contoh log self-healing:

```text
[STREAMING] current=STREAMING-FAST selected=WARM-UP checks=[WARM-UP-CF:FAIL(cooldown 639s), STREAMING-FAST:FAIL(HTTP Error 504: Gateway Timeout), WARM-UP:58ms]
[OK] STREAMING -> WARM-UP
```

Artinya `STREAMING-FAST` sedang gagal, lalu AutoPilot memindahkan `STREAMING` ke `WARM-UP`.

Contoh log cooldown:

```text
WARM-UP-CF:FAIL(cooldown 858s)
```

Artinya group tersebut sedang ditahan sementara agar tidak dipilih berulang.

---

## 10. Troubleshooting

### 10.1 HTTP Error 401 Unauthorized di AutoPilot

Penyebab: AutoPilot memanggil API Mihomo tanpa secret atau secret salah.

Pastikan YAML berisi:

```yaml
secret: "reyre"
```

Pastikan cron membawa secret:

```sh
crontab -l | grep mihomo_autopilot
```

Baris yang benar:

```sh
MIHOMO_SECRET='reyre'
```

Cara bersihkan cron lama yang dobel:

```sh
crontab -l | grep -v "mihomo_autopilot.py" | crontab -
(crontab -l 2>/dev/null; echo "*/2 * * * * MIHOMO_API=http://127.0.0.1:9090 MIHOMO_SECRET='reyre' python3 /etc/mihomo-autopilot/mihomo_autopilot.py --once --close-connections >> /tmp/mihomo_autopilot.log 2>&1") | crontab -
/etc/init.d/cron restart
: > /tmp/mihomo_autopilot.log
```

Tes manual:

```sh
MIHOMO_SECRET='reyre' python3 /etc/mihomo-autopilot/mihomo_autopilot.py --once --close-connections
```

### 10.2 API Mihomo tidak bisa diakses

Tes:

```sh
curl -H "Authorization: Bearer reyre" http://127.0.0.1:9090/proxies
```

Jika gagal:

- Pastikan OpenClash aktif.
- Pastikan `external-controller` benar.
- Pastikan port `9090` tidak berubah.
- Restart OpenClash:

```sh
/etc/init.d/openclash restart
```

### 10.3 WARM-UP-CF sering 503/504

Ini masih normal pada node Cloudflare/Worker gratis. AutoPilot akan memberi cooldown lalu memilih group lain seperti `WARM-UP` atau `AUTO-FAST`.

Selama log masih menunjukkan `WARM-UP:xxms`, koneksi utama masih sehat.

### 10.4 Workflow gagal karena file tidak ada

Versi ini sudah membuat workflow lebih aman. File opsional yang tidak ada akan dilewati otomatis.

Jika masih error `pathspec ... did not match any files`, pastikan workflow terbaru sudah mengganti:

```text
.github/workflows/update-yaml-6jam.yml
```

### 10.5 GitHub token 401/404

Tes:

```sh
. /etc/mihomo-autopilot/github.env
curl -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/repos/$GITHUB_REPO
```

- `401`: token salah/expired.
- `404`: repo salah atau token tidak punya akses repo.
- `403`: permission kurang atau rate limit.

### 10.6 Config baru gagal setelah pull

Jalankan rollback:

```sh
sh /etc/mihomo-autopilot/rollback_openclash_config.sh
```

Cek log:

```sh
tail -n 100 /tmp/router_github_sync.log
```

---

## 11. Rekomendasi mode pemakaian

### Router normal

```text
Config: openclash_auto.yaml
AutoPilot: aktif tiap 2 menit
Router sync: aktif
LOAD-BALANCE: boleh untuk browsing/download
Streaming/game: pilih WARM-UP atau STREAMING-FAST, bukan LOAD-BALANCE
```

### Router kecil/RAM rendah

```text
Config: openclash_lite.yaml
AutoPilot: aktif tiap 2 menit
Router sync: aktif
LOAD-BALANCE: jangan dipakai untuk streaming/game
Jika router terasa berat, kurangi interval feedback/pull di crontab
```

### Android/NekoBox

```text
Config: openclash_android.yaml
Tanpa rule-providers
Tanpa redir-port
Tanpa tproxy-port
```

---

## 12. File manual node

Manual node disimpan di:

```text
manual_nodes.txt
```

Node manual tetap masuk group `MANUAL` dan `FALLBACK`, tetapi tidak dipaksa masuk semua fast pool agar health-check tidak terlalu berat.

Node manual yang tidak bisa diproses akan dicatat di:

```text
manual_nodes_skipped.txt
```

---

## 13. Laporan kualitas node

Lihat:

```text
node_quality_report.md
```

File ini membantu melihat:

- Node tier utama.
- Node yang layak masuk `WARM-UP`.
- Node Cloudflare yang cocok untuk `WARM-UP-CF`.
- Node cadangan.
- Rekomendasi pemakaian config.

Laporan CSV:

```text
openclash_auto_report.csv
urltest_report.csv
nekobox_test_report.csv
```

---

## 14. Keamanan

- Jangan simpan token GitHub di YAML OpenClash.
- Simpan token hanya di:

```text
/etc/mihomo-autopilot/github.env
```

- Amankan permission:

```sh
chmod 600 /etc/mihomo-autopilot/github.env
```

- Jika memakai `external-controller: 0.0.0.0:9090`, wajib pakai `secret`.
- Lebih aman untuk router lokal:

```yaml
external-controller: 127.0.0.1:9090
secret: "reyre"
```

- Gunakan token GitHub dengan permission minimal dan hanya untuk repo ini.

---

## 15. Quick command reference

### OpenWrt install lengkap

```sh
opkg update
opkg install python3 curl ca-certificates
sh /root/scripts/install_router_github_sync_openwrt.sh
vi /etc/mihomo-autopilot/github.env
chmod 600 /etc/mihomo-autopilot/github.env
/etc/init.d/cron restart
```

### Tes AutoPilot

```sh
. /etc/mihomo-autopilot/github.env
python3 /etc/mihomo-autopilot/mihomo_autopilot.py --once --close-connections
```

### Tes feedback ke GitHub

```sh
. /etc/mihomo-autopilot/github.env
python3 /etc/mihomo-autopilot/openwrt_report_status.py --upload
```

### Tes trigger rebuild

```sh
. /etc/mihomo-autopilot/github.env
sh /etc/mihomo-autopilot/trigger_github_rebuild.sh "manual-test"
```

### Tes pull config

```sh
. /etc/mihomo-autopilot/github.env
sh /etc/mihomo-autopilot/openwrt_pull_config.sh
```

### Rollback

```sh
sh /etc/mihomo-autopilot/rollback_openclash_config.sh
```

### Lihat log

```sh
tail -f /tmp/mihomo_autopilot.log
tail -f /tmp/router_github_sync.log
```

---

## 16. Catatan versi ini

Versi ini adalah gabungan dari beberapa patch:

```text
Responsif anti-hibernasi
STREAMING-FAST url-test
WARM-UP stabil responsif
Smart Stable v2
AutoPilot Self-Healing
Secret reire/reyre fix
Router ↔ GitHub Sync
README lengkap
```

Secret default paket ini:

```yaml
secret: "reyre"
```

Jika kamu mengganti secret OpenClash, sesuaikan juga:

```text
MIHOMO_SECRET di /etc/mihomo-autopilot/github.env
MIHOMO_SECRET di cron AutoPilot
MIHOMO_SECRET di workflow jika perlu
```


---

## Force After OpenClash Reload

Fitur ini berguna agar setelah OpenClash reload/restart, koneksi langsung dipaksa masuk ke jalur/node sehat tanpa menunggu lama.

### Masalah yang diselesaikan

Kadang setelah OpenClash reload, node belum langsung siap. Akibatnya dashboard belum hijau, koneksi terasa delay, atau traffic pertama masih nyangkut di pilihan lama. Patch ini menambahkan script yang akan:

1. Menunggu Mihomo API hidup.
2. Menjalankan AutoPilot beberapa kali.
3. Memilih group sehat seperti `WARM-UP`, `WARM-UP-CF`, `AUTO-FAST`, atau `STREAMING-FAST`.
4. Menutup koneksi lama agar koneksi baru langsung memakai jalur yang sudah sehat.

### Install khusus Force After Reload

Upload folder `scripts` ke router, lalu jalankan:

```sh
opkg update
opkg install python3 curl ca-certificates
cd /root/scripts
MIHOMO_SECRET='reyre' sh install_force_after_reload_openwrt.sh
```

### Tes manual

```sh
sh /etc/mihomo-autopilot/force_after_openclash_reload.sh
```

### Reload OpenClash sekaligus paksa node siap

Setelah installer berjalan, gunakan wrapper ini:

```sh
openclash-reload-autopilot restart
```

Bisa juga:

```sh
openclash-reload-autopilot reload
```

### Guard otomatis setelah reload dari LuCI

Installer juga memasang guard cron tiap 1 menit. Kalau kamu reload OpenClash dari LuCI/OpenClash, guard akan mendeteksi PID core berubah, lalu menjalankan force-after-reload otomatis.

Cek cron:

```sh
crontab -l
```

Cek log:

```sh
tail -f /tmp/mihomo_force_after_reload.log
```

### Setting opsional

Edit file:

```sh
vi /etc/mihomo-autopilot/github.env
```

Tambahkan atau ubah:

```sh
FORCE_WAIT_SECONDS='90'
FORCE_PASSES='3'
FORCE_SLEEP_BETWEEN='5'
FORCE_DELAY_TIMEOUT_MS='3000'
FORCE_MAX_DELAY_MS='1500'
FORCE_FLUSH_FAKEIP='0'
```

Rekomendasi:

- `FORCE_PASSES='3'` sudah cukup untuk router normal.
- `FORCE_FLUSH_FAKEIP='0'` lebih aman untuk harian.
- Pakai `FORCE_FLUSH_FAKEIP='1'` hanya kalau DNS/fake-ip sering nyangkut setelah reload.

### Kalau ingin install lewat Router ↔ GitHub Sync

Installer router-sync juga sudah menyalin file force-after-reload dan menambahkan cron guard otomatis:

```sh
sh /root/scripts/install_router_github_sync_openwrt.sh
```


## No DIRECT After OpenClash Reload

Patch ini mencegah selector utama jatuh ke `DIRECT` setelah OpenClash reload/restart. Setelah core Mihomo aktif, script `force_after_openclash_reload.sh` menjalankan AutoPilot dengan mode:

```sh
--avoid-direct
```

Dengan mode ini, AutoPilot akan memilih jalur proxy sehat seperti:

```text
WARM-UP → WARM-UP-CF → AUTO-FAST → STREAMING-FAST → FALLBACK
```

`DIRECT` tetap tersedia sebagai opsi manual darurat, tetapi tidak dipilih otomatis saat force-after-reload berjalan.

### Install ulang di OpenWrt

```sh
cd /root/scripts
MIHOMO_SECRET='reyre' FORCE_AVOID_DIRECT=1 sh install_force_after_reload_openwrt.sh
```

### Tes manual

```sh
FORCE_AVOID_DIRECT=1 sh /etc/mihomo-autopilot/force_after_openclash_reload.sh
```

### Reload OpenClash + paksa proxy siap

```sh
openclash-reload-autopilot restart
```

### Cek log

```sh
tail -f /tmp/mihomo_force_after_reload.log
```

Jika ingin mengizinkan `DIRECT` sebagai fallback otomatis setelah reload, ubah:

```sh
FORCE_AVOID_DIRECT=0
```

Namun untuk mencegah traffic bocor ke koneksi langsung, biarkan default:

```sh
FORCE_AVOID_DIRECT=1
```

---

## Manual Unblock Domains → Group MANUAL

Project ini mendukung file khusus:

```text
manual_unblock_domains.txt
```

Semua domain aktif yang ditulis di file tersebut akan **dipaksa berjalan melalui group `MANUAL`**.

Fitur ini cocok untuk domain/web tertentu yang harus memakai node manual, misalnya domain yang lebih cocok memakai SNI/Host manual atau domain yang tidak ingin lewat `GLOBAL`, `AUTO-FAST`, `STREAMING`, maupun `DIRECT`.

### Cara isi file

Buka `manual_unblock_domains.txt`, lalu isi satu domain per baris:

```txt
reddit.com
medium.com
old.reddit.com
```

Format yang didukung:

```txt
example.com
*.example.com
+.example.com
https://example.com/path
DOMAIN,sub.example.com
DOMAIN-SUFFIX,example.com
DOMAIN-KEYWORD,keyword
GEOSITE,category
```

Contoh lengkap:

```txt
reddit.com
DOMAIN,old.reddit.com
DOMAIN-SUFFIX,medium.com
DOMAIN-KEYWORD,reddit
```

Setelah GitHub Action/generator berjalan, rule akan dimasukkan otomatis ke YAML:

```yaml
- DOMAIN-SUFFIX,reddit.com,MANUAL
- DOMAIN,old.reddit.com,MANUAL
- DOMAIN-SUFFIX,medium.com,MANUAL
- DOMAIN-KEYWORD,reddit,MANUAL
```

### Posisi rule

Rule dari `manual_unblock_domains.txt` dimasukkan setelah rule LAN/private dan sebelum rule iklan, sosial media, YouTube, streaming, dan `MATCH`.

Urutan ini sengaja dibuat agar:

- akses router/LAN tetap `DIRECT`,
- domain manual tetap prioritas ke `MANUAL`,
- domain tersebut tidak tertimpa rule `GLOBAL`, `STREAMING`, `SOCIAL-MEDIA`, atau `REJECT`.

### Generate ulang

Setelah mengubah `manual_unblock_domains.txt`, jalankan GitHub Action atau generate lokal:

```sh
python3 generate_yaml.py
```

Lalu OpenWrt bisa pull config terbaru seperti biasa.

### Catatan penting

`manual_unblock_domains.txt` hanya mengatur **routing domain**. Node yang dipakai tetap berasal dari group `MANUAL`, yaitu daftar node di `manual_nodes.txt`.

