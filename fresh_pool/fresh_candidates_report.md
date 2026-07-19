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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=216ms, nekobox=235ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-63MS` (url=226ms, nekobox=247ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=219ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-61MS` (url=212ms, nekobox=241ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-70MS` (url=226ms, nekobox=255ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS` (url=202ms, nekobox=234ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-66MS` (url=224ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-62MS` (url=231ms, nekobox=267ms, status=yes)
9. `AKUN-009-WEBEX-VLESS-WS-77MS` (url=225ms, nekobox=237ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-76MS` (url=229ms, nekobox=7177ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-72MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-79MS` (url=221ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-67MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-69MS` (url=217ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-69MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-75MS` (url=216ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-65MS` (url=217ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-69MS` (url=219ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-81MS` (url=228ms, status=HTTP 204)
20. `AKUN-020-CCWU-VLESS-WS-79MS` (url=199ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-82MS` (url=223ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-85MS` (url=223ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-99MS` (url=200ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-77MS` (url=226ms, status=HTTP 204)
25. `AKUN-025-466688-VLESS-WS-105MS` (url=224ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
