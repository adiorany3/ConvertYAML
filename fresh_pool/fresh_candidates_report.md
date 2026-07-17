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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-79MS` (url=201ms, nekobox=247ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=222ms, nekobox=252ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=219ms, nekobox=264ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=221ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-97MS` (url=213ms, nekobox=249ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=215ms, nekobox=251ms, status=yes)
7. `AKUN-007-DIXONS-VLESS-WS-89MS` (url=241ms, nekobox=231ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=219ms, nekobox=254ms, status=yes)
9. `AKUN-009-GO-DADDY-COM-LLC-VLESS-WS-105MS` (url=212ms, nekobox=238ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS` (url=217ms, nekobox=235ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-87MS` (url=217ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-122MS` (url=216ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-96MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-121MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-126MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-104MS` (url=213ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-120MS` (url=215ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-88MS` (url=253ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-131MS` (url=280ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-162MS` (url=215ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-169MS` (url=222ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-154MS` (url=233ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-148MS` (url=224ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-112MS` (url=221ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-102MS` (url=211ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
