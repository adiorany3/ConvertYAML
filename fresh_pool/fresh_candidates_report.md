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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=205ms, nekobox=227ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-88MS` (url=215ms, nekobox=251ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=230ms, nekobox=250ms, status=yes)
4. `AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-89MS` (url=205ms, nekobox=263ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-63MS` (url=203ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS` (url=232ms, nekobox=254ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-91MS` (url=215ms, nekobox=239ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS` (url=209ms, nekobox=235ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-118MS` (url=212ms, nekobox=256ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-80MS` (url=225ms, nekobox=228ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-91MS` (url=218ms, status=HTTP 204)
12. `AKUN-012-CZ-LOTUNA-19970206-VLESS-WS-68MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-124MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-80MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-104MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-67MS` (url=208ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-113MS` (url=225ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-69MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-89MS` (url=221ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-72MS` (url=230ms, status=HTTP 204)
21. `AKUN-021-ZVC-VLESS-WS-89MS` (url=201ms, status=HTTP 204)
22. `AKUN-022-NEXUSMODS-VLESS-WS-92MS` (url=217ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-111MS` (url=212ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-131MS` (url=279ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-73MS` (url=218ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
