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
1. `AKUN-001-ORACLE-VLESS-WS-67MS` (url=232ms, nekobox=266ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=243ms, nekobox=263ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS` (url=263ms, nekobox=189ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-89MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-85MS`
6. `AKUN-005-BIGCOMMERCE-VLESS-WS-84MS`
7. `AKUN-006-COMPREND-NET-VLESS-WS-92MS`
8. `AKUN-007-COMPREND-NET-VLESS-WS-90MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-96MS` (url=252ms, nekobox=201ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-88MS` (url=262ms, nekobox=212ms, status=no)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-84MS` (url=260ms, nekobox=209ms, status=no)
12. `AKUN-012-DEV-VLESS-WS-83MS` (url=249ms, nekobox=198ms, status=no)
13. `AKUN-008-UNKNOWN-VLESS-WS-90MS`
14. `AKUN-009-UNKNOWN-VLESS-WS-91MS`
15. `AKUN-010-UNKNOWN-VLESS-WS-103MS`
16. `AKUN-016-UNKNOWN-VLESS-WS-83MS` (url=264ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-96MS` (url=280ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-115MS` (url=259ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-120MS` (url=291ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-252MS` (url=549ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-273MS` (url=602ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-285MS` (url=574ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-287MS` (url=668ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-292MS` (url=793ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-299MS` (url=631ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
