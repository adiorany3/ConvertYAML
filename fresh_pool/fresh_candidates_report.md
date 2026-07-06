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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-148MS` (url=285ms, nekobox=324ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-148MS` (url=316ms, nekobox=308ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-142MS` (url=286ms, nekobox=301ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-156MS` (url=372ms, nekobox=313ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-148MS` (url=283ms, nekobox=305ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-160MS` (url=288ms, nekobox=331ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-150MS` (url=277ms, nekobox=323ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-145MS` (url=317ms, nekobox=330ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-156MS` (url=290ms, nekobox=301ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-161MS` (url=323ms, nekobox=358ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-138MS` (url=283ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-171MS` (url=350ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-150MS` (url=333ms, status=HTTP 204)
14. `AKUN-014-WEYRO-NET-VLESS-WS-188MS` (url=358ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-189MS` (url=341ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-131MS` (url=348ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-221MS` (url=310ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-193MS` (url=262ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-291MS` (url=456ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-358MS` (url=743ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-367MS` (url=765ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-374MS` (url=725ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-370MS` (url=764ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-388MS` (url=779ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-382MS` (url=808ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
