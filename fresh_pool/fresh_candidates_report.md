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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=230ms, nekobox=256ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=218ms, nekobox=240ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-62MS` (url=201ms, nekobox=282ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-66MS` (url=223ms, nekobox=252ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-68MS` (url=222ms, nekobox=268ms, status=yes)
6. `AKUN-006-WEBEX-VLESS-WS-64MS` (url=222ms, nekobox=242ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-61MS` (url=223ms, nekobox=264ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-72MS` (url=231ms, nekobox=249ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-74MS` (url=216ms, nekobox=244ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-95MS` (url=255ms, nekobox=247ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-86MS` (url=235ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-92MS` (url=226ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-90MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-117MS` (url=200ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-83MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-ZOOM-VLESS-WS-63MS` (url=227ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-71MS` (url=249ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-104MS` (url=255ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-144MS` (url=387ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-348MS` (url=5705ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-354MS` (url=805ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-508MS` (url=900ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-641MS` (url=1002ms, status=HTTP 204)
24. `AKUN-029-DEV-VLESS-WS-406MS` (url=900ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-707MS` (url=1094ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
