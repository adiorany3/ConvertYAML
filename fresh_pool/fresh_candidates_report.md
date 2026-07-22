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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-116MS` (url=258ms, nekobox=279ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-115MS` (url=255ms, nekobox=282ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-127MS` (url=267ms, nekobox=286ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-121MS` (url=263ms, nekobox=310ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-126MS` (url=238ms, nekobox=283ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-137MS` (url=270ms, nekobox=310ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-138MS` (url=268ms, nekobox=295ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-147MS` (url=258ms, nekobox=290ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-144MS` (url=295ms, nekobox=309ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-133MS` (url=267ms, nekobox=332ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-147MS` (url=284ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-130MS` (url=270ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-140MS` (url=254ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-139MS` (url=246ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-141MS` (url=270ms, status=HTTP 204)
16. `AKUN-016-WPENG-VLESS-WS-164MS` (url=275ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-146MS` (url=266ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-191MS` (url=308ms, status=HTTP 204)
19. `AKUN-019-ZVC-VLESS-WS-151MS` (url=272ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-187MS` (url=346ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-423MS` (url=932ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-423MS` (url=1316ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-748MS` (url=1212ms, status=HTTP 204)
24. `AKUN-028-SPEEDTEST-VLESS-WS-494MS` (url=793ms, status=HTTP 204)
25. `AKUN-030-SPEEDTEST-VLESS-WS-681MS` (url=826ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
