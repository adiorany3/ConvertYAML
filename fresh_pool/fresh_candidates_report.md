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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-79MS` (url=211ms, nekobox=238ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-79MS` (url=199ms, nekobox=262ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=214ms, nekobox=235ms, status=yes)
4. `AKUN-004-154-83-95-0-154-83-95-25-VLESS-WS-90MS` (url=204ms, nekobox=289ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-96MS` (url=213ms, nekobox=242ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-102MS` (url=226ms, nekobox=239ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-66MS` (url=215ms, nekobox=235ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS` (url=238ms, nekobox=254ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS` (url=205ms, nekobox=247ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS` (url=212ms, nekobox=239ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-82MS` (url=207ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-80MS` (url=216ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-119MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-94MS` (url=202ms, status=HTTP 204)
15. `AKUN-015-WEBEX-VLESS-WS-91MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-62MS` (url=200ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-67MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-SPEEDTEST-VLESS-WS-175MS` (url=393ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-248MS` (url=552ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-232MS` (url=534ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-297MS` (url=550ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-232MS` (url=488ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-229MS` (url=484ms, status=HTTP 204)
24. `AKUN-030-PERSIANSHIELD-VLESS-WS-444MS` (url=737ms, status=HTTP 204)
25. `AKUN-031-UNKNOWN-VLESS-WS-457MS` (url=726ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
