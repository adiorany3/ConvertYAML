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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-89MS` (url=206ms, nekobox=231ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-93MS` (url=203ms, nekobox=241ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS` (url=201ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-102MS` (url=206ms, nekobox=234ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-100MS` (url=229ms, nekobox=242ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=218ms, nekobox=254ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-108MS` (url=223ms, nekobox=288ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-126MS` (url=217ms, nekobox=259ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-135MS` (url=218ms, nekobox=272ms, status=yes)
10. `AKUN-010-GO-DADDY-COM-LLC-VLESS-WS-93MS` (url=248ms, nekobox=243ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-112MS` (url=234ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-124MS` (url=203ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-147MS` (url=252ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-103MS` (url=229ms, status=HTTP 204)
15. `AKUN-015-US-VLESS-WS-111MS` (url=262ms, status=HTTP 204)
16. `AKUN-016-WEBEX-VLESS-WS-110MS` (url=264ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-112MS` (url=203ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-98MS` (url=232ms, status=HTTP 204)
19. `AKUN-020-DEV-VLESS-WS-124MS` (url=228ms, status=HTTP 204)
20. `AKUN-021-466688-VLESS-WS-107MS` (url=254ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-109MS` (url=229ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-123MS` (url=360ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-102MS` (url=239ms, status=HTTP 204)
24. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-222MS` (url=627ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-245MS` (url=841ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
