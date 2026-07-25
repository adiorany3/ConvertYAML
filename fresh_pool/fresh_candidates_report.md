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
1. `AKUN-001-UNKNOWN-VLESS-WS-71MS` (url=228ms, nekobox=243ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-78MS` (url=232ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS` (url=214ms, nekobox=256ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=213ms, nekobox=240ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS` (url=224ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-112MS` (url=300ms, nekobox=296ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-122MS` (url=242ms, nekobox=267ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-75MS` (url=223ms, nekobox=243ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS` (url=228ms, nekobox=261ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-87MS` (url=215ms, nekobox=252ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-138MS` (url=263ms, status=HTTP 204)
12. `AKUN-012-GOOGLE-VLESS-WS-78MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-77MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-147MS` (url=242ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-126MS` (url=248ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-162MS` (url=321ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-144MS` (url=231ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-69MS` (url=224ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-141MS` (url=235ms, status=HTTP 204)
20. `AKUN-021-ZOOM-VLESS-WS-73MS` (url=199ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-166MS` (url=321ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-357MS` (url=3464ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-365MS` (url=788ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-383MS` (url=770ms, status=HTTP 204)
25. `AKUN-027-SUKARIO-VLESS-WS-642MS` (url=1049ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
