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
1. `AKUN-001-UNKNOWN-VLESS-WS-184MS` (url=381ms, nekobox=375ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-186MS` (url=336ms, nekobox=7177ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-190MS`
4. `AKUN-003-DEV-VLESS-WS-191MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-187MS`
6. `AKUN-005-MEDIUM-VLESS-WS-191MS`
7. `AKUN-007-SPEEDTEST-VLESS-WS-185MS` (url=294ms, nekobox=266ms, status=no)
8. `AKUN-006-DEV-VLESS-WS-191MS`
9. `AKUN-007-UNKNOWN-VLESS-WS-199MS`
10. `AKUN-008-UNKNOWN-VLESS-WS-205MS`
11. `AKUN-009-UNKNOWN-VLESS-WS-203MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-198MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-192MS` (url=349ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-193MS` (url=331ms, status=HTTP 204)
15. `AKUN-015-MYBB-VLESS-WS-185MS` (url=295ms, status=HTTP 204)
16. `AKUN-016-SPEEDTEST-VLESS-WS-198MS` (url=286ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-192MS` (url=342ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-191MS` (url=346ms, status=HTTP 204)
19. `AKUN-019-CCWU-VLESS-WS-200MS` (url=324ms, status=HTTP 204)
20. `AKUN-020-RMGYVPN-VLESS-WS-302MS` (url=574ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-623MS` (url=1214ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-681MS` (url=1075ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-676MS` (url=1052ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-632MS` (url=1063ms, status=HTTP 204)
25. `AKUN-027-SUKARIO-VLESS-WS-679MS` (url=1043ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
