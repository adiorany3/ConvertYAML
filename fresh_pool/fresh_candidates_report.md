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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-83MS` (url=337ms, nekobox=307ms, status=yes)
2. `AKUN-002-CCWU-VLESS-WS-86MS` (url=323ms, nekobox=374ms, status=yes)
3. `AKUN-003-SHOPIFY-VLESS-WS-83MS` (url=367ms, nekobox=299ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-91MS` (url=305ms, nekobox=310ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-91MS` (url=348ms, nekobox=310ms, status=yes)
6. `AKUN-006-VULTR-VLESS-WS-93MS` (url=280ms, nekobox=348ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-80MS` (url=275ms, nekobox=320ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS` (url=315ms, nekobox=380ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-110MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-113MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-82MS` (url=315ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-93MS` (url=355ms, status=HTTP 204)
13. `AKUN-014-DEV-VLESS-WS-136MS` (url=389ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-93MS` (url=281ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-143MS` (url=326ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-144MS` (url=289ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-175MS` (url=397ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-305MS` (url=647ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-323MS` (url=683ms, status=HTTP 204)
20. `AKUN-021-SKK-VLESS-WS-259MS` (url=549ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-116MS` (url=318ms, status=HTTP 204)
22. `AKUN-023-ZOOM-VLESS-WS-93MS` (url=412ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-299MS` (url=3572ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-441MS` (url=815ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-474MS` (url=874ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
