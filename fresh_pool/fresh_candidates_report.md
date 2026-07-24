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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-77MS` (url=212ms, nekobox=230ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-80MS` (url=229ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-85MS` (url=231ms, nekobox=260ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-88MS` (url=280ms, nekobox=7178ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-96MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-97MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-89MS`
12. `AKUN-012-DEV-VLESS-WS-80MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-96MS` (url=200ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-90MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-95MS` (url=224ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-84MS` (url=209ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-101MS` (url=217ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-101MS` (url=222ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-127MS` (url=215ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-91MS` (url=232ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-125MS` (url=258ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-107MS` (url=231ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-115MS` (url=220ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-83MS` (url=205ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-90MS` (url=219ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
