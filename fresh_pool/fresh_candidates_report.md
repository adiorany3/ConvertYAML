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
1. `AKUN-001-CELESTARA-VLESS-WS-78MS` (url=363ms, nekobox=357ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-87MS` (url=281ms, nekobox=335ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-87MS` (url=307ms, nekobox=321ms, status=yes)
4. `AKUN-004-DIXONS-VLESS-WS-81MS` (url=337ms, nekobox=405ms, status=yes)
5. `AKUN-005-UK-GB-DCL-01-20191003-VLESS-WS-102MS` (url=355ms, nekobox=345ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS` (url=355ms, nekobox=400ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-102MS` (url=423ms, nekobox=410ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=396ms, nekobox=348ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-105MS` (url=350ms, nekobox=370ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-93MS` (url=349ms, nekobox=370ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-75MS` (url=346ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-100MS` (url=334ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-118MS` (url=387ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-132MS` (url=321ms, status=HTTP 204)
15. `AKUN-015-ZOOM-VLESS-WS-81MS` (url=308ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-105MS` (url=345ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-124MS` (url=360ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-128MS` (url=321ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-88MS` (url=397ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-85MS` (url=289ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-118MS` (url=370ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-128MS` (url=335ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-165MS` (url=334ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-129MS` (url=378ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-93MS` (url=285ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
