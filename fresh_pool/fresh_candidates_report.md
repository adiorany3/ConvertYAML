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
1. `AKUN-001-SIN-VLESS-WS-67MS` (url=214ms, nekobox=223ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=242ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=221ms, nekobox=248ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-78MS` (url=223ms, nekobox=279ms, status=yes)
5. `AKUN-005-NL-BRAINOZA-20250311-VLESS-WS-78MS` (url=224ms, nekobox=283ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=272ms, nekobox=278ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-63MS` (url=210ms, nekobox=256ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-66MS` (url=226ms, nekobox=238ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS` (url=217ms, nekobox=257ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-109MS` (url=237ms, nekobox=251ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-76MS` (url=239ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-106MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-101MS` (url=240ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-136MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-96MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-109MS` (url=196ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-63MS` (url=221ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-223MS` (url=364ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-357MS` (url=727ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-387MS` (url=888ms, status=HTTP 204)
21. `AKUN-024-MICROSOFT-VLESS-WS-393MS` (url=807ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-389MS` (url=853ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-378MS` (url=834ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-81MS` (url=203ms, status=HTTP 204)
25. `AKUN-033-UNKNOWN-VLESS-WS-813MS` (url=1321ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
