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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-106MS` (url=259ms, nekobox=319ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-106MS` (url=285ms, nekobox=336ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-117MS` (url=310ms, nekobox=301ms, status=yes)
4. `AKUN-004-OVH-VLESS-WS-99MS` (url=322ms, nekobox=298ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-126MS` (url=257ms, nekobox=314ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-111MS` (url=307ms, nekobox=349ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-109MS` (url=248ms, nekobox=322ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-123MS` (url=278ms, nekobox=325ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-128MS` (url=254ms, nekobox=320ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-142MS` (url=254ms, nekobox=414ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-125MS` (url=342ms, status=HTTP 204)
12. `AKUN-012-WPENG-VLESS-WS-122MS` (url=270ms, status=HTTP 204)
13. `AKUN-013-466688-VLESS-WS-140MS` (url=292ms, status=HTTP 204)
14. `AKUN-014-TENCENT-VLESS-WS-145MS` (url=258ms, status=HTTP 204)
15. `AKUN-015-WEYRO-NET-VLESS-WS-167MS` (url=295ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-122MS` (url=274ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-157MS` (url=287ms, status=HTTP 204)
18. `AKUN-018-WPENG-VLESS-WS-113MS` (url=294ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-311MS` (url=618ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-292MS` (url=728ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-312MS` (url=651ms, status=HTTP 204)
22. `AKUN-022-RC-PRO-5-VLESS-WS-342MS` (url=686ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-351MS` (url=787ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-361MS` (url=699ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-308MS` (url=688ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
