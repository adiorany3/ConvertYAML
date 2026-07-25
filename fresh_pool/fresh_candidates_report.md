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
1. `AKUN-001-UNKNOWN-VLESS-WS-70MS` (url=217ms, nekobox=244ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-72MS` (url=220ms, nekobox=246ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-71MS` (url=216ms, nekobox=246ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-75MS` (url=213ms, nekobox=244ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-77MS` (url=219ms, nekobox=249ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-67MS` (url=200ms, nekobox=248ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-77MS` (url=222ms, nekobox=246ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-85MS` (url=221ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-90MS` (url=216ms, nekobox=240ms, status=yes)
10. `AKUN-010-GOOGLE-VLESS-WS-78MS` (url=223ms, nekobox=239ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-89MS` (url=216ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-111MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-114MS` (url=362ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-75MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-SPEEDTEST-VLESS-WS-81MS` (url=199ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-129MS` (url=329ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-76MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-144MS` (url=366ms, status=HTTP 204)
19. `AKUN-019-3666888-VLESS-WS-92MS` (url=220ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-130MS` (url=242ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-175MS` (url=365ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-133MS` (url=279ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-158MS` (url=325ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-152MS` (url=269ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-115MS` (url=266ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
