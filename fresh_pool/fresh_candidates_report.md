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
1. `AKUN-001-DEV-VLESS-WS-110MS` (url=281ms, nekobox=337ms, status=yes)
2. `AKUN-002-MYBB-VLESS-WS-112MS` (url=291ms, nekobox=338ms, status=yes)
3. `AKUN-003-1PASSWORD-VLESS-WS-107MS` (url=256ms, nekobox=315ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-118MS` (url=266ms, nekobox=317ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-103MS` (url=302ms, nekobox=295ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-121MS` (url=272ms, nekobox=223ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-113MS`
8. `AKUN-007-ZVC-VLESS-WS-123MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-121MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-120MS`
11. `AKUN-010-DEV-VLESS-WS-152MS`
12. `AKUN-012-CCWU-VLESS-WS-129MS` (url=291ms, status=HTTP 204)
13. `AKUN-013-DIGITALOCEAN-VLESS-WS-162MS` (url=283ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-115MS` (url=254ms, status=HTTP 204)
15. `AKUN-015-ES-FORNEX-20160629-VLESS-WS-127MS` (url=374ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-98MS` (url=302ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-98MS` (url=302ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-253MS` (url=415ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-305MS` (url=596ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-321MS` (url=648ms, status=HTTP 204)
21. `AKUN-022-DEV-VLESS-WS-334MS` (url=2956ms, status=HTTP 204)
22. `AKUN-023-DEV-VLESS-WS-332MS` (url=1683ms, status=HTTP 204)
23. `AKUN-024-DEV-VLESS-WS-358MS` (url=1935ms, status=HTTP 204)
24. `AKUN-025-DEV-VLESS-WS-346MS` (url=2499ms, status=HTTP 204)
25. `AKUN-026-DEV-VLESS-WS-330MS` (url=1917ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
