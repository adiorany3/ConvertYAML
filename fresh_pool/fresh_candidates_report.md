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
1. `AKUN-001-UNKNOWN-VLESS-WS-77MS` (url=211ms, nekobox=252ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=225ms, nekobox=241ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-86MS` (url=205ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=204ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=223ms, nekobox=246ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS` (url=198ms, nekobox=229ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-102MS` (url=230ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=202ms, nekobox=263ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-83MS`
10. `AKUN-010-DEV-VLESS-WS-101MS`
11. `AKUN-012-ZVC-VLESS-WS-125MS` (url=213ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-111MS` (url=205ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-91MS` (url=226ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-90MS` (url=219ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-106MS` (url=231ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-118MS` (url=236ms, status=HTTP 204)
17. `AKUN-018-WPENG-VLESS-WS-93MS` (url=223ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-106MS` (url=218ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-145MS` (url=246ms, status=HTTP 204)
20. `AKUN-021-UK-GB-DCL-01-20191003-VLESS-WS-136MS` (url=228ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-139MS` (url=238ms, status=HTTP 204)
22. `AKUN-023-UK-GB-DCL-01-20191003-VLESS-WS-117MS` (url=204ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-110MS` (url=227ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-147MS` (url=311ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-137MS` (url=349ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
