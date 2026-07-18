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
1. `AKUN-001-UNKNOWN-VLESS-WS-62MS` (url=228ms, nekobox=233ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-70MS` (url=215ms, nekobox=226ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-81MS` (url=218ms, nekobox=234ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-80MS` (url=211ms, nekobox=229ms, status=yes)
5. `AKUN-005-DIXONS-VLESS-WS-87MS` (url=213ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=217ms, nekobox=248ms, status=yes)
7. `AKUN-007-466688-VLESS-WS-93MS` (url=216ms, nekobox=258ms, status=yes)
8. `AKUN-008-466688-VLESS-WS-85MS` (url=214ms, nekobox=255ms, status=yes)
9. `AKUN-009-BGP48-HK-VLESS-WS-75MS` (url=217ms, nekobox=247ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-94MS` (url=205ms, nekobox=264ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-86MS` (url=208ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-78MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-UK-GB-DCL-01-20191003-VLESS-WS-110MS` (url=205ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-115MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-104MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-UK-GB-DCL-01-20191003-VLESS-WS-108MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-117MS` (url=203ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-97MS` (url=212ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-100MS` (url=225ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-115MS` (url=223ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-110MS` (url=217ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-242MS` (url=682ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-242MS` (url=534ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-248MS` (url=505ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-260MS` (url=358ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
