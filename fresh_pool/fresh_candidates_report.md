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
1. `AKUN-001-ZOOM-VLESS-WS-76MS` (url=218ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=234ms, nekobox=256ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=228ms, nekobox=257ms, status=yes)
4. `AKUN-004-CCWU-VLESS-WS-71MS` (url=199ms, nekobox=249ms, status=yes)
5. `AKUN-005-DEV-VLESS-WS-74MS` (url=220ms, nekobox=259ms, status=yes)
6. `AKUN-006-SPEEDTEST-VLESS-WS-74MS` (url=205ms, nekobox=191ms, status=no)
7. `AKUN-006-UNKNOWN-VLESS-WS-77MS`
8. `AKUN-007-008500-VLESS-WS-78MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-75MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-83MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-79MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-87MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-74MS` (url=237ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-103MS` (url=209ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-88MS` (url=243ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-106MS` (url=242ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-85MS` (url=221ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-75MS` (url=218ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-97MS` (url=228ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-76MS` (url=225ms, status=HTTP 204)
21. `AKUN-022-DEV-VLESS-WS-107MS` (url=231ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-115MS` (url=227ms, status=HTTP 204)
23. `AKUN-024-MEDIUM-VLESS-WS-82MS` (url=202ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-170MS` (url=416ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-125MS` (url=225ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
