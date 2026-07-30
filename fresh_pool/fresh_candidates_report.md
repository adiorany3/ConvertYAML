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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=232ms, nekobox=271ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=232ms, nekobox=252ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-65MS` (url=235ms, nekobox=300ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS` (url=234ms, nekobox=299ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-65MS` (url=198ms, nekobox=7177ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-74MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-72MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS`
10. `AKUN-009-BIGCOMMERCE-VLESS-WS-83MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-77MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-100MS` (url=252ms, status=HTTP 204)
13. `AKUN-013-CCWU-VLESS-WS-99MS` (url=269ms, status=HTTP 204)
14. `AKUN-014-SPEEDTEST-VLESS-WS-75MS` (url=263ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-81MS` (url=230ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-90MS` (url=320ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-109MS` (url=262ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-86MS` (url=306ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-75MS` (url=240ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-118MS` (url=229ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-106MS` (url=237ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-131MS` (url=260ms, status=HTTP 204)
23. `AKUN-023-MYBB-VLESS-WS-78MS` (url=310ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-125MS` (url=231ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-83MS` (url=237ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
