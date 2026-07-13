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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=245ms, nekobox=277ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=242ms, nekobox=261ms, status=yes)
3. `AKUN-003-IDC-SG-VLESS-WS-90MS` (url=262ms, nekobox=297ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-79MS` (url=231ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS` (url=250ms, nekobox=322ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS` (url=241ms, nekobox=298ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS` (url=232ms, nekobox=274ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-87MS` (url=238ms, nekobox=271ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-96MS` (url=257ms, nekobox=276ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-106MS` (url=239ms, nekobox=282ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-96MS` (url=241ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-109MS` (url=252ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-95MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-113MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-117MS` (url=254ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-102MS` (url=253ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-86MS` (url=259ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-124MS` (url=288ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-179MS` (url=394ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-171MS` (url=263ms, status=HTTP 204)
21. `AKUN-021-QZZ-VLESS-WS-207MS` (url=471ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-230MS` (url=455ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-258MS` (url=557ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-268MS` (url=563ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-277MS` (url=594ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
