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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=241ms, nekobox=279ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=224ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-62MS` (url=230ms, nekobox=247ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-63MS` (url=229ms, nekobox=248ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-57MS` (url=240ms, nekobox=255ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-63MS` (url=229ms, nekobox=248ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-63MS` (url=241ms, nekobox=247ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-69MS` (url=218ms, nekobox=250ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-71MS` (url=231ms, nekobox=278ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-69MS` (url=238ms, nekobox=264ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-104MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-128MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-95MS` (url=231ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-119MS` (url=372ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-72MS` (url=293ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-96MS` (url=231ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-125MS` (url=301ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-138MS` (url=310ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-113MS` (url=318ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-125MS` (url=333ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-178MS` (url=313ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-142MS` (url=280ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-118MS` (url=286ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-252MS` (url=562ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-265MS` (url=878ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
