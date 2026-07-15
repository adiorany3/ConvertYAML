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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=218ms, nekobox=228ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=229ms, nekobox=248ms, status=yes)
3. `AKUN-003-CZ-LOTUNA-19970206-VLESS-WS-60MS` (url=218ms, nekobox=229ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-73MS` (url=211ms, nekobox=230ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS` (url=215ms, nekobox=258ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=217ms, nekobox=248ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS` (url=240ms, nekobox=316ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS` (url=239ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=233ms, nekobox=230ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-94MS` (url=223ms, nekobox=266ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-100MS` (url=230ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-90MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-73MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-91MS` (url=277ms, status=HTTP 204)
15. `AKUN-015-CZ-LOTUNA-19970206-VLESS-WS-93MS` (url=264ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-101MS` (url=204ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-149MS` (url=302ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-124MS` (url=230ms, status=HTTP 204)
19. `AKUN-019-NEXUSMODS-VLESS-WS-118MS` (url=221ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-348MS` (url=749ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-243MS` (url=801ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-365MS` (url=790ms, status=HTTP 204)
23. `AKUN-023-SPEEDTEST-VLESS-WS-396MS` (url=2239ms, status=HTTP 204)
24. `AKUN-025-SPEEDTEST-VLESS-WS-116MS` (url=754ms, status=HTTP 204)
25. `AKUN-030-GOOGLE-VLESS-WS-761MS` (url=1241ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
