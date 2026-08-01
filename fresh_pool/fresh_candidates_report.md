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
1. `AKUN-001-UNKNOWN-VLESS-WS-59MS` (url=243ms, nekobox=279ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-63MS` (url=226ms, nekobox=275ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS` (url=233ms, nekobox=279ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS` (url=230ms, nekobox=254ms, status=yes)
5. `AKUN-005-008500-VLESS-WS-67MS` (url=224ms, nekobox=268ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-69MS` (url=3619ms, status=SSLError: HTTPSConnectionPool(host='www.gstatic.com', port=443): Max retries exceeded with url: /generate_204 (Caused by SSLError()
7. `AKUN-007-CLOUDFLARE-VLESS-WS-63MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-71MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-66MS`
10. `AKUN-010-DEV-VLESS-WS-63MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-71MS` (url=217ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-103MS` (url=233ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-85MS` (url=279ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-89MS` (url=222ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-66MS` (url=239ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-74MS` (url=233ms, status=HTTP 204)
17. `AKUN-018-DEV-VLESS-WS-76MS` (url=228ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-69MS` (url=250ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-68MS` (url=288ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-73MS` (url=240ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-117MS` (url=229ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-85MS` (url=240ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-177MS` (url=236ms, status=HTTP 204)
24. `AKUN-025-1PASSWORD-VLESS-WS-91MS` (url=252ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-73MS` (url=241ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
