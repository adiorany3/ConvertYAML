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
1. `AKUN-001-DEV-VLESS-WS-65MS` (url=230ms, nekobox=259ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-68MS` (url=236ms, nekobox=267ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-61MS` (url=269ms, nekobox=273ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS` (url=250ms, nekobox=277ms, status=yes)
5. `AKUN-005-DEV-VLESS-WS-67MS` (url=253ms, nekobox=260ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-66MS` (url=266ms, nekobox=176ms, status=no)
7. `AKUN-006-UNKNOWN-VLESS-WS-67MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-69MS`
9. `AKUN-008-DEV-VLESS-WS-70MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-66MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-65MS` (url=220ms, nekobox=7178ms, status=no)
12. `AKUN-010-UNKNOWN-VLESS-WS-73MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-78MS` (url=236ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-74MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-66MS` (url=256ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-86MS` (url=206ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-90MS` (url=230ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-78MS` (url=260ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-95MS` (url=239ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-93MS` (url=235ms, status=HTTP 204)
21. `AKUN-022-MEDIUM-VLESS-WS-66MS` (url=245ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-66MS` (url=238ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-84MS` (url=280ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-71MS` (url=283ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-147MS` (url=308ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
