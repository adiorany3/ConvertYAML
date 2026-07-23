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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-87MS` (url=234ms, nekobox=237ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-91MS` (url=234ms, nekobox=232ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-91MS` (url=228ms, nekobox=240ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS` (url=212ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=228ms, nekobox=249ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-96MS` (url=231ms, nekobox=263ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-105MS` (url=240ms, nekobox=263ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-111MS` (url=213ms, nekobox=247ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-107MS` (url=247ms, nekobox=7172ms, status=no)
10. `AKUN-009-DEV-VLESS-WS-112MS`
11. `AKUN-010-DEV-VLESS-WS-114MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-93MS` (url=293ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-94MS` (url=251ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-119MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-108MS` (url=212ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-102MS` (url=211ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-109MS` (url=260ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-140MS` (url=279ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-108MS` (url=241ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-129MS` (url=230ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-110MS` (url=231ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-114MS` (url=208ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-106MS` (url=270ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-115MS` (url=238ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-142MS` (url=232ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
