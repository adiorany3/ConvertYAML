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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-114MS` (url=275ms, nekobox=278ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-114MS` (url=260ms, nekobox=272ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-117MS` (url=252ms, nekobox=280ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-120MS` (url=246ms, nekobox=282ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-124MS` (url=254ms, nekobox=291ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-127MS` (url=277ms, nekobox=346ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-117MS` (url=240ms, nekobox=272ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-130MS` (url=243ms, nekobox=287ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-123MS` (url=245ms, nekobox=274ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-145MS` (url=249ms, nekobox=283ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-119MS` (url=255ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-144MS` (url=254ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-165MS` (url=245ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-137MS` (url=257ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-147MS` (url=242ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-165MS` (url=251ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-192MS` (url=332ms, status=HTTP 204)
18. `AKUN-018-ZVC-VLESS-WS-123MS` (url=243ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-190MS` (url=351ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-190MS` (url=330ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-179MS` (url=319ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-178MS` (url=306ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-189MS` (url=309ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-125MS` (url=324ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-129MS` (url=251ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
