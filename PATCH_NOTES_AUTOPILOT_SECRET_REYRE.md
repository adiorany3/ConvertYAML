# Patch Notes — AutoPilot Secret `reyre`

Perubahan ini dibuat untuk memperbaiki error:

```text
HTTP Error 401: Unauthorized
```

## Perubahan

- Menambahkan `secret: "reyre"` ke YAML OpenClash utama.
- AutoPilot default memakai secret `reyre`.
- Installer OpenWrt otomatis memasang `MIHOMO_SECRET='reyre'` di cron.
- Helper `run_autopilot_once.sh` otomatis membawa `MIHOMO_SECRET='reyre'`.
- AutoPilot bisa mencoba mendeteksi secret dari file config OpenClash/Mihomo tanpa dependency PyYAML.
- Pesan error `401 Unauthorized` dibuat lebih jelas dengan instruksi fix.
- Workflow GitHub diberi env `MIHOMO_SECRET: "reyre"` agar YAML hasil generate ulang tetap membawa secret.

## Tes cepat di OpenWrt

```sh
MIHOMO_SECRET='reyre' python3 /etc/mihomo-autopilot/mihomo_autopilot.py --once --close-connections
```

## Reinstall cron

```sh
MIHOMO_SECRET='reyre' sh scripts/install_autopilot_openwrt.sh
```
