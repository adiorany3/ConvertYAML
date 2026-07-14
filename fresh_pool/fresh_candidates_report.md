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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=240ms, nekobox=256ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=227ms, nekobox=276ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-81MS` (url=261ms, nekobox=288ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS` (url=234ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=228ms, nekobox=7178ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-71MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-77MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-77MS` (url=241ms, nekobox=269ms, status=yes)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-75MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-97MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-73MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-87MS` (url=270ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-71MS` (url=247ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-83MS` (url=281ms, status=HTTP 204)
15. `AKUN-015-MYBB-VLESS-WS-83MS` (url=257ms, status=HTTP 204)
16. `AKUN-016-MEDIUM-VLESS-WS-97MS` (url=246ms, status=HTTP 204)
17. `AKUN-017-ADF-VLESS-WS-118MS` (url=253ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-96MS` (url=233ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-82MS` (url=266ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-87MS` (url=246ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-98MS` (url=237ms, status=HTTP 204)
22. `AKUN-022-466688-VLESS-WS-107MS` (url=252ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-136MS` (url=258ms, status=HTTP 204)
24. `AKUN-024-US-VLESS-WS-117MS` (url=241ms, status=HTTP 204)
25. `AKUN-025-SHOPIFY-VLESS-WS-115MS` (url=246ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
