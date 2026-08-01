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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-69MS` (url=222ms, nekobox=248ms, status=yes)
2. `AKUN-002-ZOOM-VLESS-WS-67MS` (url=228ms, nekobox=243ms, status=yes)
3. `AKUN-003-SPEEDTEST-VLESS-WS-78MS` (url=229ms, nekobox=206ms, status=no)
4. `AKUN-003-UNKNOWN-VLESS-WS-86MS`
5. `AKUN-005-DEV-VLESS-WS-92MS` (url=228ms, nekobox=179ms, status=no)
6. `AKUN-004-UNKNOWN-VLESS-WS-102MS`
7. `AKUN-005-SEECK-VLESS-WS-93MS`
8. `AKUN-006-UNKNOWN-VLESS-WS-101MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-108MS`
10. `AKUN-008-UNKNOWN-VLESS-WS-91MS`
11. `AKUN-011-DEV-VLESS-WS-99MS` (url=228ms, nekobox=209ms, status=no)
12. `AKUN-012-DEV-VLESS-WS-104MS` (url=229ms, nekobox=188ms, status=no)
13. `AKUN-009-UNKNOWN-VLESS-WS-83MS`
14. `AKUN-010-UNKNOWN-VLESS-WS-100MS`
15. `AKUN-015-UNKNOWN-VLESS-WS-125MS` (url=214ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-88MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-107MS` (url=282ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-90MS` (url=227ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-85MS` (url=198ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-240MS` (url=627ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-372MS` (url=742ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-602MS` (url=1028ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-621MS` (url=1033ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-600MS` (url=1082ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-659MS` (url=879ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
