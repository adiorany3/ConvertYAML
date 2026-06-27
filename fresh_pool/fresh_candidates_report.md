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
1. `AKUN-001-UNKNOWN-VLESS-WS-62MS` (url=209ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=218ms, nekobox=255ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-69MS` (url=211ms, nekobox=248ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-71MS` (url=200ms, nekobox=244ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-71MS` (url=202ms, nekobox=255ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-74MS` (url=221ms, nekobox=241ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-77MS` (url=238ms, nekobox=246ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-94MS` (url=208ms, nekobox=254ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS` (url=220ms, nekobox=255ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-94MS` (url=217ms, nekobox=273ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-86MS` (url=220ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-97MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-101MS` (url=199ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-114MS` (url=221ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-119MS` (url=200ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-86MS` (url=211ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-349MS` (url=752ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-348MS` (url=2502ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-351MS` (url=772ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-395MS` (url=853ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-408MS` (url=818ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-401MS` (url=874ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-405MS` (url=870ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-374MS` (url=640ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-412MS` (url=855ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
