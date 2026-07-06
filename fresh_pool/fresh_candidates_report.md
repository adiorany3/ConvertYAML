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
1. `AKUN-001-VULTR-VLESS-WS-70MS` (url=228ms, nekobox=240ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=213ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=210ms, nekobox=180ms, status=no)
4. `AKUN-003-ADF-VLESS-WS-83MS`
5. `AKUN-004-ZVC-VLESS-WS-82MS`
6. `AKUN-005-ZVC-VLESS-WS-85MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-72MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-94MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-97MS`
11. `AKUN-010-WPENG-VLESS-WS-70MS`
12. `AKUN-012-CHSL-HEL-VLESS-WS-91MS` (url=216ms, status=HTTP 204)
13. `AKUN-013-WEYRO-NET-VLESS-WS-91MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-89MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-79MS` (url=226ms, status=HTTP 204)
16. `AKUN-016-MYBB-VLESS-WS-119MS` (url=211ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-99MS` (url=228ms, status=HTTP 204)
18. `AKUN-018-WPENG-VLESS-WS-68MS` (url=210ms, status=HTTP 204)
19. `AKUN-019-1PASSWORD-VLESS-WS-87MS` (url=223ms, status=HTTP 204)
20. `AKUN-020-MEDIUM-VLESS-WS-172MS` (url=222ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-67MS` (url=214ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-232MS` (url=486ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-239MS` (url=573ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-242MS` (url=505ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-245MS` (url=539ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
