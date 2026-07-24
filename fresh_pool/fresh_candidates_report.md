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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-87MS` (url=238ms, nekobox=254ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-89MS` (url=211ms, nekobox=244ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS` (url=233ms, nekobox=235ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-90MS` (url=219ms, nekobox=266ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-91MS` (url=216ms, nekobox=267ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-90MS` (url=228ms, nekobox=236ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-100MS` (url=241ms, nekobox=242ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS` (url=221ms, nekobox=248ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-104MS` (url=251ms, nekobox=236ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-105MS` (url=243ms, nekobox=255ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-107MS` (url=216ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-97MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-99MS` (url=237ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-90MS` (url=239ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-127MS` (url=208ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-134MS` (url=255ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-126MS` (url=245ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-145MS` (url=210ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-112MS` (url=208ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-144MS` (url=213ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-128MS` (url=210ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-129MS` (url=206ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-157MS` (url=224ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-377MS` (url=4715ms, status=HTTP 204)
25. `AKUN-025-NET-141-11-202-0-23-VLESS-WS-378MS` (url=772ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
