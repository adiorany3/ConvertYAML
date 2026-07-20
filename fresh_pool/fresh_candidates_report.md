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
1. `AKUN-001-UNKNOWN-VLESS-WS-62MS` (url=233ms, nekobox=262ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=235ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=227ms, nekobox=252ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=234ms, nekobox=258ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-89MS` (url=254ms, nekobox=259ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-97MS` (url=266ms, nekobox=277ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-93MS` (url=288ms, nekobox=269ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-75MS` (url=247ms, nekobox=284ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-78MS` (url=251ms, nekobox=276ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS` (url=283ms, nekobox=300ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-104MS` (url=230ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-85MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-79MS` (url=250ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-96MS` (url=265ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-83MS` (url=242ms, status=HTTP 204)
16. `AKUN-016-UK-GB-DCL-01-20191003-VLESS-WS-123MS` (url=292ms, status=HTTP 204)
17. `AKUN-017-UK-GB-DCL-01-20191003-VLESS-WS-131MS` (url=255ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-97MS` (url=226ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-111MS` (url=257ms, status=HTTP 204)
20. `AKUN-020-466688-VLESS-WS-81MS` (url=252ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-110MS` (url=230ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-102MS` (url=246ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-77MS` (url=244ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-72MS` (url=230ms, status=HTTP 204)
25. `AKUN-025-WEBEX-VLESS-WS-117MS` (url=276ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
