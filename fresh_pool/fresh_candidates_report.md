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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-89MS` (url=217ms, nekobox=243ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-88MS` (url=236ms, nekobox=240ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-97MS` (url=207ms, nekobox=242ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-100MS` (url=231ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-103MS` (url=246ms, nekobox=243ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-95MS` (url=207ms, nekobox=236ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-99MS` (url=209ms, nekobox=250ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-104MS` (url=236ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS` (url=239ms, nekobox=266ms, status=yes)
10. `AKUN-010-ES-FORNEX-20160629-VLESS-WS-125MS` (url=264ms, nekobox=262ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-123MS` (url=303ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-131MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-121MS` (url=271ms, status=HTTP 204)
14. `AKUN-014-1PASSWORD-VLESS-WS-131MS` (url=234ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-106MS` (url=244ms, status=HTTP 204)
16. `AKUN-016-MEDIUM-VLESS-WS-135MS` (url=230ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-104MS` (url=204ms, status=HTTP 204)
18. `AKUN-018-US-VLESS-WS-134MS` (url=248ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-120MS` (url=253ms, status=HTTP 204)
20. `AKUN-020-SHOPIFY-VLESS-WS-118MS` (url=242ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-127MS` (url=246ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-120MS` (url=242ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-105MS` (url=266ms, status=HTTP 204)
24. `AKUN-024-466688-VLESS-WS-120MS` (url=244ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-125MS` (url=233ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
