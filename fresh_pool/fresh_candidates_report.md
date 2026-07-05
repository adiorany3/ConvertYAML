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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=205ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=239ms, nekobox=259ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=209ms, nekobox=228ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-77MS` (url=209ms, nekobox=232ms, status=yes)
5. `AKUN-005-WEBEX-VLESS-WS-70MS` (url=204ms, nekobox=242ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-81MS` (url=217ms, nekobox=245ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-86MS` (url=219ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-69MS` (url=233ms, nekobox=254ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-69MS` (url=226ms, nekobox=240ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-79MS` (url=211ms, nekobox=238ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-88MS` (url=199ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-77MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-78MS` (url=203ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-91MS` (url=227ms, status=HTTP 204)
15. `AKUN-015-WEYRO-NET-VLESS-WS-87MS` (url=233ms, status=HTTP 204)
16. `AKUN-016-WEBEX-VLESS-WS-98MS` (url=209ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-154MS` (url=246ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-227MS` (url=486ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-176MS` (url=868ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-252MS` (url=532ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-248MS` (url=535ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-259MS` (url=530ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-260MS` (url=531ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-233MS` (url=483ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-76MS` (url=213ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
