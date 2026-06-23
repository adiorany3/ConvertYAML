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
1. `AKUN-001-DEV-VLESS-WS-72MS` (url=201ms, nekobox=183ms, status=no)
2. `AKUN-001-UNKNOWN-VLESS-WS-67MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-85MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS`
6. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS` (url=198ms, nekobox=175ms, status=no)
7. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-66MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS`
9. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-69MS`
10. `AKUN-011-CLOUDFLARE-VLESS-WS-94MS` (url=197ms, nekobox=188ms, status=no)
11. `AKUN-008-CLOUDFLARE-VLESS-WS-71MS`
12. `AKUN-009-BIGCOMMERCE-VLESS-WS-97MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-84MS` (url=192ms, nekobox=176ms, status=no)
14. `AKUN-015-DEV-VLESS-WS-77MS` (url=195ms, nekobox=180ms, status=no)
15. `AKUN-016-DEV-VLESS-WS-72MS` (url=203ms, nekobox=192ms, status=no)
16. `AKUN-017-DEV-VLESS-WS-73MS` (url=188ms, nekobox=180ms, status=no)
17. `AKUN-010-UNKNOWN-VLESS-WS-96MS`
18. `AKUN-019-UNKNOWN-VLESS-WS-79MS` (url=220ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-114MS` (url=217ms, status=HTTP 204)
20. `AKUN-021-DEV-VLESS-WS-80MS` (url=197ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-117MS` (url=205ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-118MS` (url=204ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-394MS` (url=853ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-403MS` (url=811ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-346MS` (url=761ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
