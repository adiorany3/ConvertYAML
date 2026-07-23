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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=595ms, nekobox=344ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=279ms, nekobox=324ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-103MS` (url=299ms, nekobox=303ms, status=yes)
4. `AKUN-004-MYBB-VLESS-WS-106MS` (url=276ms, nekobox=376ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-111MS` (url=296ms, nekobox=336ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS` (url=299ms, nekobox=342ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-117MS` (url=303ms, nekobox=316ms, status=yes)
8. `AKUN-008-DEV-VLESS-WS-110MS` (url=488ms, nekobox=319ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-111MS` (url=280ms, nekobox=368ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS` (url=303ms, nekobox=330ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-126MS` (url=312ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-120MS` (url=277ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-120MS` (url=289ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-137MS` (url=290ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-131MS` (url=318ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-125MS` (url=286ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-114MS` (url=367ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-106MS` (url=348ms, status=HTTP 204)
19. `AKUN-019-LEVIKOGJGFDD-VLESS-WS-121MS` (url=416ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-116MS` (url=302ms, status=HTTP 204)
21. `AKUN-021-ZOOM-VLESS-WS-122MS` (url=309ms, status=HTTP 204)
22. `AKUN-022-CCWU-VLESS-WS-138MS` (url=338ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-154MS` (url=315ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-165MS` (url=285ms, status=HTTP 204)
25. `AKUN-025-SHOPIFY-VLESS-WS-132MS` (url=383ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
