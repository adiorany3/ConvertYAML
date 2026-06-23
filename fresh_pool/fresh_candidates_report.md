# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 18
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 24

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-133MS` (url=261ms, nekobox=280ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-133MS` (url=255ms, nekobox=301ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-133MS` (url=245ms, nekobox=224ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-137MS`
5. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-157MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-142MS`
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-150MS`
8. `AKUN-007-UK-GB-DCL-01-20191003-VLESS-WS-167MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-352MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-354MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-378MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-380MS` (url=756ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-371MS` (url=752ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-389MS` (url=767ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-386MS` (url=805ms, status=HTTP 204)
16. `AKUN-026-APPLESERAJ-VLESS-WS-633MS` (url=968ms, status=HTTP 204)
17. `AKUN-032-UNKNOWN-VLESS-WS-668MS` (url=882ms, status=HTTP 204)
18. `AKUN-035-DEV-VLESS-WS-305MS` (url=1280ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
