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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=203ms, nekobox=244ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-78MS` (url=205ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS` (url=222ms, nekobox=180ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS`
5. `AKUN-004-SHOPIFY-VLESS-WS-75MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-69MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-85MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS`
9. `AKUN-008-ZVC-VLESS-WS-68MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-72MS` (url=207ms, nekobox=7178ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-78MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-71MS` (url=222ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-92MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-73MS` (url=207ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-77MS` (url=217ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-75MS` (url=214ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-80MS` (url=200ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-71MS` (url=200ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-102MS` (url=199ms, status=HTTP 204)
21. `AKUN-021-ZVC-VLESS-WS-109MS` (url=290ms, status=HTTP 204)
22. `AKUN-023-MYBB-VLESS-WS-75MS` (url=200ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-99MS` (url=214ms, status=HTTP 204)
24. `AKUN-025-MEDIUM-VLESS-WS-79MS` (url=218ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-228MS` (url=494ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
