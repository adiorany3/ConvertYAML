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
1. `AKUN-001-ZVC-VLESS-WS-59MS` (url=244ms, nekobox=285ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-62MS` (url=232ms, nekobox=263ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-69MS` (url=235ms, nekobox=254ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=239ms, nekobox=277ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=251ms, nekobox=297ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS` (url=251ms, nekobox=268ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS` (url=269ms, nekobox=293ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-84MS` (url=241ms, nekobox=265ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS` (url=260ms, nekobox=313ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-64MS` (url=236ms, nekobox=287ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-89MS` (url=246ms, status=HTTP 204)
12. `AKUN-012-WPENG-VLESS-WS-70MS` (url=244ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-73MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-73MS` (url=246ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-95MS` (url=270ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-108MS` (url=252ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-129MS` (url=269ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-168MS` (url=251ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-271MS` (url=591ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-288MS` (url=628ms, status=HTTP 204)
21. `AKUN-021-WPENG-VLESS-WS-284MS` (url=652ms, status=HTTP 204)
22. `AKUN-022-PUBLICDOMAINREGISTRY-NET-VLESS-WS-288MS` (url=629ms, status=HTTP 204)
23. `AKUN-023-INTERNETWORKS-45-131-208-VLESS-WS-288MS` (url=638ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-282MS` (url=555ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-303MS` (url=634ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
