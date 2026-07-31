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
1. `AKUN-001-UNKNOWN-VLESS-WS-59MS` (url=225ms, nekobox=244ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-54MS` (url=219ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=224ms, nekobox=236ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-72MS` (url=212ms, nekobox=235ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=218ms, nekobox=246ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=226ms, nekobox=268ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-68MS` (url=219ms, nekobox=235ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-62MS` (url=214ms, nekobox=237ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-67MS` (url=223ms, nekobox=227ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-105MS` (url=215ms, nekobox=245ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-68MS` (url=223ms, status=HTTP 204)
12. `AKUN-013-UNKNOWN-VLESS-WS-101MS` (url=208ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-342MS` (url=746ms, status=HTTP 204)
14. `AKUN-015-090227-VLESS-WS-299MS` (url=598ms, status=HTTP 204)
15. `AKUN-019-CN-CF-VLESS-WS-419MS` (url=2591ms, status=HTTP 204)
16. `AKUN-020-UNKNOWN-VLESS-WS-402MS` (url=916ms, status=HTTP 204)
17. `AKUN-023-CLOUDFLARE-VLESS-WS-560MS` (url=990ms, status=HTTP 204)
18. `AKUN-024-CLOUDFLARE-VLESS-WS-620MS` (url=1030ms, status=HTTP 204)
19. `AKUN-025-CLOUDFLARE-VLESS-WS-603MS` (url=1063ms, status=HTTP 204)
20. `AKUN-026-UNKNOWN-VLESS-WS-693MS` (url=1133ms, status=HTTP 204)
21. `AKUN-027-UNKNOWN-VLESS-WS-691MS` (url=1172ms, status=HTTP 204)
22. `AKUN-028-CLOUDFLARE-VLESS-WS-658MS` (url=1077ms, status=HTTP 204)
23. `AKUN-029-CLOUDFLARE-VLESS-WS-693MS` (url=1162ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-743MS` (url=1299ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-841MS` (url=1587ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
