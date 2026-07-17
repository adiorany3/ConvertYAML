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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=217ms, nekobox=245ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-89MS` (url=222ms, nekobox=242ms, status=yes)
3. `AKUN-003-CZ-LOTUNA-19970206-VLESS-WS-80MS` (url=207ms, nekobox=260ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-92MS` (url=228ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=234ms, nekobox=257ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=227ms, nekobox=231ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS` (url=235ms, nekobox=259ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-85MS` (url=220ms, nekobox=261ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS` (url=205ms, nekobox=239ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS` (url=241ms, nekobox=7170ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-81MS` (url=221ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-97MS` (url=202ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-102MS` (url=231ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-109MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-103MS` (url=278ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-105MS` (url=220ms, status=HTTP 204)
18. `AKUN-018-WEBEX-VLESS-WS-114MS` (url=202ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-94MS` (url=230ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-110MS` (url=218ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-124MS` (url=230ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-105MS` (url=205ms, status=HTTP 204)
23. `AKUN-023-POLICE-VLESS-WS-121MS` (url=226ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-130MS` (url=233ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-133MS` (url=207ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
