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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=198ms, nekobox=226ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=205ms, nekobox=248ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-73MS` (url=197ms, nekobox=235ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=219ms, nekobox=242ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=197ms, nekobox=238ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS` (url=196ms, nekobox=225ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=221ms, nekobox=247ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS` (url=200ms, nekobox=241ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS` (url=217ms, nekobox=245ms, status=yes)
10. `AKUN-010-UK-GB-DCL-01-20191003-VLESS-WS-103MS` (url=235ms, nekobox=257ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-76MS` (url=217ms, status=HTTP 204)
12. `AKUN-012-DEV-VLESS-WS-102MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-WEBEX-VLESS-WS-107MS` (url=211ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-81MS` (url=210ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-117MS` (url=234ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-109MS` (url=201ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-118MS` (url=209ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-98MS` (url=217ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-107MS` (url=225ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-120MS` (url=214ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-114MS` (url=218ms, status=HTTP 204)
22. `AKUN-022-DEV-VLESS-WS-77MS` (url=224ms, status=HTTP 204)
23. `AKUN-023-DEV-VLESS-WS-107MS` (url=215ms, status=HTTP 204)
24. `AKUN-024-POLICE-VLESS-WS-99MS` (url=209ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-105MS` (url=219ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
