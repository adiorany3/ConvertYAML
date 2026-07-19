# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-85MS` (url=371ms, nekobox=312ms, status=yes)
2. `AKUN-002-RTCOMM-SRAVNI-RU-VLESS-WS-86MS` (url=363ms, nekobox=344ms, status=yes)
3. `AKUN-003-CF-CLIENTS-VLESS-WS-100MS` (url=379ms, nekobox=328ms, status=yes)
4. `AKUN-004-GO-DADDY-COM-LLC-VLESS-WS-97MS` (url=336ms, nekobox=333ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-102MS` (url=334ms, nekobox=530ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-103MS` (url=373ms, nekobox=402ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-105MS` (url=298ms, nekobox=321ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-106MS` (url=324ms, nekobox=355ms, status=yes)
9. `AKUN-009-BGP48-HK-VLESS-WS-78MS` (url=361ms, nekobox=364ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-109MS` (url=309ms, nekobox=373ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-97MS` (url=343ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-101MS` (url=400ms, status=HTTP 204)
13. `AKUN-013-ZOOM-VLESS-WS-87MS` (url=303ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-102MS` (url=290ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-126MS` (url=337ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-109MS` (url=350ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-116MS` (url=365ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-117MS` (url=322ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-115MS` (url=279ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-105MS` (url=318ms, status=HTTP 204)
21. `AKUN-021-WEBEX-VLESS-WS-115MS` (url=382ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-137MS` (url=309ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-113MS` (url=315ms, status=HTTP 204)
24. `AKUN-024-DEV-VLESS-WS-133MS` (url=330ms, status=HTTP 204)
25. `AKUN-025-NEXUSMODS-VLESS-WS-156MS` (url=344ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
