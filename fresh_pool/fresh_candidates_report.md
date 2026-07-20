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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=253ms, nekobox=271ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=245ms, nekobox=273ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS` (url=227ms, nekobox=260ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-76MS` (url=245ms, nekobox=264ms, status=yes)
5. `AKUN-005-GO-DADDY-COM-LLC-VLESS-WS-76MS` (url=258ms, nekobox=289ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-88MS` (url=291ms, nekobox=282ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS` (url=265ms, nekobox=305ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-103MS` (url=260ms, nekobox=305ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-121MS` (url=269ms, nekobox=287ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-109MS` (url=249ms, nekobox=278ms, status=yes)
11. `AKUN-011-GO-DADDY-COM-LLC-VLESS-WS-103MS` (url=260ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-108MS` (url=251ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-123MS` (url=238ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-126MS` (url=250ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-123MS` (url=245ms, status=HTTP 204)
16. `AKUN-016-UK-GB-DCL-01-20191003-VLESS-WS-91MS` (url=251ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-133MS` (url=282ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-113MS` (url=315ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-90MS` (url=270ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-123MS` (url=289ms, status=HTTP 204)
21. `AKUN-021-UK-GB-DCL-01-20191003-VLESS-WS-130MS` (url=318ms, status=HTTP 204)
22. `AKUN-022-ZVC-VLESS-WS-117MS` (url=292ms, status=HTTP 204)
23. `AKUN-024-WPENG-VLESS-WS-97MS` (url=280ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-252MS` (url=3364ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-293MS` (url=708ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
