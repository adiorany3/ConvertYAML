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
1. `AKUN-001-EGN-22-VLESS-WS-60MS` (url=221ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=215ms, nekobox=248ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-68MS` (url=218ms, nekobox=245ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-62MS` (url=217ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=239ms, nekobox=261ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS` (url=218ms, nekobox=250ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS` (url=234ms, nekobox=241ms, status=yes)
8. `AKUN-008-WEYRO-NET-VLESS-WS-70MS` (url=232ms, nekobox=262ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-72MS` (url=219ms, nekobox=262ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-82MS` (url=204ms, nekobox=244ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-85MS` (url=208ms, status=HTTP 204)
12. `AKUN-012-VDSINA-VLESS-WS-103MS` (url=245ms, status=HTTP 204)
13. `AKUN-014-WPENG-VLESS-WS-72MS` (url=223ms, status=HTTP 204)
14. `AKUN-015-WPENG-VLESS-WS-70MS` (url=222ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-127MS` (url=236ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-61MS` (url=215ms, status=HTTP 204)
17. `AKUN-018-466688-VLESS-WS-79MS` (url=216ms, status=HTTP 204)
18. `AKUN-021-UNKNOWN-VLESS-WS-362MS` (url=758ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-345MS` (url=740ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-371MS` (url=814ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-376MS` (url=839ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-391MS` (url=803ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-392MS` (url=827ms, status=HTTP 204)
24. `AKUN-027-SPEEDTEST-VLESS-WS-344MS` (url=752ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-613MS` (url=993ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
