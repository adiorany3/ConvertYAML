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
1. `AKUN-001-UNKNOWN-VLESS-WS-76MS` (url=205ms, nekobox=252ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-78MS` (url=210ms, nekobox=262ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-89MS` (url=227ms, nekobox=257ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=223ms, nekobox=260ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS` (url=232ms, nekobox=251ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-105MS` (url=229ms, nekobox=241ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-103MS` (url=203ms, nekobox=239ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-104MS` (url=230ms, nekobox=292ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-86MS` (url=214ms, nekobox=266ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS` (url=239ms, nekobox=236ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-101MS` (url=225ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-131MS` (url=256ms, status=HTTP 204)
13. `AKUN-013-WEBEX-VLESS-WS-87MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-109MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-86MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-95MS` (url=232ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-99MS` (url=210ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-139MS` (url=269ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-133MS` (url=231ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-126MS` (url=205ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-107MS` (url=259ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-369MS` (url=817ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-248MS` (url=1468ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-373MS` (url=791ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-659MS` (url=1085ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
