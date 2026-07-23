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
1. `AKUN-001-UNKNOWN-VLESS-WS-73MS` (url=201ms, nekobox=224ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-73MS` (url=209ms, nekobox=7177ms, status=no)
3. `AKUN-002-1PASSWORD-VLESS-WS-70MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-71MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-61MS`
6. `AKUN-005-ZVC-VLESS-WS-78MS`
7. `AKUN-006-ADF-VLESS-WS-76MS`
8. `AKUN-007-LEVIKOGJGFDD-VLESS-WS-71MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-71MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-75MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-SHOPIFY-VLESS-WS-103MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-63MS` (url=206ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-107MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-92MS` (url=198ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-94MS` (url=200ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-101MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-124MS` (url=210ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-105MS` (url=206ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-120MS` (url=211ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-109MS` (url=226ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-94MS` (url=221ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-113MS` (url=211ms, status=HTTP 204)
25. `AKUN-025-DEV-VLESS-WS-111MS` (url=223ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
