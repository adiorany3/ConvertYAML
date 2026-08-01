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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=235ms, nekobox=265ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-60MS` (url=225ms, nekobox=268ms, status=yes)
3. `AKUN-003-ICOOK-VLESS-WS-60MS` (url=233ms, nekobox=252ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-64MS` (url=251ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-65MS` (url=241ms, nekobox=262ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-98MS` (url=260ms, nekobox=173ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-92MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-63MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-79MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-64MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-125MS` (url=250ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-120MS` (url=236ms, status=HTTP 204)
14. `AKUN-015-DEV-VLESS-WS-68MS` (url=273ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-74MS` (url=236ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-144MS` (url=258ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-121MS` (url=231ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-102MS` (url=335ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-166MS` (url=271ms, status=HTTP 204)
20. `AKUN-021-DE-CLOUDKLEYER-20190515-VLESS-WS-211MS` (url=320ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-211MS` (url=313ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-428MS` (url=761ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-485MS` (url=946ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-512MS` (url=891ms, status=HTTP 204)
25. `AKUN-028-SUKARIO-VLESS-WS-463MS` (url=974ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
