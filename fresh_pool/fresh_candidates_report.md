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
1. `AKUN-001-ORACLE-VLESS-WS-57MS` (url=390ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=230ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-61MS` (url=213ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=239ms, nekobox=239ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-62MS` (url=209ms, nekobox=247ms, status=yes)
6. `AKUN-006-008500-VLESS-WS-65MS` (url=224ms, nekobox=248ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-63MS` (url=214ms, nekobox=240ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-71MS` (url=221ms, nekobox=262ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-81MS` (url=216ms, nekobox=238ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-56MS` (url=219ms, nekobox=256ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS` (url=207ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-74MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-67MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-83MS` (url=236ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-100MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-76MS` (url=222ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-75MS` (url=224ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-165MS` (url=228ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-167MS` (url=201ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-67MS` (url=200ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-139MS` (url=249ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-68MS` (url=229ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-69MS` (url=222ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-71MS` (url=224ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-167MS` (url=245ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
