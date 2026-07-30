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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=207ms, nekobox=259ms, status=yes)
2. `AKUN-002-SPEEDTEST-VLESS-WS-60MS` (url=227ms, nekobox=183ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-67MS`
4. `AKUN-003-BIGCOMMERCE-VLESS-WS-67MS`
5. `AKUN-004-LEVIKOGJGFDD-VLESS-WS-63MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-66MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-58MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-70MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-69MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-75MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-70MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-59MS` (url=207ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-62MS` (url=205ms, status=HTTP 204)
14. `AKUN-014-CCWU-VLESS-WS-74MS` (url=203ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-67MS` (url=219ms, status=HTTP 204)
16. `AKUN-016-LEVIKOGJGFDD-VLESS-WS-61MS` (url=200ms, status=HTTP 204)
17. `AKUN-017-SPEEDTEST-VLESS-WS-68MS` (url=240ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-70MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-106MS` (url=214ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-89MS` (url=290ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-125MS` (url=230ms, status=HTTP 204)
22. `AKUN-023-LEVIKOGJGFDD-VLESS-WS-175MS` (url=269ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-85MS` (url=215ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-59MS` (url=205ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-67MS` (url=209ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
