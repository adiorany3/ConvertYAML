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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=197ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=204ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS` (url=212ms, nekobox=252ms, status=yes)
4. `AKUN-004-MYBB-VLESS-WS-60MS` (url=226ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-61MS` (url=203ms, nekobox=178ms, status=no)
6. `AKUN-005-BIGCOMMERCE-VLESS-WS-63MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-85MS`
10. `AKUN-009-DEV-VLESS-WS-81MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-88MS`
12. `AKUN-012-ZVC-VLESS-WS-89MS` (url=222ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-85MS` (url=205ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-80MS` (url=202ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-74MS` (url=226ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-83MS` (url=230ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-69MS` (url=221ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-68MS` (url=221ms, status=HTTP 204)
19. `AKUN-019-CCWU-VLESS-WS-67MS` (url=221ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-108MS` (url=199ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-79MS` (url=218ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-63MS` (url=208ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-110MS` (url=198ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-145MS` (url=227ms, status=HTTP 204)
25. `AKUN-025-ADF-VLESS-WS-64MS` (url=231ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
