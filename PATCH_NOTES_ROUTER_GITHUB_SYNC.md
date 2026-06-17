# Patch Notes — Router GitHub Sync

Improvement baru:

- Tambah `openwrt_pull_config.sh` untuk download config dari GitHub ke OpenWrt.
- Tambah backup + rollback otomatis jika config baru gagal.
- Tambah `openwrt_report_status.py` untuk mengirim status router ke GitHub.
- Tambah `trigger_github_rebuild.sh` untuk memicu GitHub Actions dari router.
- Tambah `rollback_openclash_config.sh` untuk rollback manual.
- Tambah `install_router_github_sync_openwrt.sh` untuk instalasi cron otomatis.
- Tambah workflow `.github/workflows/router-feedback.yml` untuk menerima `repository_dispatch`.
- Tambah contoh env `openwrt_github.env.example`.
- Token GitHub tidak ditaruh di YAML; disimpan aman di `/etc/mihomo-autopilot/github.env`.

Validasi lokal:

- Python compile OK.
- Shell syntax OK.
- YAML workflow parse OK.
- ZIP integrity OK.
