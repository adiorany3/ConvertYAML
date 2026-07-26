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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=231ms, nekobox=230ms, status=yes)
2. `AKUN-002-008500-VLESS-WS-78MS` (url=214ms, nekobox=254ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-77MS` (url=223ms, nekobox=231ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-75MS` (url=222ms, nekobox=256ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-76MS` (url=217ms, nekobox=252ms, status=yes)
6. `AKUN-006-CCWU-VLESS-WS-83MS` (url=209ms, nekobox=257ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-83MS` (url=225ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS` (url=204ms, nekobox=238ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS` (url=217ms, nekobox=248ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=221ms, nekobox=249ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-71MS` (url=218ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-109MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-97MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-87MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-138MS` (url=224ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-77MS` (url=227ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-117MS` (url=230ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-209MS` (url=346ms, status=HTTP 204)
19. `AKUN-019-008500-VLESS-WS-76MS` (url=221ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-79MS` (url=218ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-76MS` (url=206ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-81MS` (url=204ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-90MS` (url=221ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-353MS` (url=756ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-87MS` (url=230ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
