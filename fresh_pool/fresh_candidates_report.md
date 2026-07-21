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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=239ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=223ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-61MS` (url=223ms, nekobox=258ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=308ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-66MS` (url=221ms, nekobox=248ms, status=yes)
6. `AKUN-006-UK-GB-DCL-01-20191003-VLESS-WS-80MS` (url=231ms, nekobox=287ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-86MS` (url=223ms, nekobox=230ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS` (url=240ms, nekobox=234ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS` (url=229ms, nekobox=254ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-100MS` (url=204ms, nekobox=258ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-73MS` (url=209ms, status=HTTP 204)
12. `AKUN-012-SHOPIFY-VLESS-WS-92MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-92MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-90MS` (url=259ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-87MS` (url=230ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-118MS` (url=211ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-105MS` (url=216ms, status=HTTP 204)
18. `AKUN-018-MEDIUM-VLESS-WS-72MS` (url=212ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-132MS` (url=232ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-126MS` (url=211ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-105MS` (url=242ms, status=HTTP 204)
22. `AKUN-022-PAGES-VLESS-WS-81MS` (url=234ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-83MS` (url=212ms, status=HTTP 204)
24. `AKUN-024-1PASSWORD-VLESS-WS-67MS` (url=246ms, status=HTTP 204)
25. `AKUN-025-WEBEX-VLESS-WS-75MS` (url=229ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
