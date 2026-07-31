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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-101MS` (url=234ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-111MS` (url=249ms, nekobox=374ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-105MS` (url=254ms, nekobox=276ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-108MS` (url=237ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-109MS` (url=247ms, nekobox=201ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-119MS`
7. `AKUN-006-ZVC-VLESS-WS-90MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-115MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-119MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-109MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-118MS`
12. `AKUN-012-ADF-VLESS-WS-119MS` (url=237ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-121MS` (url=251ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-115MS` (url=228ms, status=HTTP 204)
15. `AKUN-015-1PASSWORD-VLESS-WS-125MS` (url=227ms, status=HTTP 204)
16. `AKUN-016-MYBB-VLESS-WS-96MS` (url=219ms, status=HTTP 204)
17. `AKUN-017-LEVIKOGJGFDD-VLESS-WS-124MS` (url=216ms, status=HTTP 204)
18. `AKUN-018-CCWU-VLESS-WS-146MS` (url=285ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-127MS` (url=203ms, status=HTTP 204)
20. `AKUN-020-LEVIKOGJGFDD-VLESS-WS-179MS` (url=253ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-109MS` (url=381ms, status=HTTP 204)
22. `AKUN-022-DEV-VLESS-WS-102MS` (url=230ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-162MS` (url=233ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-106MS` (url=203ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-115MS` (url=212ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
