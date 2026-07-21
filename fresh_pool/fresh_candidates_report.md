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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-88MS` (url=239ms, nekobox=240ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-93MS` (url=209ms, nekobox=241ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-95MS` (url=215ms, nekobox=1092ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-112MS` (url=798ms, nekobox=2462ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-109MS` (url=213ms, nekobox=259ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-95MS` (url=235ms, nekobox=238ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-100MS` (url=221ms, nekobox=244ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-106MS` (url=209ms, nekobox=258ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS` (url=217ms, nekobox=249ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-161MS` (url=306ms, nekobox=407ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-96MS` (url=224ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-199MS` (url=649ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-115MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-377MS` (url=785ms, status=HTTP 204)
15. `AKUN-015-UK-GB-DCL-01-20191003-VLESS-WS-125MS` (url=461ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-354MS` (url=398ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-188MS` (url=846ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-109MS` (url=245ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-425MS` (url=835ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-269MS` (url=312ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-417MS` (url=822ms, status=HTTP 204)
22. `AKUN-022-WPENG-VLESS-WS-121MS` (url=221ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-459MS` (url=919ms, status=HTTP 204)
24. `AKUN-024-UK-GB-DCL-01-20191003-VLESS-WS-704MS` (url=3900ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-286MS` (url=1230ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
