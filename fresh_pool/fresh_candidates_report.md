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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=280ms, nekobox=265ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=230ms, nekobox=262ms, status=yes)
3. `AKUN-003-MYBB-VLESS-WS-72MS` (url=251ms, nekobox=262ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-78MS` (url=245ms, nekobox=287ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-77MS` (url=234ms, nekobox=264ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS` (url=243ms, nekobox=257ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS` (url=246ms, nekobox=283ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-67MS` (url=240ms, nekobox=278ms, status=yes)
9. `AKUN-009-1PASSWORD-VLESS-WS-83MS` (url=253ms, nekobox=269ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-76MS` (url=262ms, nekobox=315ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-74MS` (url=244ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-76MS` (url=235ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-78MS` (url=235ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-77MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-88MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-89MS` (url=242ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-89MS` (url=256ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-89MS` (url=226ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-89MS` (url=431ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-80MS` (url=268ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-91MS` (url=429ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-151MS` (url=360ms, status=HTTP 204)
23. `AKUN-023-ADF-VLESS-WS-71MS` (url=237ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-255MS` (url=572ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-257MS` (url=465ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
