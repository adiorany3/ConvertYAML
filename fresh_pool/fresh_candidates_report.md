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
1. `AKUN-001-UNKNOWN-VLESS-WS-105MS` (url=297ms, nekobox=313ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-112MS` (url=279ms, nekobox=319ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-102MS` (url=293ms, nekobox=332ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-119MS` (url=309ms, nekobox=336ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-124MS` (url=332ms, nekobox=331ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-109MS` (url=292ms, nekobox=339ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-112MS` (url=310ms, nekobox=339ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-118MS` (url=282ms, nekobox=318ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-115MS` (url=313ms, nekobox=346ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-136MS` (url=285ms, nekobox=346ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-125MS` (url=291ms, status=HTTP 204)
12. `AKUN-012-ORG-VLESS-WS-153MS` (url=298ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-167MS` (url=350ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-130MS` (url=301ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-121MS` (url=330ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-182MS` (url=313ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-170MS` (url=331ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-171MS` (url=433ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-251MS` (url=451ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-320MS` (url=605ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-341MS` (url=688ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-314MS` (url=2927ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-509MS` (url=828ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-566MS` (url=966ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-594MS` (url=1446ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
