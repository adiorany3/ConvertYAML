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
1. `AKUN-001-UNKNOWN-VLESS-WS-80MS` (url=236ms, nekobox=249ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-80MS` (url=235ms, nekobox=259ms, status=yes)
3. `AKUN-003-BIGCOMMERCE-VLESS-WS-87MS` (url=233ms, nekobox=238ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-90MS` (url=230ms, nekobox=254ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS` (url=208ms, nekobox=229ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS` (url=203ms, nekobox=190ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-107MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS` (url=213ms, nekobox=190ms, status=no)
9. `AKUN-007-ALIBABA-VLESS-WS-135MS`
10. `AKUN-008-DE-XTOM-20210903-VLESS-WS-95MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-128MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-109MS` (url=238ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-129MS` (url=229ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-113MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-240MS` (url=424ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-249MS` (url=513ms, status=HTTP 204)
18. `AKUN-018-SPEEDTEST-VLESS-WS-271MS` (url=590ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-272MS` (url=570ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-289MS` (url=562ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-238MS` (url=1291ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-279MS` (url=608ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-97MS` (url=244ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-345MS` (url=570ms, status=HTTP 204)
25. `AKUN-025-MICROSOFT-VLESS-WS-276MS` (url=587ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
