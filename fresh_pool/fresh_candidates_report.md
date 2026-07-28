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
1. `AKUN-001-CCWU-VLESS-WS-59MS` (url=222ms, nekobox=254ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-59MS` (url=216ms, nekobox=259ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-62MS` (url=216ms, nekobox=246ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS` (url=222ms, nekobox=247ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-68MS` (url=218ms, nekobox=248ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-67MS` (url=226ms, nekobox=234ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-74MS` (url=200ms, nekobox=228ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-64MS` (url=215ms, nekobox=246ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-56MS` (url=203ms, nekobox=233ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-57MS` (url=196ms, nekobox=244ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-57MS` (url=210ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-135MS` (url=220ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-63MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-63MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-68MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-65MS` (url=222ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-64MS` (url=225ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-58MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-58MS` (url=223ms, status=HTTP 204)
20. `AKUN-020-008500-VLESS-WS-62MS` (url=220ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-154MS` (url=246ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-63MS` (url=196ms, status=HTTP 204)
23. `AKUN-023-DEV-VLESS-WS-66MS` (url=219ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-59MS` (url=298ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-70MS` (url=221ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
