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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=241ms, nekobox=265ms, status=yes)
2. `AKUN-002-090227-VLESS-WS-67MS` (url=235ms, nekobox=265ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=245ms, nekobox=264ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS` (url=243ms, nekobox=280ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS` (url=248ms, nekobox=195ms, status=no)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=248ms, nekobox=178ms, status=no)
7. `AKUN-005-WEBEX-VLESS-WS-90MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=282ms, nekobox=208ms, status=no)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-88MS` (url=268ms, nekobox=178ms, status=no)
10. `AKUN-006-BIGCOMMERCE-VLESS-WS-109MS`
11. `AKUN-007-DIXONS-VLESS-WS-107MS`
12. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS`
13. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-122MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-95MS` (url=249ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-110MS` (url=237ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-115MS` (url=259ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-87MS` (url=261ms, status=HTTP 204)
19. `AKUN-019-3666888-VLESS-WS-121MS` (url=264ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-101MS` (url=258ms, status=HTTP 204)
21. `AKUN-021-1PASSWORD-VLESS-WS-131MS` (url=260ms, status=HTTP 204)
22. `AKUN-022-SHOPIFY-VLESS-WS-123MS` (url=249ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-144MS` (url=264ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-113MS` (url=295ms, status=HTTP 204)
25. `AKUN-025-ADF-VLESS-WS-154MS` (url=259ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
