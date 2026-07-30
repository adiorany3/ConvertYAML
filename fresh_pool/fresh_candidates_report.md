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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=233ms, nekobox=261ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=241ms, nekobox=268ms, status=yes)
3. `AKUN-003-CCWU-VLESS-WS-63MS` (url=241ms, nekobox=256ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=244ms, nekobox=272ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-67MS` (url=243ms, nekobox=265ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS` (url=238ms, nekobox=185ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-72MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-71MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-79MS` (url=258ms, nekobox=264ms, status=yes)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-79MS` (url=244ms, nekobox=264ms, status=yes)
12. `AKUN-012-UNKNOWN-VLESS-WS-70MS` (url=242ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-79MS` (url=261ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-73MS` (url=251ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-75MS` (url=239ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-68MS` (url=233ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-82MS` (url=243ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-93MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-77MS` (url=281ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-89MS` (url=266ms, status=HTTP 204)
21. `AKUN-021-MEDIUM-VLESS-WS-66MS` (url=269ms, status=HTTP 204)
22. `AKUN-022-ADF-VLESS-WS-93MS` (url=235ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-73MS` (url=232ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-95MS` (url=251ms, status=HTTP 204)
25. `AKUN-025-1PASSWORD-VLESS-WS-69MS` (url=240ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
