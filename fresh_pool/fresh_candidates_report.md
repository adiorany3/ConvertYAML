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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-116MS` (url=297ms, nekobox=293ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-126MS` (url=249ms, nekobox=286ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-124MS` (url=297ms, nekobox=269ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-127MS` (url=238ms, nekobox=287ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-128MS` (url=268ms, nekobox=275ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-125MS` (url=283ms, nekobox=299ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-113MS` (url=282ms, nekobox=299ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-132MS` (url=242ms, nekobox=289ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-144MS` (url=246ms, nekobox=290ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-121MS` (url=263ms, nekobox=287ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-155MS` (url=274ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-170MS` (url=332ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-175MS` (url=313ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-115MS` (url=258ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-141MS` (url=253ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-144MS` (url=285ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-165MS` (url=299ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-126MS` (url=243ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-154MS` (url=229ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-177MS` (url=381ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-129MS` (url=321ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-226MS` (url=435ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-227MS` (url=338ms, status=HTTP 204)
24. `AKUN-024-ZVC-VLESS-WS-121MS` (url=257ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-405MS` (url=1217ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
