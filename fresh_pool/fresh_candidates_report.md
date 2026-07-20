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
1. `AKUN-001-CZ-LOTUNA-19970206-VLESS-WS-71MS` (url=233ms, nekobox=256ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-71MS` (url=210ms, nekobox=253ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-75MS` (url=216ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=214ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-70MS` (url=201ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-64MS` (url=214ms, nekobox=235ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-74MS` (url=228ms, nekobox=242ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-79MS` (url=226ms, nekobox=256ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-69MS` (url=211ms, nekobox=249ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-74MS` (url=205ms, nekobox=247ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-89MS` (url=242ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-91MS` (url=200ms, status=HTTP 204)
13. `AKUN-013-466688-VLESS-WS-76MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-75MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-WPENG-VLESS-WS-81MS` (url=228ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-97MS` (url=208ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-96MS` (url=211ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-90MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-UK-GB-DCL-01-20191003-VLESS-WS-109MS` (url=221ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-104MS` (url=253ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-93MS` (url=229ms, status=HTTP 204)
22. `AKUN-022-VOV-VLESS-WS-103MS` (url=208ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-113MS` (url=231ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-125MS` (url=203ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-91MS` (url=239ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
