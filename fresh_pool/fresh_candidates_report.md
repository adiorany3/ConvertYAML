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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=231ms, nekobox=250ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-63MS` (url=221ms, nekobox=247ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-61MS` (url=213ms, nekobox=257ms, status=yes)
4. `AKUN-004-466688-VLESS-WS-69MS` (url=218ms, nekobox=240ms, status=yes)
5. `AKUN-005-SAVVY-7-VLESS-WS-60MS` (url=227ms, nekobox=250ms, status=yes)
6. `AKUN-006-US-VLESS-WS-72MS` (url=200ms, nekobox=234ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-81MS` (url=218ms, nekobox=253ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-90MS` (url=204ms, nekobox=257ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-88MS` (url=199ms, nekobox=274ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-90MS` (url=270ms, nekobox=244ms, status=yes)
11. `AKUN-011-UK-GB-DCL-01-20191003-VLESS-WS-92MS` (url=205ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-102MS` (url=226ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-95MS` (url=199ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-63MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-78MS` (url=243ms, status=HTTP 204)
16. `AKUN-016-UK-GB-DCL-01-20191003-VLESS-WS-104MS` (url=232ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-77MS` (url=211ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-96MS` (url=254ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-105MS` (url=224ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-113MS` (url=227ms, status=HTTP 204)
21. `AKUN-021-UK-GB-DCL-01-20191003-VLESS-WS-114MS` (url=226ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-68MS` (url=259ms, status=HTTP 204)
23. `AKUN-023-WEBEX-VLESS-WS-109MS` (url=209ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-131MS` (url=260ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-127MS` (url=225ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
