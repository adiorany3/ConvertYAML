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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=218ms, nekobox=269ms, status=yes)
2. `AKUN-002-UK-GB-DCL-01-20191003-VLESS-WS-78MS` (url=216ms, nekobox=240ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-66MS` (url=211ms, nekobox=259ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=220ms, nekobox=232ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-65MS` (url=212ms, nekobox=249ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-70MS` (url=214ms, nekobox=260ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-78MS` (url=225ms, nekobox=264ms, status=yes)
8. `AKUN-008-MEDIUM-VLESS-WS-79MS` (url=208ms, nekobox=245ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-71MS` (url=227ms, nekobox=240ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-101MS` (url=290ms, nekobox=268ms, status=yes)
11. `AKUN-011-DEV-VLESS-WS-72MS` (url=228ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-105MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-1PASSWORD-VLESS-WS-91MS` (url=238ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-96MS` (url=253ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-110MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-104MS` (url=218ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-93MS` (url=232ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-77MS` (url=219ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-107MS` (url=244ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-125MS` (url=338ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-77MS` (url=223ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-136MS` (url=216ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-81MS` (url=227ms, status=HTTP 204)
24. `AKUN-024-WPENG-VLESS-WS-87MS` (url=211ms, status=HTTP 204)
25. `AKUN-025-SHOPIFY-VLESS-WS-98MS` (url=211ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
