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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=215ms, nekobox=264ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-67MS` (url=227ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-69MS` (url=244ms, nekobox=246ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-63MS` (url=241ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-64MS` (url=235ms, nekobox=253ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS` (url=227ms, nekobox=262ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-78MS` (url=241ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-83MS` (url=225ms, nekobox=259ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS` (url=238ms, nekobox=252ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-70MS` (url=226ms, nekobox=245ms, status=yes)
11. `AKUN-011-PAGES-VLESS-WS-95MS` (url=236ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-104MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-71MS` (url=230ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-94MS` (url=241ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-95MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-WPENG-VLESS-WS-72MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-84MS` (url=245ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-75MS` (url=254ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-238MS` (url=704ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-222MS` (url=385ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-346MS` (url=768ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-396MS` (url=867ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-370MS` (url=733ms, status=HTTP 204)
24. `AKUN-027-SPEEDTEST-VLESS-WS-364MS` (url=765ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-684MS` (url=1057ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
