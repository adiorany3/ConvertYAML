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
1. `AKUN-001-UNKNOWN-VLESS-WS-59MS` (url=224ms, nekobox=249ms, status=yes)
2. `AKUN-002-OVH-VLESS-WS-59MS` (url=202ms, nekobox=259ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-67MS` (url=233ms, nekobox=264ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-71MS` (url=268ms, nekobox=261ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-72MS` (url=229ms, nekobox=240ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-82MS` (url=240ms, nekobox=263ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-99MS` (url=229ms, nekobox=243ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-83MS` (url=275ms, nekobox=252ms, status=yes)
9. `AKUN-009-090227-VLESS-WS-121MS` (url=279ms, nekobox=263ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-104MS` (url=235ms, nekobox=183ms, status=no)
11. `AKUN-010-WPENG-VLESS-WS-81MS`
12. `AKUN-012-WEYRO-NET-VLESS-WS-94MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-69MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-138MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-88MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-78MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-112MS` (url=292ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-359MS` (url=733ms, status=HTTP 204)
19. `AKUN-019-SPEEDTEST-VLESS-WS-363MS` (url=750ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-376MS` (url=825ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-380MS` (url=782ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-388MS` (url=821ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-381MS` (url=841ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-387MS` (url=826ms, status=HTTP 204)
25. `AKUN-025-RAVANPLUS-VLESS-WS-464MS` (url=962ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
