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
1. `AKUN-001-UNKNOWN-VLESS-WS-91MS` (url=213ms, nekobox=241ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-103MS` (url=224ms, nekobox=270ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-100MS` (url=223ms, nekobox=261ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-108MS` (url=248ms, nekobox=250ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-109MS` (url=216ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-113MS` (url=218ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-109MS` (url=244ms, nekobox=267ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-112MS` (url=235ms, nekobox=257ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-124MS` (url=255ms, nekobox=285ms, status=yes)
10. `AKUN-010-GO-DADDY-COM-LLC-VLESS-WS-130MS` (url=343ms, nekobox=251ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-119MS` (url=253ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-109MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-140MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-134MS` (url=247ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-121MS` (url=242ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-152MS` (url=258ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-104MS` (url=238ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-148MS` (url=232ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-161MS` (url=241ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-92MS` (url=297ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-115MS` (url=255ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-175MS` (url=230ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-162MS` (url=266ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-177MS` (url=332ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-177MS` (url=238ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
