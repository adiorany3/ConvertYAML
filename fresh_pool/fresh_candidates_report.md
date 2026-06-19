# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=200ms, nekobox=245ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-79MS` (url=206ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS` (url=213ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=215ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-103MS` (url=212ms, nekobox=254ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-112MS` (url=211ms, nekobox=253ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-99MS` (url=223ms, nekobox=248ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS` (url=213ms, nekobox=235ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS` (url=218ms, nekobox=239ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-232MS`
11. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-248MS` (url=553ms, status=HTTP 204)
12. `AKUN-015-CLOUDFLARE-VLESS-WS-254MS` (url=578ms, status=HTTP 204)
13. `AKUN-016-CLOUDFLARE-VLESS-WS-264MS` (url=599ms, status=HTTP 204)
14. `AKUN-017-CLOUDFLARE-VLESS-WS-269MS` (url=2474ms, status=HTTP 204)
15. `AKUN-018-UNKNOWN-VLESS-WS-279MS` (url=512ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-259MS` (url=1389ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-263MS` (url=560ms, status=HTTP 204)
18. `AKUN-025-CLOUDFLARE-VLESS-WS-369MS` (url=566ms, status=HTTP 204)
19. `AKUN-026-CLOUDFLARE-VLESS-WS-405MS` (url=558ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-370MS` (url=564ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
