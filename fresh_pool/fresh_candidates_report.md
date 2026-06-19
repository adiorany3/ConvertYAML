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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=198ms, nekobox=255ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-79MS` (url=217ms, nekobox=257ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS` (url=221ms, nekobox=257ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-84MS` (url=210ms, nekobox=189ms, status=no)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS` (url=229ms, nekobox=199ms, status=no)
6. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-78MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-107MS` (url=229ms, nekobox=208ms, status=no)
11. `AKUN-008-CLOUDFLARE-VLESS-WS-100MS`
12. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-88MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-227MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-265MS` (url=554ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-259MS` (url=574ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-273MS` (url=581ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-251MS` (url=3332ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-266MS` (url=592ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-410MS` (url=619ms, status=HTTP 204)
20. `AKUN-024-UNKNOWN-VLESS-WS-449MS` (url=900ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-392MS` (url=625ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-388MS` (url=607ms, status=HTTP 204)
23. `AKUN-032-CLOUDFLARE-VLESS-WS-583MS` (url=1140ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-524MS` (url=1143ms, status=HTTP 204)
25. `AKUN-035-CLOUDFLARE-VLESS-WS-641MS` (url=1738ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
