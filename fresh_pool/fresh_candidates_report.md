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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=246ms, nekobox=263ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-68MS` (url=218ms, nekobox=261ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS` (url=224ms, nekobox=268ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-73MS` (url=235ms, nekobox=278ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=235ms, nekobox=269ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-74MS` (url=246ms, nekobox=274ms, status=yes)
7. `AKUN-007-OVH-VLESS-WS-81MS` (url=301ms, nekobox=277ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS` (url=275ms, nekobox=271ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-85MS` (url=196ms, nekobox=7173ms, status=no)
10. `AKUN-009-UNKNOWN-VLESS-WS-94MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-104MS`
12. `AKUN-012-ZVC-VLESS-WS-108MS` (url=275ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-90MS` (url=281ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-92MS` (url=239ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-100MS` (url=244ms, status=HTTP 204)
16. `AKUN-016-HETZNER-VLESS-WS-116MS` (url=274ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-99MS` (url=247ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-75MS` (url=260ms, status=HTTP 204)
19. `AKUN-019-HETZNER-VLESS-WS-92MS` (url=260ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-106MS` (url=257ms, status=HTTP 204)
21. `AKUN-021-SPEEDTEST-VLESS-WS-207MS` (url=579ms, status=HTTP 204)
22. `AKUN-022-WPENG-VLESS-WS-260MS` (url=581ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-257MS` (url=607ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-249MS` (url=375ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-262MS` (url=629ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
