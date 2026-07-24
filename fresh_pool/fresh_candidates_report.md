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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=227ms, nekobox=264ms, status=yes)
2. `AKUN-002-ZOOM-VLESS-WS-70MS` (url=255ms, nekobox=265ms, status=yes)
3. `AKUN-003-008500-VLESS-WS-75MS` (url=245ms, nekobox=269ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-69MS` (url=258ms, nekobox=255ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-77MS` (url=227ms, nekobox=265ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-65MS` (url=233ms, nekobox=264ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-66MS` (url=234ms, nekobox=273ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-70MS` (url=252ms, nekobox=271ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=230ms, nekobox=7177ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-71MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-71MS` (url=247ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-80MS` (url=307ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-80MS` (url=247ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-82MS` (url=237ms, status=HTTP 204)
16. `AKUN-016-CCWU-VLESS-WS-89MS` (url=242ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-81MS` (url=229ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-89MS` (url=234ms, status=HTTP 204)
19. `AKUN-019-MYBB-VLESS-WS-78MS` (url=272ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-99MS` (url=246ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-79MS` (url=249ms, status=HTTP 204)
22. `AKUN-022-DEV-VLESS-WS-112MS` (url=231ms, status=HTTP 204)
23. `AKUN-023-ADF-VLESS-WS-76MS` (url=243ms, status=HTTP 204)
24. `AKUN-024-MEDIUM-VLESS-WS-79MS` (url=250ms, status=HTTP 204)
25. `AKUN-025-1PASSWORD-VLESS-WS-83MS` (url=269ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
