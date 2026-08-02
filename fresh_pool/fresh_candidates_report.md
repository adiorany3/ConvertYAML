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
1. `AKUN-001-UNKNOWN-VLESS-WS-56MS` (url=219ms, nekobox=234ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-72MS` (url=220ms, nekobox=236ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=212ms, nekobox=7177ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-63MS`
6. `AKUN-006-SPEEDTEST-VLESS-WS-72MS` (url=199ms, nekobox=170ms, status=no)
7. `AKUN-005-SEECK-VLESS-WS-81MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS`
9. `AKUN-007-008500-VLESS-WS-75MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-71MS`
12. `AKUN-012-SPEEDTEST-VLESS-WS-83MS` (url=219ms, nekobox=170ms, status=no)
13. `AKUN-010-CLOUDFLARE-VLESS-WS-67MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-70MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-91MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-96MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-109MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-97MS` (url=222ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-87MS` (url=224ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-95MS` (url=221ms, status=HTTP 204)
21. `AKUN-021-EE-WELCOMEHOST-20190515-VLESS-WS-119MS` (url=211ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-94MS` (url=211ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-147MS` (url=214ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-132MS` (url=211ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-105MS` (url=230ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
