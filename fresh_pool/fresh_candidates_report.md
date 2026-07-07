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
1. `AKUN-001-UNKNOWN-VLESS-WS-69MS` (url=237ms, nekobox=244ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=213ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=224ms, nekobox=251ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-75MS` (url=208ms, nekobox=247ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-70MS` (url=220ms, nekobox=229ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=231ms, nekobox=234ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=218ms, nekobox=254ms, status=yes)
8. `AKUN-008-WPENG-VLESS-WS-77MS` (url=197ms, nekobox=237ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS` (url=227ms, nekobox=235ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS` (url=205ms, nekobox=240ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-83MS` (url=225ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-105MS` (url=233ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-96MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-89MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-93MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-106MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-106MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-92MS` (url=220ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-239MS` (url=577ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-257MS` (url=538ms, status=HTTP 204)
21. `AKUN-022-SPEEDTEST-VLESS-WS-248MS` (url=502ms, status=HTTP 204)
22. `AKUN-023-MICROSOFT-VLESS-WS-273MS` (url=593ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-281MS` (url=638ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-284MS` (url=605ms, status=HTTP 204)
25. `AKUN-026-SPEEDTEST-VLESS-WS-400MS` (url=551ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
