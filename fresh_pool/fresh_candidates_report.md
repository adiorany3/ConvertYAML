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
1. `AKUN-001-UNKNOWN-VLESS-WS-90MS` (url=231ms, nekobox=263ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-121MS` (url=254ms, nekobox=294ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-120MS` (url=233ms, nekobox=276ms, status=yes)
4. `AKUN-004-ZOOM-VLESS-WS-149MS` (url=212ms, nekobox=240ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-151MS` (url=330ms, nekobox=358ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-123MS` (url=258ms, nekobox=262ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-164MS` (url=256ms, nekobox=285ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-137MS` (url=254ms, nekobox=269ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-182MS` (url=252ms, nekobox=257ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-183MS` (url=218ms, nekobox=257ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-123MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-169MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-106MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-129MS` (url=265ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-100MS` (url=253ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-128MS` (url=237ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-118MS` (url=273ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-185MS` (url=233ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-97MS` (url=236ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-109MS` (url=216ms, status=HTTP 204)
21. `AKUN-021-INTERNETWORKS-45-131-210-VLESS-WS-366MS` (url=747ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-375MS` (url=772ms, status=HTTP 204)
23. `AKUN-023-DEV-VLESS-WS-409MS` (url=2280ms, status=HTTP 204)
24. `AKUN-024-DEV-VLESS-WS-427MS` (url=3992ms, status=HTTP 204)
25. `AKUN-025-DEV-VLESS-WS-423MS` (url=2825ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
