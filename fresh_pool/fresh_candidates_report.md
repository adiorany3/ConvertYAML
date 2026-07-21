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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=223ms, nekobox=253ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-65MS` (url=211ms, nekobox=253ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-67MS` (url=209ms, nekobox=259ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-58MS` (url=218ms, nekobox=241ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-73MS` (url=229ms, nekobox=231ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-61MS` (url=208ms, nekobox=240ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-75MS` (url=222ms, nekobox=242ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-69MS` (url=223ms, nekobox=260ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-72MS` (url=215ms, nekobox=252ms, status=yes)
10. `AKUN-010-MEDIUM-VLESS-WS-67MS` (url=229ms, nekobox=256ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-80MS` (url=229ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-96MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-102MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-88MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-69MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-73MS` (url=210ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-103MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-121MS` (url=220ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-123MS` (url=199ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-151MS` (url=217ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-89MS` (url=223ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-105MS` (url=208ms, status=HTTP 204)
23. `AKUN-024-ZVC-VLESS-WS-66MS` (url=224ms, status=HTTP 204)
24. `AKUN-025-ZVC-VLESS-WS-67MS` (url=218ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-180MS` (url=203ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
