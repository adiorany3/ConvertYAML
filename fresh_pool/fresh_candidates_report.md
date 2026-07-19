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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=224ms, nekobox=245ms, status=yes)
2. `AKUN-002-SAVVY-7-VLESS-WS-64MS` (url=241ms, nekobox=280ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-62MS` (url=218ms, nekobox=247ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-72MS` (url=232ms, nekobox=258ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=262ms, nekobox=262ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-74MS` (url=238ms, nekobox=274ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-75MS` (url=287ms, nekobox=267ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS` (url=242ms, nekobox=261ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-71MS` (url=224ms, nekobox=7176ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-65MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-64MS`
12. `AKUN-012-DEV-VLESS-WS-77MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-466688-VLESS-WS-77MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-89MS` (url=231ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-77MS` (url=231ms, status=HTTP 204)
16. `AKUN-017-ES-FORNEX-20160629-VLESS-WS-71MS` (url=239ms, status=HTTP 204)
17. `AKUN-018-WPENG-VLESS-WS-88MS` (url=227ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-91MS` (url=263ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-102MS` (url=232ms, status=HTTP 204)
20. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-99MS` (url=256ms, status=HTTP 204)
21. `AKUN-022-RTCOMM-SRAVNI-RU-VLESS-WS-87MS` (url=231ms, status=HTTP 204)
22. `AKUN-023-BGP48-HK-VLESS-WS-87MS` (url=239ms, status=HTTP 204)
23. `AKUN-024-UK-GB-DCL-01-20191003-VLESS-WS-114MS` (url=257ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-122MS` (url=295ms, status=HTTP 204)
25. `AKUN-026-NEXUSMODS-VLESS-WS-99MS` (url=306ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
