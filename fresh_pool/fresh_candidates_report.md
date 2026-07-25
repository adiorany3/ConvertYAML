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
1. `AKUN-001-UNKNOWN-VLESS-WS-86MS` (url=209ms, nekobox=253ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-87MS` (url=205ms, nekobox=232ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-86MS` (url=235ms, nekobox=234ms, status=yes)
4. `AKUN-004-WEBEX-VLESS-WS-85MS` (url=212ms, nekobox=263ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-100MS` (url=213ms, nekobox=244ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-102MS` (url=217ms, nekobox=253ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-113MS` (url=207ms, nekobox=292ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-110MS` (url=224ms, nekobox=300ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-105MS` (url=211ms, nekobox=263ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-119MS` (url=251ms, nekobox=264ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-144MS` (url=244ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-153MS` (url=268ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-147MS` (url=315ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-113MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-97MS` (url=224ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-144MS` (url=275ms, status=HTTP 204)
17. `AKUN-017-008500-VLESS-WS-95MS` (url=206ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-96MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-115MS` (url=242ms, status=HTTP 204)
20. `AKUN-020-ZOOM-VLESS-WS-88MS` (url=210ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-101MS` (url=211ms, status=HTTP 204)
22. `AKUN-022-ZVC-VLESS-WS-82MS` (url=204ms, status=HTTP 204)
23. `AKUN-023-3666888-VLESS-WS-97MS` (url=226ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-90MS` (url=210ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-87MS` (url=206ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
