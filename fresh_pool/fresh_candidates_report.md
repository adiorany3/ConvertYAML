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
1. `AKUN-001-UNKNOWN-VLESS-WS-59MS` (url=235ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=238ms, nekobox=256ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS` (url=231ms, nekobox=259ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-64MS` (url=219ms, nekobox=251ms, status=yes)
5. `AKUN-005-ZOOM-VLESS-WS-66MS` (url=300ms, nekobox=267ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS` (url=278ms, nekobox=260ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-64MS` (url=235ms, nekobox=331ms, status=yes)
8. `AKUN-008-OVH-VLESS-WS-58MS` (url=306ms, nekobox=256ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS` (url=251ms, nekobox=255ms, status=yes)
10. `AKUN-010-008500-VLESS-WS-68MS` (url=224ms, nekobox=259ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-66MS` (url=240ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-95MS` (url=226ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-102MS` (url=222ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-103MS` (url=244ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-67MS` (url=250ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-73MS` (url=529ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-74MS` (url=218ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-74MS` (url=261ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-91MS` (url=244ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-244MS` (url=542ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-237MS` (url=551ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-262MS` (url=547ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-275MS` (url=440ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-460MS` (url=813ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-506MS` (url=4825ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
