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
1. `AKUN-001-UNKNOWN-VLESS-WS-74MS` (url=250ms, nekobox=275ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=275ms, nekobox=319ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-89MS` (url=258ms, nekobox=273ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-94MS` (url=244ms, nekobox=266ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=290ms, nekobox=263ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS` (url=228ms, nekobox=272ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS` (url=246ms, nekobox=262ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-102MS` (url=249ms, nekobox=269ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS` (url=265ms, nekobox=284ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-107MS` (url=234ms, nekobox=279ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-120MS` (url=243ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-97MS` (url=277ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=222ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-120MS` (url=268ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-118MS` (url=259ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-166MS` (url=283ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-263MS` (url=594ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-256MS` (url=567ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-286MS` (url=648ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-296MS` (url=664ms, status=HTTP 204)
21. `AKUN-021-SPEEDTEST-VLESS-WS-288MS` (url=637ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-271MS` (url=577ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-298MS` (url=543ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-305MS` (url=690ms, status=HTTP 204)
25. `AKUN-029-RS-RAPIDSEEDBOX-20190717-VLESS-WS-544MS` (url=1645ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
