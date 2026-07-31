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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-87MS` (url=203ms, nekobox=229ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-95MS` (url=214ms, nekobox=256ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-93MS` (url=254ms, nekobox=193ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-100MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-101MS` (url=235ms, nekobox=7177ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-96MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-103MS`
8. `AKUN-006-DEV-VLESS-WS-92MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-98MS`
10. `AKUN-008-MYBB-VLESS-WS-103MS`
11. `AKUN-009-UNKNOWN-VLESS-WS-109MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=298ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-111MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-96MS` (url=251ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-126MS` (url=234ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-106MS` (url=221ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-106MS` (url=224ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-102MS` (url=230ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-102MS` (url=220ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-120MS` (url=240ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-115MS` (url=241ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-128MS` (url=227ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-136MS` (url=342ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-131MS` (url=306ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
