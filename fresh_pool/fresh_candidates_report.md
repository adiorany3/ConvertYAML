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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=220ms, nekobox=269ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-62MS` (url=229ms, nekobox=254ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-66MS` (url=220ms, nekobox=241ms, status=yes)
4. `AKUN-004-WEBEX-VLESS-WS-75MS` (url=205ms, nekobox=265ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-63MS` (url=224ms, nekobox=248ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-75MS` (url=219ms, nekobox=244ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-64MS` (url=217ms, nekobox=253ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-70MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-66MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-95MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-102MS` (url=223ms, status=HTTP 204)
12. `AKUN-013-ZVC-VLESS-WS-68MS` (url=235ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-91MS` (url=233ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-105MS` (url=206ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-71MS` (url=217ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-57MS` (url=220ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-150MS` (url=314ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-105MS` (url=213ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-124MS` (url=360ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-185MS` (url=244ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-223MS` (url=261ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-188MS` (url=382ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-351MS` (url=781ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-353MS` (url=1262ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-352MS` (url=5987ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
