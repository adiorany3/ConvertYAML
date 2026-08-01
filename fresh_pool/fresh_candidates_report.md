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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-DEV-VLESS-WS-87MS` (url=370ms, nekobox=316ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-81MS` (url=289ms, nekobox=190ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-97MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS` (url=244ms, nekobox=7178ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-106MS` (url=299ms, nekobox=191ms, status=no)
13. `AKUN-010-UNKNOWN-VLESS-WS-85MS`
14. `AKUN-014-CCWU-VLESS-WS-83MS` (url=376ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-100MS` (url=399ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-97MS` (url=303ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-100MS` (url=295ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-111MS` (url=306ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-81MS` (url=363ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-99MS` (url=317ms, status=HTTP 204)
21. `AKUN-021-MEDIUM-VLESS-WS-121MS` (url=335ms, status=HTTP 204)
22. `AKUN-022-LEVIKOGJGFDD-VLESS-WS-103MS` (url=316ms, status=HTTP 204)
23. `AKUN-023-1PASSWORD-VLESS-WS-98MS` (url=298ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-130MS` (url=318ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-102MS` (url=341ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
