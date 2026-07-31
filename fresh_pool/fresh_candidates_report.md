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
1. `AKUN-001-UNKNOWN-VLESS-WS-74MS` (url=200ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-81MS` (url=217ms, nekobox=251ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-98MS`
4. `AKUN-005-CLOUDFLARE-VLESS-WS-100MS` (url=218ms, nekobox=182ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-102MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-93MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS`
8. `AKUN-007-ZENFO-1-VLESS-WS-93MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-97MS`
10. `AKUN-011-CLOUDFLARE-VLESS-WS-109MS` (url=205ms, nekobox=223ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-101MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-129MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-136MS` (url=359ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-248MS` (url=509ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-238MS` (url=1318ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-204MS` (url=1081ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-361MS` (url=645ms, status=HTTP 204)
18. `AKUN-021-UNKNOWN-VLESS-WS-407MS` (url=662ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-429MS` (url=723ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-421MS` (url=715ms, status=HTTP 204)
21. `AKUN-024-GAMEFICTOINSPEED-VLESS-WS-454MS` (url=754ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-507MS` (url=854ms, status=HTTP 204)
23. `AKUN-026-SRTONGSTON-VLESS-WS-479MS` (url=733ms, status=HTTP 204)
24. `AKUN-030-CLOUDFLARE-VLESS-WS-547MS` (url=962ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-522MS` (url=4906ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
