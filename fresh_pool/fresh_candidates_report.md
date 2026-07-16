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
1. `AKUN-001-UNKNOWN-VLESS-WS-74MS` (url=220ms, nekobox=252ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=220ms, nekobox=260ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS` (url=222ms, nekobox=230ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-92MS` (url=217ms, nekobox=232ms, status=yes)
5. `AKUN-005-DIXONS-VLESS-WS-93MS` (url=220ms, nekobox=231ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS` (url=201ms, nekobox=252ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-92MS` (url=225ms, nekobox=229ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-111MS` (url=247ms, nekobox=321ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-115MS` (url=221ms, nekobox=246ms, status=yes)
10. `AKUN-010-GO-DADDY-COM-LLC-VLESS-WS-91MS` (url=233ms, nekobox=232ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-90MS` (url=201ms, status=HTTP 204)
12. `AKUN-012-ORG-VLESS-WS-90MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-132MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-104MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-134MS` (url=212ms, status=HTTP 204)
16. `AKUN-016-WEBEX-VLESS-WS-96MS` (url=236ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-137MS` (url=252ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-121MS` (url=223ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-101MS` (url=214ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-168MS` (url=245ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-165MS` (url=220ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-146MS` (url=240ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-258MS` (url=615ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-255MS` (url=1003ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-268MS` (url=613ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
