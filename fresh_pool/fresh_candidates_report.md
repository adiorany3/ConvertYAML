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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=213ms, nekobox=244ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=212ms, nekobox=173ms, status=no)
3. `AKUN-002-UNKNOWN-VLESS-WS-60MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-68MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-66MS` (url=213ms, nekobox=173ms, status=no)
8. `AKUN-006-CLOUDFLARE-VLESS-WS-105MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-107MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS` (url=203ms, nekobox=248ms, status=yes)
11. `AKUN-009-ZVC-VLESS-WS-87MS`
12. `AKUN-010-090227-VLESS-WS-115MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-112MS` (url=201ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-110MS` (url=217ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-159MS` (url=253ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-126MS` (url=216ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-155MS` (url=260ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-63MS` (url=214ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-252MS` (url=485ms, status=HTTP 204)
20. `AKUN-023-SKK-VLESS-WS-303MS` (url=760ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-297MS` (url=500ms, status=HTTP 204)
22. `AKUN-026-UNKNOWN-VLESS-WS-391MS` (url=661ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-460MS` (url=762ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-507MS` (url=834ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-459MS` (url=743ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
