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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=226ms, nekobox=262ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-81MS` (url=219ms, nekobox=255ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-84MS` (url=229ms, nekobox=258ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-82MS` (url=203ms, nekobox=237ms, status=yes)
5. `AKUN-005-UK-GB-DCL-01-20191003-VLESS-WS-84MS` (url=240ms, nekobox=229ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=208ms, nekobox=229ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-91MS` (url=206ms, nekobox=251ms, status=yes)
8. `AKUN-008-HOSTOFF-NET-VLESS-WS-89MS` (url=222ms, nekobox=235ms, status=yes)
9. `AKUN-009-U1HOST-FRA-VLESS-WS-92MS` (url=218ms, nekobox=238ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-105MS` (url=239ms, nekobox=243ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-96MS` (url=224ms, status=HTTP 204)
12. `AKUN-012-SPACECORE-VLESS-WS-84MS` (url=203ms, status=HTTP 204)
13. `AKUN-013-DIGITALOCEAN-VLESS-WS-120MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-112MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-WEYRO-NET-VLESS-WS-109MS` (url=279ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-120MS` (url=216ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-86MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-88MS` (url=212ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-117MS` (url=229ms, status=HTTP 204)
20. `AKUN-020-WPENG-VLESS-WS-115MS` (url=229ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-262MS` (url=548ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-263MS` (url=502ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-263MS` (url=580ms, status=HTTP 204)
24. `AKUN-024-SPEEDTEST-VLESS-WS-280MS` (url=527ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-249MS` (url=581ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
