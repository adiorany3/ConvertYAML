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
1. `AKUN-001-UNKNOWN-VLESS-WS-75MS` (url=218ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=203ms, nekobox=247ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-85MS` (url=228ms, nekobox=449ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-91MS` (url=213ms, nekobox=248ms, status=yes)
5. `AKUN-005-466688-VLESS-WS-79MS` (url=202ms, nekobox=262ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-94MS` (url=213ms, nekobox=256ms, status=yes)
7. `AKUN-007-UK-GB-DCL-01-20191003-VLESS-WS-116MS` (url=280ms, nekobox=248ms, status=yes)
8. `AKUN-008-DE-XTOM-20210903-VLESS-WS-121MS` (url=218ms, nekobox=250ms, status=yes)
9. `AKUN-009-ALIBABA-VLESS-WS-96MS` (url=225ms, nekobox=246ms, status=yes)
10. `AKUN-010-TENCENT-VLESS-WS-148MS` (url=267ms, nekobox=265ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-150MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-242MS` (url=520ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-248MS` (url=554ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-257MS` (url=528ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-273MS` (url=597ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-296MS` (url=548ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-299MS` (url=569ms, status=HTTP 204)
19. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-273MS` (url=550ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-107MS` (url=214ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-444MS` (url=470ms, status=HTTP 204)
22. `AKUN-027-UNKNOWN-VLESS-WS-486MS` (url=823ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-478MS` (url=486ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-249MS` (url=505ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-251MS` (url=511ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
