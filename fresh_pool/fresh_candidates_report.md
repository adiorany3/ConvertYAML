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
1. `AKUN-001-UK-GB-DCL-01-20191003-VLESS-WS-61MS` (url=198ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-67MS` (url=216ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=219ms, nekobox=251ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-63MS` (url=203ms, nekobox=241ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=230ms, nekobox=237ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS` (url=228ms, nekobox=256ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-64MS` (url=214ms, nekobox=253ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS` (url=224ms, nekobox=254ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-75MS` (url=217ms, nekobox=248ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS` (url=209ms, nekobox=242ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-103MS` (url=231ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-90MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-119MS` (url=233ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-76MS` (url=209ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-134MS` (url=202ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-133MS` (url=205ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-121MS` (url=218ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-352MS` (url=758ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-364MS` (url=764ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-403MS` (url=825ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-396MS` (url=873ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-395MS` (url=824ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-403MS` (url=841ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-381MS` (url=625ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
