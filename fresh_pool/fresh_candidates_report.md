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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=219ms, nekobox=260ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=221ms, nekobox=252ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-61MS` (url=232ms, nekobox=272ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-63MS` (url=239ms, nekobox=250ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-75MS` (url=272ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-64MS` (url=220ms, nekobox=247ms, status=yes)
7. `AKUN-007-UK-GB-DCL-01-20191003-VLESS-WS-81MS` (url=226ms, nekobox=258ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-85MS` (url=217ms, nekobox=250ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-84MS` (url=237ms, nekobox=246ms, status=yes)
10. `AKUN-010-GO-DADDY-COM-LLC-VLESS-WS-86MS` (url=238ms, nekobox=271ms, status=yes)
11. `AKUN-011-UK-GB-DCL-01-20191003-VLESS-WS-95MS` (url=241ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-98MS` (url=243ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-93MS` (url=266ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-79MS` (url=230ms, status=HTTP 204)
15. `AKUN-015-US-VLESS-WS-110MS` (url=240ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-109MS` (url=218ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-129MS` (url=209ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-136MS` (url=210ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-98MS` (url=1243ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-125MS` (url=209ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-93MS` (url=270ms, status=HTTP 204)
22. `AKUN-023-WEBEX-VLESS-WS-80MS` (url=234ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-140MS` (url=228ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-344MS` (url=1108ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-356MS` (url=789ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
