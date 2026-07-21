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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-92MS` (url=215ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-94MS` (url=209ms, nekobox=234ms, status=yes)
3. `AKUN-003-WEBEX-VLESS-WS-90MS` (url=288ms, nekobox=257ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-96MS` (url=226ms, nekobox=246ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-104MS` (url=217ms, nekobox=277ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS` (url=216ms, nekobox=232ms, status=yes)
7. `AKUN-007-MEDIUM-VLESS-WS-107MS` (url=226ms, nekobox=252ms, status=yes)
8. `AKUN-009-UNKNOWN-VLESS-WS-114MS` (url=385ms, nekobox=247ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-100MS`
10. `AKUN-011-CLOUDFLARE-VLESS-WS-129MS` (url=480ms, nekobox=204ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-138MS`
12. `AKUN-013-DEV-VLESS-WS-160MS` (url=217ms, nekobox=206ms, status=no)
13. `AKUN-010-CLOUDFLARE-VLESS-WS-115MS`
14. `AKUN-015-CLOUDFLARE-VLESS-WS-107MS` (url=209ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-132MS` (url=214ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-131MS` (url=212ms, status=HTTP 204)
17. `AKUN-018-SPEEDTEST-VLESS-WS-172MS` (url=391ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-148MS` (url=232ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-156MS` (url=221ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-104MS` (url=538ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-109MS` (url=299ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-242MS` (url=213ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-297MS` (url=258ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-369MS` (url=752ms, status=HTTP 204)
25. `AKUN-026-SPEEDTEST-VLESS-WS-175MS` (url=544ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
