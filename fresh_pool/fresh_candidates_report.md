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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-SIN-VLESS-WS-129MS` (url=275ms, nekobox=299ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-139MS` (url=271ms, nekobox=290ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-141MS` (url=244ms, nekobox=299ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-142MS` (url=345ms, nekobox=312ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-138MS` (url=258ms, nekobox=283ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-141MS` (url=247ms, nekobox=234ms, status=no)
7. `AKUN-006-UNKNOWN-VLESS-WS-142MS`
8. `AKUN-007-WPENG-VLESS-WS-134MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-148MS`
10. `AKUN-009-MYBB-VLESS-WS-148MS`
11. `AKUN-010-ZVC-VLESS-WS-134MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-139MS` (url=253ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-152MS` (url=279ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-155MS` (url=268ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-150MS` (url=255ms, status=HTTP 204)
16. `AKUN-016-OVH-VLESS-WS-162MS` (url=283ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-138MS` (url=280ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-150MS` (url=274ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-172MS` (url=249ms, status=HTTP 204)
20. `AKUN-020-WEYRO-NET-VLESS-WS-153MS` (url=298ms, status=HTTP 204)
21. `AKUN-021-WPENG-VLESS-WS-144MS` (url=326ms, status=HTTP 204)
22. `AKUN-022-COMPREND-NET-VLESS-WS-147MS` (url=268ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-159MS` (url=282ms, status=HTTP 204)
24. `AKUN-024-1PASSWORD-VLESS-WS-157MS` (url=254ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-287MS` (url=487ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
