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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS` (url=229ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=231ms, nekobox=254ms, status=yes)
3. `AKUN-003-CZ-LOTUNA-19970206-VLESS-WS-87MS` (url=240ms, nekobox=239ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=225ms, nekobox=232ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS` (url=203ms, nekobox=286ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=200ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=210ms, nekobox=245ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-92MS` (url=234ms, nekobox=263ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS` (url=212ms, nekobox=232ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-88MS` (url=259ms, nekobox=237ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-89MS` (url=218ms, status=HTTP 204)
12. `AKUN-012-WEBEX-VLESS-WS-96MS` (url=259ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-110MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-97MS` (url=230ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS` (url=219ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-118MS` (url=218ms, status=HTTP 204)
17. `AKUN-017-NEXUSMODS-VLESS-WS-106MS` (url=240ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-142MS` (url=212ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-150MS` (url=270ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-150MS` (url=202ms, status=HTTP 204)
21. `AKUN-022-466688-VLESS-WS-158MS` (url=211ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-137MS` (url=233ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-229MS` (url=518ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-238MS` (url=534ms, status=HTTP 204)
25. `AKUN-026-SPEEDTEST-VLESS-WS-246MS` (url=553ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
