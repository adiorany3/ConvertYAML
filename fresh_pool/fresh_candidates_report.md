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
1. `AKUN-001-IPXO-VLESS-WS-86MS` (url=211ms, nekobox=244ms, status=yes)
2. `AKUN-002-466688-VLESS-WS-96MS` (url=223ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-96MS` (url=250ms, nekobox=262ms, status=yes)
4. `AKUN-004-466688-VLESS-WS-90MS` (url=245ms, nekobox=245ms, status=yes)
5. `AKUN-005-DEV-VLESS-WS-106MS` (url=265ms, nekobox=239ms, status=no)
6. `AKUN-005-UNKNOWN-VLESS-WS-96MS`
7. `AKUN-007-UNKNOWN-VLESS-WS-101MS` (url=278ms, nekobox=7178ms, status=no)
8. `AKUN-006-UNKNOWN-VLESS-WS-100MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-113MS` (url=279ms, nekobox=264ms, status=no)
10. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-103MS`
11. `AKUN-008-UNKNOWN-VLESS-WS-102MS`
12. `AKUN-009-PAGES-VLESS-WS-119MS`
13. `AKUN-010-ZOOM-VLESS-WS-122MS`
14. `AKUN-014-CZ-LOTUNA-19970206-VLESS-WS-89MS` (url=244ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-130MS` (url=324ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-129MS` (url=254ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-101MS` (url=240ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-133MS` (url=271ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-161MS` (url=236ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-163MS` (url=248ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-111MS` (url=275ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-137MS` (url=309ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-180MS` (url=239ms, status=HTTP 204)
24. `AKUN-024-WPENG-VLESS-WS-165MS` (url=245ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-109MS` (url=279ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
