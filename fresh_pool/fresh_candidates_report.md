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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-97MS` (url=339ms, nekobox=301ms, status=yes)
2. `AKUN-002-ICOOK-VLESS-WS-95MS` (url=267ms, nekobox=269ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-101MS` (url=246ms, nekobox=316ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-111MS` (url=237ms, nekobox=305ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-93MS` (url=252ms, nekobox=274ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-107MS` (url=241ms, nekobox=266ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-107MS` (url=255ms, nekobox=221ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-115MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-115MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-112MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-115MS` (url=224ms, nekobox=212ms, status=no)
12. `AKUN-010-FMN5-RENTED-NET2-VLESS-WS-96MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-117MS` (url=240ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-112MS` (url=334ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-113MS` (url=261ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-119MS` (url=266ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-93MS` (url=258ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-100MS` (url=249ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-95MS` (url=263ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-111MS` (url=241ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-110MS` (url=269ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-140MS` (url=253ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-133MS` (url=287ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-133MS` (url=281ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-132MS` (url=271ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
