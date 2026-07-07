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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=223ms, nekobox=260ms, status=yes)
2. `AKUN-002-ORACLE-VLESS-WS-59MS` (url=210ms, nekobox=253ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-61MS` (url=230ms, nekobox=235ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-61MS` (url=208ms, nekobox=240ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-66MS` (url=223ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-67MS` (url=211ms, nekobox=242ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-63MS` (url=214ms, nekobox=272ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-63MS` (url=208ms, nekobox=240ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-59MS` (url=218ms, nekobox=252ms, status=yes)
10. `AKUN-010-DIGITALOCEAN-VLESS-WS-73MS` (url=244ms, nekobox=256ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-83MS` (url=212ms, status=HTTP 204)
12. `AKUN-012-WEBEX-VLESS-WS-76MS` (url=220ms, status=HTTP 204)
13. `AKUN-013-466688-VLESS-WS-62MS` (url=243ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-87MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-100MS` (url=237ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-98MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-115MS` (url=229ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-67MS` (url=280ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-74MS` (url=308ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-67MS` (url=228ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-354MS` (url=747ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-354MS` (url=811ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-354MS` (url=743ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-384MS` (url=799ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-373MS` (url=791ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
