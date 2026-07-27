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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=236ms, nekobox=318ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-65MS` (url=222ms, nekobox=256ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-71MS` (url=285ms, nekobox=257ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=262ms, nekobox=255ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-78MS` (url=256ms, nekobox=274ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-70MS` (url=241ms, nekobox=258ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS` (url=224ms, nekobox=265ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-73MS` (url=295ms, nekobox=253ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS` (url=238ms, nekobox=262ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS` (url=241ms, nekobox=246ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-93MS` (url=232ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-81MS` (url=244ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-116MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-77MS` (url=229ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-107MS` (url=234ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-121MS` (url=236ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-85MS` (url=225ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-98MS` (url=330ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-133MS` (url=325ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-121MS` (url=427ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-266MS` (url=568ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-328MS` (url=7498ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-100MS` (url=333ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-77MS` (url=240ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-117MS` (url=252ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
