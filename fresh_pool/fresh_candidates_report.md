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
1. `AKUN-001-ORACLE-VLESS-WS-79MS` (url=258ms, nekobox=285ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=253ms, nekobox=183ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-91MS`
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-81MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-101MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-89MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-108MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS` (url=274ms, nekobox=199ms, status=no)
9. `AKUN-007-CLOUDFLARE-VLESS-WS-107MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-80MS` (url=273ms, nekobox=204ms, status=no)
11. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-92MS`
12. `AKUN-012-DEV-VLESS-WS-119MS` (url=256ms, nekobox=190ms, status=no)
13. `AKUN-009-UNKNOWN-VLESS-WS-83MS`
14. `AKUN-010-UNKNOWN-VLESS-WS-84MS`
15. `AKUN-015-DEV-VLESS-WS-85MS` (url=255ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-79MS` (url=247ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-82MS` (url=272ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-80MS` (url=260ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-145MS` (url=268ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-282MS` (url=572ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-93MS` (url=271ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-301MS` (url=677ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-289MS` (url=549ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-319MS` (url=670ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-296MS` (url=656ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
