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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-90MS` (url=221ms, nekobox=234ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-91MS` (url=205ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS` (url=226ms, nekobox=235ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-98MS` (url=225ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-97MS` (url=206ms, nekobox=242ms, status=yes)
6. `AKUN-006-CCWU-VLESS-WS-102MS` (url=221ms, nekobox=269ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-95MS` (url=220ms, nekobox=273ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=211ms, nekobox=277ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS` (url=201ms, nekobox=242ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-100MS` (url=244ms, nekobox=258ms, status=yes)
11. `AKUN-011-008500-VLESS-WS-107MS` (url=239ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-98MS` (url=252ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-97MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-108MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-101MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-104MS` (url=216ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-120MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-SHOPIFY-VLESS-WS-140MS` (url=237ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-163MS` (url=248ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-114MS` (url=249ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-98MS` (url=305ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-136MS` (url=367ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-144MS` (url=224ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-103MS` (url=252ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-109MS` (url=218ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
