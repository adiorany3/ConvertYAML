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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-69MS` (url=224ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=218ms, nekobox=257ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-70MS` (url=221ms, nekobox=243ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=230ms, nekobox=242ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-72MS` (url=230ms, nekobox=254ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-88MS` (url=211ms, nekobox=255ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-73MS` (url=234ms, nekobox=240ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-112MS` (url=221ms, nekobox=250ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-83MS` (url=228ms, nekobox=252ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-77MS` (url=218ms, nekobox=261ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-111MS` (url=219ms, status=HTTP 204)
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-125MS` (url=227ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-100MS` (url=205ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-101MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-93MS` (url=235ms, status=HTTP 204)
17. `AKUN-017-ZOOM-VLESS-WS-129MS` (url=199ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-96MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-128MS` (url=227ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-138MS` (url=202ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-122MS` (url=217ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-129MS` (url=226ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-91MS` (url=221ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-356MS` (url=816ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-363MS` (url=813ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
