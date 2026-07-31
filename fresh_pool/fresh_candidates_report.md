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
1. `AKUN-001-130519-VLESS-WS-58MS` (url=212ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=222ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-56MS` (url=212ms, nekobox=260ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-51MS` (url=223ms, nekobox=250ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-68MS` (url=210ms, nekobox=249ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-73MS` (url=261ms, nekobox=253ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-71MS` (url=229ms, nekobox=578ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=212ms, nekobox=251ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS` (url=222ms, nekobox=239ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-56MS` (url=209ms, nekobox=246ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-94MS` (url=213ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-88MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-127MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-134MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-57MS` (url=212ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-299MS` (url=670ms, status=HTTP 204)
17. `AKUN-019-CN-CF-VLESS-WS-408MS` (url=955ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-596MS` (url=1028ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-660MS` (url=1001ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-658MS` (url=1071ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-664MS` (url=1028ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-666MS` (url=1141ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-659MS` (url=1261ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-661MS` (url=1407ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-634MS` (url=1179ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
