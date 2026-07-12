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
1. `AKUN-001-OVH-VLESS-WS-74MS` (url=227ms, nekobox=244ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-75MS` (url=225ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=214ms, nekobox=256ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS` (url=219ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=224ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS` (url=203ms, nekobox=265ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=206ms, nekobox=264ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-86MS` (url=224ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-86MS` (url=214ms, nekobox=261ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-80MS` (url=215ms, nekobox=254ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-85MS` (url=230ms, status=HTTP 204)
12. `AKUN-012-US-VLESS-WS-99MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-99MS` (url=229ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-118MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-81MS` (url=232ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-90MS` (url=205ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-103MS` (url=201ms, status=HTTP 204)
18. `AKUN-019-466688-VLESS-WS-101MS` (url=226ms, status=HTTP 204)
19. `AKUN-020-DEV-VLESS-WS-101MS` (url=234ms, status=HTTP 204)
20. `AKUN-021-SPEEDTEST-VLESS-WS-129MS` (url=200ms, status=HTTP 204)
21. `AKUN-022-NODEJS-VLESS-WS-142MS` (url=250ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-245MS` (url=524ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-250MS` (url=536ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-246MS` (url=556ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-232MS` (url=507ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
