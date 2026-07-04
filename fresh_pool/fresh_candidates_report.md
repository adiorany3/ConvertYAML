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
1. `AKUN-001-UNKNOWN-VLESS-WS-71MS` (url=240ms, nekobox=265ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-71MS` (url=261ms, nekobox=255ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=245ms, nekobox=273ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-71MS` (url=247ms, nekobox=286ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=230ms, nekobox=278ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS` (url=246ms, nekobox=259ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-85MS` (url=273ms, nekobox=282ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS` (url=271ms, nekobox=211ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS`
10. `AKUN-009-466688-VLESS-WS-77MS`
11. `AKUN-010-OVH-VLESS-WS-84MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-85MS` (url=264ms, status=HTTP 204)
13. `AKUN-013-WEYRO-NET-VLESS-WS-100MS` (url=256ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS` (url=239ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-129MS` (url=238ms, status=HTTP 204)
16. `AKUN-016-WPENG-VLESS-WS-77MS` (url=270ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-86MS` (url=244ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-264MS` (url=575ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-272MS` (url=547ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-281MS` (url=608ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-286MS` (url=603ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-297MS` (url=569ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-291MS` (url=635ms, status=HTTP 204)
24. `AKUN-024-CELESTARA-VLESS-WS-298MS` (url=601ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-444MS` (url=816ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
