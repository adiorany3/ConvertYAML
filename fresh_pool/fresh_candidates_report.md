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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-56MS` (url=248ms, nekobox=243ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-59MS` (url=214ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS` (url=221ms, nekobox=254ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-58MS` (url=209ms, nekobox=244ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-64MS` (url=227ms, nekobox=250ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-67MS` (url=223ms, nekobox=249ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-75MS` (url=398ms, nekobox=256ms, status=yes)
8. `AKUN-008-OVH-VLESS-WS-69MS` (url=227ms, nekobox=260ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-78MS` (url=217ms, nekobox=255ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-58MS` (url=220ms, nekobox=263ms, status=yes)
11. `AKUN-011-466688-VLESS-WS-67MS` (url=215ms, status=HTTP 204)
12. `AKUN-012-ZOOM-VLESS-WS-118MS` (url=216ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-110MS` (url=252ms, status=HTTP 204)
14. `AKUN-014-WEYRO-NET-VLESS-WS-97MS` (url=229ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-140MS` (url=212ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-282MS` (url=778ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-367MS` (url=797ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-367MS` (url=722ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-355MS` (url=744ms, status=HTTP 204)
20. `AKUN-020-WPENG-VLESS-WS-373MS` (url=800ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-238MS` (url=802ms, status=HTTP 204)
22. `AKUN-022-PUBLICDOMAINREGISTRY-NET-VLESS-WS-390MS` (url=825ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-667MS` (url=1117ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-679MS` (url=1094ms, status=HTTP 204)
25. `AKUN-032-UNKNOWN-VLESS-WS-798MS` (url=1273ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
