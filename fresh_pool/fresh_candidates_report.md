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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=215ms, nekobox=253ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=217ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS` (url=226ms, nekobox=262ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=239ms, nekobox=246ms, status=yes)
5. `AKUN-005-DIGITALOCEAN-VLESS-WS-71MS` (url=312ms, nekobox=246ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS` (url=202ms, nekobox=256ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS` (url=225ms, nekobox=263ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-65MS` (url=261ms, nekobox=240ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-67MS` (url=220ms, nekobox=246ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-93MS` (url=221ms, nekobox=249ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-90MS` (url=303ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-87MS` (url=226ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-114MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-71MS` (url=230ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-138MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-106MS` (url=250ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-98MS` (url=202ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-74MS` (url=231ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-175MS` (url=217ms, status=HTTP 204)
20. `AKUN-020-ZVC-VLESS-WS-78MS` (url=230ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-350MS` (url=740ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-359MS` (url=771ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-384MS` (url=791ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-394MS` (url=849ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-378MS` (url=791ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
