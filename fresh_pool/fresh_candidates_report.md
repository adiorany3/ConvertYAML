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
1. `AKUN-001-UNKNOWN-VLESS-WS-57MS` (url=212ms, nekobox=248ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-70MS` (url=199ms, nekobox=228ms, status=yes)
3. `AKUN-003-WPENG-VLESS-WS-80MS` (url=202ms, nekobox=243ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-91MS` (url=202ms, nekobox=261ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-92MS` (url=206ms, nekobox=256ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-99MS` (url=213ms, nekobox=228ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-92MS` (url=216ms, nekobox=246ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-96MS` (url=230ms, nekobox=230ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-99MS` (url=216ms, nekobox=242ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-106MS` (url=233ms, nekobox=234ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-68MS` (url=201ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-92MS` (url=226ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-107MS` (url=214ms, status=HTTP 204)
14. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-100MS` (url=215ms, status=HTTP 204)
15. `AKUN-016-WEYRO-NET-VLESS-WS-125MS` (url=211ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-154MS` (url=202ms, status=HTTP 204)
17. `AKUN-018-ZOOM-VLESS-WS-83MS` (url=267ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-118MS` (url=217ms, status=HTTP 204)
19. `AKUN-020-COMPREND-NET-VLESS-WS-89MS` (url=202ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-358MS` (url=2951ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-355MS` (url=738ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-390MS` (url=815ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-368MS` (url=780ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-383MS` (url=839ms, status=HTTP 204)
25. `AKUN-027-CELESTARA-VLESS-WS-373MS` (url=825ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
