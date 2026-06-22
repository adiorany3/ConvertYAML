# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-57MS` (url=436ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=236ms, nekobox=246ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-69MS` (url=213ms, nekobox=262ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-63MS` (url=218ms, nekobox=249ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS` (url=219ms, nekobox=266ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-65MS`
8. `AKUN-008-AMAZON-VLESS-WS-118MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-341MS`
11. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-381MS` (url=848ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-369MS` (url=951ms, status=HTTP 204)
13. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-389MS` (url=835ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-384MS` (url=766ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-419MS` (url=842ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-391MS` (url=870ms, status=HTTP 204)
17. `AKUN-019-BROADNNET-KR-VLESS-WS-68MS` (url=1025ms, status=HTTP 204)
18. `AKUN-021-ORG-VLESS-WS-557MS` (url=1040ms, status=HTTP 204)
19. `AKUN-024-KAWAII520-VLESS-WS-641MS` (url=1236ms, status=HTTP 204)
20. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-707MS` (url=914ms, status=HTTP 204)
21. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-730MS` (url=1203ms, status=HTTP 204)
22. `AKUN-031-CLOUDFLARE-VLESS-WS-786MS` (url=1265ms, status=HTTP 204)
23. `AKUN-032-CLOUDFLARE-VLESS-WS-841MS` (url=1394ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-793MS` (url=1292ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
