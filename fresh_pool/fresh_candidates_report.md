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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=226ms, nekobox=269ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=246ms, nekobox=264ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-68MS` (url=289ms, nekobox=268ms, status=yes)
4. `AKUN-004-OVH-VLESS-WS-86MS` (url=259ms, nekobox=292ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=248ms, nekobox=283ms, status=yes)
6. `AKUN-006-MEDIUM-VLESS-WS-79MS` (url=263ms, nekobox=282ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS` (url=249ms, nekobox=265ms, status=yes)
8. `AKUN-008-WPENG-VLESS-WS-97MS` (url=240ms, nekobox=269ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-95MS` (url=264ms, nekobox=274ms, status=yes)
10. `AKUN-010-WEYRO-NET-VLESS-WS-74MS` (url=267ms, nekobox=271ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-119MS` (url=258ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-76MS` (url=237ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-117MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-98MS` (url=248ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-79MS` (url=249ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-91MS` (url=268ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-73MS` (url=264ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-85MS` (url=245ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-152MS` (url=255ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-260MS` (url=564ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-288MS` (url=625ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-282MS` (url=645ms, status=HTTP 204)
23. `AKUN-025-CONFLU-VLESS-WS-260MS` (url=544ms, status=HTTP 204)
24. `AKUN-026-GALAKTIKA-20201015-VLESS-WS-278MS` (url=600ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-285MS` (url=592ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
