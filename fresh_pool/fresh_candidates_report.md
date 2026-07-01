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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=216ms, nekobox=235ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=197ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS` (url=210ms, nekobox=257ms, status=yes)
4. `AKUN-004-COMPREND-NET-VLESS-WS-84MS` (url=203ms, nekobox=254ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-85MS` (url=222ms, nekobox=234ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-93MS` (url=215ms, nekobox=244ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=212ms, nekobox=243ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-103MS` (url=204ms, nekobox=240ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-90MS` (url=246ms, nekobox=230ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-100MS` (url=202ms, nekobox=232ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-111MS` (url=239ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-98MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-124MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-96MS` (url=198ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-147MS` (url=281ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-69MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-80MS` (url=211ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-140MS` (url=213ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-237MS` (url=679ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-235MS` (url=509ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-238MS` (url=560ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-263MS` (url=577ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-272MS` (url=598ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-270MS` (url=570ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-284MS` (url=584ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
