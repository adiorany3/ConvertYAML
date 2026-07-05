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
1. `AKUN-001-WPENG-VLESS-WS-63MS` (url=229ms, nekobox=262ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=237ms, nekobox=268ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=406ms, nekobox=273ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=229ms, nekobox=279ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=251ms, nekobox=268ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=258ms, nekobox=273ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-68MS` (url=244ms, nekobox=255ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-69MS` (url=238ms, nekobox=254ms, status=yes)
9. `AKUN-009-SSL-1134-VLESS-WS-81MS` (url=230ms, nekobox=299ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-88MS` (url=248ms, nekobox=197ms, status=no)
11. `AKUN-010-WEYRO-NET-VLESS-WS-82MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-83MS` (url=250ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-82MS` (url=222ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-89MS` (url=271ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-84MS` (url=257ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-78MS` (url=278ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-99MS` (url=252ms, status=HTTP 204)
18. `AKUN-018-ZVC-VLESS-WS-73MS` (url=226ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-251MS` (url=580ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-273MS` (url=544ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-284MS` (url=622ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-279MS` (url=571ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-290MS` (url=600ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-289MS` (url=651ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-294MS` (url=603ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
