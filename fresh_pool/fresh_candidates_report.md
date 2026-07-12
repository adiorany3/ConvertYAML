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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-UNKNOWN-VLESS-WS-80MS` (url=317ms, nekobox=318ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-84MS` (url=338ms, nekobox=343ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-93MS` (url=337ms, nekobox=396ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-97MS` (url=307ms, nekobox=349ms, status=yes)
5. `AKUN-005-NET-82-21-84-0-24-VLESS-WS-87MS` (url=310ms, nekobox=389ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=308ms, nekobox=396ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-105MS` (url=332ms, nekobox=359ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS` (url=362ms, nekobox=355ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-104MS` (url=376ms, nekobox=340ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-116MS` (url=373ms, nekobox=402ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-105MS` (url=256ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-105MS` (url=339ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-103MS` (url=458ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-111MS` (url=301ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-108MS` (url=298ms, status=HTTP 204)
16. `AKUN-016-US-VLESS-WS-103MS` (url=321ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-110MS` (url=400ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-100MS` (url=303ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-112MS` (url=375ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-136MS` (url=339ms, status=HTTP 204)
21. `AKUN-021-MYBB-VLESS-WS-118MS` (url=360ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-115MS` (url=337ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-229MS` (url=572ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-316MS` (url=694ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-315MS` (url=730ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
