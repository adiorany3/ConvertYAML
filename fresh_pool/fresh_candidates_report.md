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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-117MS` (url=262ms, nekobox=277ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-124MS` (url=264ms, nekobox=284ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-120MS` (url=254ms, nekobox=265ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-125MS` (url=238ms, nekobox=272ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-123MS` (url=256ms, nekobox=286ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-123MS` (url=255ms, nekobox=294ms, status=yes)
7. `AKUN-007-CCWU-VLESS-WS-133MS` (url=264ms, nekobox=274ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-130MS` (url=235ms, nekobox=290ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-129MS` (url=248ms, nekobox=270ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-141MS` (url=271ms, nekobox=289ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-151MS` (url=248ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-133MS` (url=1012ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-145MS` (url=252ms, status=HTTP 204)
14. `AKUN-014-MYBB-VLESS-WS-136MS` (url=244ms, status=HTTP 204)
15. `AKUN-015-ADF-VLESS-WS-121MS` (url=238ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-150MS` (url=258ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-152MS` (url=257ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-154MS` (url=260ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-131MS` (url=268ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-164MS` (url=267ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-144MS` (url=260ms, status=HTTP 204)
22. `AKUN-022-SHOPIFY-VLESS-WS-154MS` (url=249ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-133MS` (url=325ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-197MS` (url=264ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-143MS` (url=250ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
