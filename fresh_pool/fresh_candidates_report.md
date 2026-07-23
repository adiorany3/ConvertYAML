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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-77MS` (url=237ms, nekobox=244ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=228ms, nekobox=256ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=218ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=217ms, nekobox=258ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-87MS` (url=200ms, nekobox=278ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS` (url=243ms, nekobox=263ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-91MS` (url=221ms, nekobox=247ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS` (url=271ms, nekobox=195ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-106MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-107MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-80MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-118MS` (url=233ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-81MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-120MS` (url=251ms, status=HTTP 204)
15. `AKUN-015-CF-BYOIP-188-164-248-0-2-VLESS-WS-123MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-TIME-VLESS-WS-135MS` (url=285ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-209MS` (url=440ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-177MS` (url=372ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-193MS` (url=428ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-371MS` (url=834ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-372MS` (url=816ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-97MS` (url=925ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-642MS` (url=1096ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-725MS` (url=1213ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-422MS` (url=3474ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
