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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=259ms, nekobox=260ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-79MS` (url=231ms, nekobox=276ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=238ms, nekobox=279ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-61MS` (url=228ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-90MS` (url=236ms, nekobox=187ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-99MS`
7. `AKUN-006-ZVC-VLESS-WS-107MS`
8. `AKUN-007-ES-FORNEX-20160629-VLESS-WS-74MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-107MS` (url=252ms, nekobox=178ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS`
12. `AKUN-010-ZVC-VLESS-WS-67MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-71MS` (url=243ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-75MS` (url=245ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-96MS` (url=266ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-96MS` (url=242ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-87MS` (url=224ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-129MS` (url=268ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-173MS` (url=286ms, status=HTTP 204)
20. `AKUN-020-NAVIDAM-VLESS-WS-242MS` (url=708ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-229MS` (url=526ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-138MS` (url=220ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-355MS` (url=756ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-283MS` (url=333ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-392MS` (url=853ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
