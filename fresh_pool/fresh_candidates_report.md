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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=226ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-58MS` (url=211ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=215ms, nekobox=202ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS`
5. `AKUN-004-ZVC-VLESS-WS-70MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-81MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-74MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-74MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-83MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-89MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-75MS`
12. `AKUN-012-PUBLICDOMAINREGISTRY-NET-VLESS-WS-79MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-87MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-98MS` (url=256ms, status=HTTP 204)
15. `AKUN-015-1323123-VLESS-WS-77MS` (url=212ms, status=HTTP 204)
16. `AKUN-016-WEBEX-VLESS-WS-90MS` (url=262ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-124MS` (url=242ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-71MS` (url=210ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-127MS` (url=224ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-117MS` (url=227ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-358MS` (url=736ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-363MS` (url=853ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-357MS` (url=764ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-395MS` (url=834ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-389MS` (url=845ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
