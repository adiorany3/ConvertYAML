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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-137MS` (url=283ms, nekobox=301ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-137MS` (url=262ms, nekobox=299ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-142MS` (url=274ms, nekobox=306ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-142MS` (url=272ms, nekobox=280ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-142MS` (url=303ms, nekobox=308ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-143MS` (url=269ms, nekobox=295ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-145MS` (url=270ms, nekobox=297ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-140MS` (url=282ms, nekobox=319ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-144MS` (url=271ms, nekobox=306ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-135MS` (url=246ms, nekobox=300ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-136MS` (url=274ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-139MS` (url=270ms, status=HTTP 204)
13. `AKUN-013-ES-FORNEX-20160629-VLESS-WS-140MS` (url=270ms, status=HTTP 204)
14. `AKUN-014-DIXONS-VLESS-WS-153MS` (url=280ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-142MS` (url=300ms, status=HTTP 204)
16. `AKUN-016-CZ-LOTUNA-19970206-VLESS-WS-162MS` (url=258ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-143MS` (url=250ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-156MS` (url=278ms, status=HTTP 204)
19. `AKUN-019-UK-GB-DCL-01-20191003-VLESS-WS-154MS` (url=322ms, status=HTTP 204)
20. `AKUN-020-UK-GB-DCL-01-20191003-VLESS-WS-161MS` (url=326ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-152MS` (url=322ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-147MS` (url=289ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-163MS` (url=270ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-204MS` (url=308ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-221MS` (url=428ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
