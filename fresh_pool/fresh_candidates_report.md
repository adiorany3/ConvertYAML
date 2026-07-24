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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-76MS` (url=220ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=212ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=223ms, nekobox=246ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-77MS` (url=231ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=213ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS` (url=223ms, nekobox=233ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=218ms, nekobox=249ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=217ms, nekobox=245ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS` (url=217ms, nekobox=250ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-104MS` (url=213ms, nekobox=241ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-109MS` (url=215ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-84MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-121MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-130MS` (url=226ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-96MS` (url=258ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-124MS` (url=253ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-129MS` (url=239ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-133MS` (url=205ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-142MS` (url=218ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-128MS` (url=227ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-180MS` (url=242ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-176MS` (url=289ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-184MS` (url=270ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-232MS` (url=503ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-233MS` (url=503ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
