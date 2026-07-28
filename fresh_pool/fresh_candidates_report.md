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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=199ms, nekobox=250ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=208ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=240ms, nekobox=239ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=225ms, nekobox=240ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-80MS` (url=200ms, nekobox=246ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=227ms, nekobox=254ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=270ms, nekobox=7177ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-72MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-102MS` (url=215ms, nekobox=199ms, status=no)
11. `AKUN-009-DEV-VLESS-WS-81MS`
12. `AKUN-010-UNKNOWN-VLESS-WS-87MS`
13. `AKUN-013-008500-VLESS-WS-79MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-111MS` (url=214ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-132MS` (url=242ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-116MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-106MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-104MS` (url=197ms, status=HTTP 204)
19. `AKUN-019-MEDIUM-VLESS-WS-100MS` (url=225ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-95MS` (url=212ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-82MS` (url=200ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-81MS` (url=228ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-88MS` (url=204ms, status=HTTP 204)
24. `AKUN-024-SKK-VLESS-WS-157MS` (url=293ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-77MS` (url=281ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
