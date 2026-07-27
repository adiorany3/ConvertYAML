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
1. `AKUN-001-UNKNOWN-VLESS-WS-59MS` (url=288ms, nekobox=269ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=285ms, nekobox=258ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS` (url=234ms, nekobox=285ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-59MS` (url=238ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-63MS` (url=223ms, nekobox=264ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-63MS` (url=225ms, nekobox=250ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-74MS` (url=239ms, nekobox=266ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-69MS` (url=218ms, nekobox=313ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-71MS` (url=226ms, nekobox=254ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-61MS` (url=227ms, nekobox=290ms, status=yes)
11. `AKUN-011-008500-VLESS-WS-66MS` (url=271ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-109MS` (url=280ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-62MS` (url=252ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-60MS` (url=229ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-65MS` (url=228ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-85MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-137MS` (url=311ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-71MS` (url=234ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-90MS` (url=239ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-66MS` (url=228ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-99MS` (url=274ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-63MS` (url=220ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-67MS` (url=231ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-83MS` (url=214ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-81MS` (url=234ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
