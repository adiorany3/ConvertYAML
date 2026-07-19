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
1. `AKUN-001-UNKNOWN-VLESS-WS-63MS` (url=218ms, nekobox=238ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-73MS` (url=206ms, nekobox=227ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=213ms, nekobox=259ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=203ms, nekobox=242ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-75MS` (url=219ms, nekobox=253ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-71MS` (url=213ms, nekobox=251ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=214ms, nekobox=244ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-74MS` (url=220ms, nekobox=252ms, status=yes)
9. `AKUN-009-CZ-LOTUNA-19970206-VLESS-WS-88MS` (url=225ms, nekobox=258ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-75MS` (url=207ms, nekobox=241ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-100MS` (url=216ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-92MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-98MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-85MS` (url=385ms, status=HTTP 204)
15. `AKUN-015-UK-GB-DCL-01-20191003-VLESS-WS-107MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-91MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-81MS` (url=215ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-87MS` (url=221ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-87MS` (url=217ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-90MS` (url=217ms, status=HTTP 204)
21. `AKUN-021-1PASSWORD-VLESS-WS-118MS` (url=228ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-92MS` (url=232ms, status=HTTP 204)
23. `AKUN-023-WPENG-VLESS-WS-91MS` (url=210ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-90MS` (url=510ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-85MS` (url=216ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
