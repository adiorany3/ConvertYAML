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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-82MS` (url=225ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-79MS` (url=220ms, nekobox=257ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-90MS` (url=226ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-91MS` (url=230ms, nekobox=7179ms, status=no)
5. `AKUN-004-WPENG-VLESS-WS-95MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-102MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-89MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-97MS`
11. `AKUN-010-CZ-LOTUNA-19970206-VLESS-WS-99MS`
12. `AKUN-012-DEV-VLESS-WS-100MS` (url=233ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-105MS` (url=237ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-95MS` (url=235ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-104MS` (url=236ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-90MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-91MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-103MS` (url=220ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-87MS` (url=227ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-88MS` (url=203ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-116MS` (url=230ms, status=HTTP 204)
22. `AKUN-022-VOV-VLESS-WS-117MS` (url=216ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-122MS` (url=203ms, status=HTTP 204)
24. `AKUN-024-SHOPIFY-VLESS-WS-88MS` (url=233ms, status=HTTP 204)
25. `AKUN-025-MEDIUM-VLESS-WS-111MS` (url=200ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
