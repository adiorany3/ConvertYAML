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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=200ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=202ms, nekobox=250ms, status=yes)
3. `AKUN-003-AEZA-NETWORK-VLESS-WS-73MS` (url=221ms, nekobox=239ms, status=yes)
4. `AKUN-004-VULTR-VLESS-WS-63MS` (url=206ms, nekobox=234ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=214ms, nekobox=231ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS` (url=227ms, nekobox=261ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-90MS` (url=220ms, nekobox=319ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-84MS` (url=205ms, nekobox=254ms, status=yes)
9. `AKUN-009-SAINT-PETERSBURG-VLESS-WS-88MS` (url=212ms, nekobox=262ms, status=yes)
10. `AKUN-010-WPENG-VLESS-WS-86MS` (url=215ms, nekobox=224ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-91MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-108MS` (url=206ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-85MS` (url=205ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-127MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-96MS` (url=219ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-128MS` (url=216ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-127MS` (url=209ms, status=HTTP 204)
18. `AKUN-018-WPENG-VLESS-WS-83MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-111MS` (url=213ms, status=HTTP 204)
20. `AKUN-020-COMPREND-NET-VLESS-WS-115MS` (url=221ms, status=HTTP 204)
21. `AKUN-021-COMPREND-NET-VLESS-WS-72MS` (url=214ms, status=HTTP 204)
22. `AKUN-022-ZOOM-VLESS-WS-90MS` (url=212ms, status=HTTP 204)
23. `AKUN-023-PAGES-VLESS-WS-166MS` (url=212ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-234MS` (url=503ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-246MS` (url=485ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
