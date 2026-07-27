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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-93MS` (url=217ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-97MS` (url=247ms, nekobox=262ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-96MS` (url=337ms, nekobox=260ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-99MS` (url=213ms, nekobox=255ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-100MS` (url=251ms, nekobox=254ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=221ms, nekobox=250ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-95MS` (url=230ms, nekobox=261ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-101MS` (url=240ms, nekobox=237ms, status=yes)
9. `AKUN-009-008500-VLESS-WS-99MS` (url=216ms, nekobox=262ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-101MS` (url=230ms, nekobox=249ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-104MS` (url=246ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-99MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-103MS` (url=290ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-102MS` (url=273ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-114MS` (url=211ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-101MS` (url=257ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-115MS` (url=273ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-113MS` (url=239ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-105MS` (url=222ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-102MS` (url=256ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-96MS` (url=235ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-113MS` (url=221ms, status=HTTP 204)
23. `AKUN-023-1PASSWORD-VLESS-WS-93MS` (url=221ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-107MS` (url=262ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-321MS` (url=4922ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
