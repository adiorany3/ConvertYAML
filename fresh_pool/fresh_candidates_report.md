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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=306ms, nekobox=304ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-104MS` (url=307ms, nekobox=304ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-112MS` (url=312ms, nekobox=325ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-109MS` (url=320ms, nekobox=347ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-115MS` (url=279ms, nekobox=387ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-119MS` (url=400ms, nekobox=352ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-83MS` (url=443ms, nekobox=361ms, status=yes)
8. `AKUN-008-PUBLICDOMAINREGISTRY-NET-VLESS-WS-105MS` (url=337ms, nekobox=422ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS` (url=297ms, nekobox=338ms, status=yes)
10. `AKUN-010-MEDIUM-VLESS-WS-109MS` (url=285ms, nekobox=486ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-121MS` (url=299ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-130MS` (url=313ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-132MS` (url=463ms, status=HTTP 204)
14. `AKUN-014-IDC-SG-VLESS-WS-112MS` (url=330ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-126MS` (url=323ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-117MS` (url=291ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-145MS` (url=303ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-156MS` (url=275ms, status=HTTP 204)
19. `AKUN-019-MYBB-VLESS-WS-133MS` (url=366ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-111MS` (url=303ms, status=HTTP 204)
21. `AKUN-021-SHOPIFY-VLESS-WS-130MS` (url=295ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-162MS` (url=357ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-219MS` (url=484ms, status=HTTP 204)
24. `AKUN-024-QZZ-VLESS-WS-281MS` (url=567ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-306MS` (url=673ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
