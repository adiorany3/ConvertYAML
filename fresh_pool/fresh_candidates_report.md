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
1. `AKUN-001-UNKNOWN-VLESS-WS-58MS` (url=216ms, nekobox=236ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-56MS` (url=230ms, nekobox=246ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS` (url=230ms, nekobox=242ms, status=yes)
4. `AKUN-004-154-83-95-0-154-83-95-25-VLESS-WS-75MS` (url=212ms, nekobox=238ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS` (url=223ms, nekobox=261ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-88MS` (url=195ms, nekobox=250ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-104MS` (url=215ms, nekobox=247ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-108MS` (url=220ms, nekobox=250ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-98MS` (url=239ms, nekobox=183ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-106MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-BIGCOMMERCE-VLESS-WS-85MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-117MS` (url=196ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-97MS` (url=213ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-74MS` (url=198ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-62MS` (url=214ms, status=HTTP 204)
18. `AKUN-018-US-VLESS-WS-71MS` (url=217ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-100MS` (url=241ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-349MS` (url=724ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-384MS` (url=654ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-398MS` (url=850ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-377MS` (url=890ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-349MS` (url=750ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-436MS` (url=874ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
