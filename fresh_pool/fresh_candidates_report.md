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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-MEDIUM-VLESS-WS-94MS` (url=207ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-105MS` (url=215ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-100MS` (url=220ms, nekobox=266ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-114MS` (url=209ms, nekobox=265ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-110MS` (url=214ms, nekobox=273ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-123MS` (url=212ms, nekobox=264ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-102MS` (url=212ms, nekobox=267ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-109MS` (url=1130ms, nekobox=1271ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-97MS` (url=213ms, nekobox=250ms, status=yes)
10. `AKUN-010-SPEEDTEST-VLESS-WS-113MS` (url=212ms, nekobox=200ms, status=no)
11. `AKUN-010-UNKNOWN-VLESS-WS-123MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-143MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-140MS` (url=244ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-128MS` (url=216ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-141MS` (url=245ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-154MS` (url=261ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-174MS` (url=268ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-124MS` (url=235ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-390MS` (url=783ms, status=HTTP 204)
20. `AKUN-023-CONFLU-VLESS-WS-378MS` (url=744ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-323MS` (url=645ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-628MS` (url=1065ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-656MS` (url=1026ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-683MS` (url=1289ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-740MS` (url=1318ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
