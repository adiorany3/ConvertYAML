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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=246ms, nekobox=278ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-77MS` (url=239ms, nekobox=297ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=302ms, nekobox=361ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-68MS` (url=242ms, nekobox=292ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-76MS` (url=228ms, nekobox=269ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS` (url=252ms, nekobox=266ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS` (url=255ms, nekobox=271ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=257ms, nekobox=265ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS` (url=262ms, nekobox=268ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-83MS` (url=269ms, nekobox=265ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-105MS` (url=256ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-83MS` (url=243ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-93MS` (url=230ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-87MS` (url=274ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-88MS` (url=241ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-94MS` (url=252ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-108MS` (url=272ms, status=HTTP 204)
18. `AKUN-019-ZVC-VLESS-WS-80MS` (url=247ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-78MS` (url=237ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-88MS` (url=229ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-145MS` (url=253ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-272MS` (url=4733ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-286MS` (url=1185ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-301MS` (url=2504ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-445MS` (url=583ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
