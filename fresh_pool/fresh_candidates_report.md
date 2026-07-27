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
1. `AKUN-001-UNKNOWN-VLESS-WS-83MS` (url=208ms, nekobox=261ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-86MS` (url=213ms, nekobox=263ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS` (url=205ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=209ms, nekobox=237ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=234ms, nekobox=234ms, status=yes)
6. `AKUN-006-008500-VLESS-WS-89MS` (url=211ms, nekobox=233ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-88MS` (url=233ms, nekobox=264ms, status=yes)
8. `AKUN-008-DEV-VLESS-WS-89MS` (url=217ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=202ms, nekobox=262ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-85MS` (url=229ms, nekobox=263ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-89MS` (url=232ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-94MS` (url=209ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-82MS` (url=203ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-100MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-94MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-100MS` (url=235ms, status=HTTP 204)
17. `AKUN-017-CCWU-VLESS-WS-91MS` (url=234ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-91MS` (url=215ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-99MS` (url=206ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-104MS` (url=227ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-125MS` (url=261ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-169MS` (url=272ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-133MS` (url=214ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-119MS` (url=209ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-171MS` (url=242ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
