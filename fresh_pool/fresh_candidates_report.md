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
1. `AKUN-001-IONOS-VLESS-WS-65MS` (url=211ms, nekobox=234ms, status=yes)
2. `AKUN-002-DIGITALOCEAN-VLESS-WS-84MS` (url=214ms, nekobox=263ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-96MS` (url=224ms, nekobox=242ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-71MS` (url=227ms, nekobox=264ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=226ms, nekobox=256ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=220ms, nekobox=239ms, status=yes)
7. `AKUN-007-WEYRO-NET-VLESS-WS-98MS` (url=208ms, nekobox=261ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-77MS` (url=211ms, nekobox=265ms, status=yes)
9. `AKUN-009-NODEJS-VLESS-WS-88MS` (url=220ms, nekobox=190ms, status=no)
10. `AKUN-010-SPEEDTEST-VLESS-WS-111MS` (url=223ms, nekobox=195ms, status=no)
11. `AKUN-009-UNKNOWN-VLESS-WS-134MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-78MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-82MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-76MS` (url=205ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-73MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-96MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-68MS` (url=228ms, status=HTTP 204)
18. `AKUN-019-WPENG-VLESS-WS-81MS` (url=202ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-88MS` (url=203ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-114MS` (url=225ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-173MS` (url=856ms, status=HTTP 204)
22. `AKUN-024-SPEEDTEST-VLESS-WS-237MS` (url=497ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-236MS` (url=492ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-259MS` (url=542ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-243MS` (url=496ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
