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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=223ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=222ms, nekobox=256ms, status=yes)
3. `AKUN-003-GO-DADDY-COM-LLC-VLESS-WS-69MS` (url=222ms, nekobox=253ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=231ms, nekobox=259ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-67MS` (url=223ms, nekobox=256ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=209ms, nekobox=250ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS` (url=229ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-67MS` (url=220ms, nekobox=279ms, status=yes)
9. `AKUN-009-IDC-SG-VLESS-WS-94MS` (url=228ms, nekobox=238ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-61MS` (url=217ms, nekobox=244ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-109MS` (url=230ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-94MS` (url=250ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-99MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-126MS` (url=226ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-78MS` (url=273ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-87MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-103MS` (url=211ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-71MS` (url=222ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-82MS` (url=209ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-76MS` (url=216ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-138MS` (url=228ms, status=HTTP 204)
22. `AKUN-022-SHOPIFY-VLESS-WS-119MS` (url=231ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-85MS` (url=276ms, status=HTTP 204)
24. `AKUN-025-DEV-VLESS-WS-87MS` (url=234ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-80MS` (url=229ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
