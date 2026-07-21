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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=249ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=234ms, nekobox=275ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=225ms, nekobox=270ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-68MS` (url=238ms, nekobox=285ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-89MS` (url=231ms, nekobox=306ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-107MS` (url=249ms, nekobox=299ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-124MS` (url=230ms, nekobox=291ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-90MS` (url=252ms, nekobox=263ms, status=yes)
9. `AKUN-009-WPENG-VLESS-WS-80MS` (url=342ms, nekobox=272ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-126MS` (url=257ms, nekobox=187ms, status=no)
11. `AKUN-010-UNKNOWN-VLESS-WS-86MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-114MS` (url=265ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-125MS` (url=294ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-103MS` (url=269ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-97MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-130MS` (url=277ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-113MS` (url=269ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-90MS` (url=269ms, status=HTTP 204)
19. `AKUN-020-ZVC-VLESS-WS-86MS` (url=312ms, status=HTTP 204)
20. `AKUN-021-ZVC-VLESS-WS-80MS` (url=305ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-104MS` (url=241ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-107MS` (url=249ms, status=HTTP 204)
23. `AKUN-024-UK-GB-DCL-01-20191003-VLESS-WS-276MS` (url=4105ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-251MS` (url=580ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-295MS` (url=650ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
