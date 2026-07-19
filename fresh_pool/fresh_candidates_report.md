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
1. `AKUN-001-SIN-VLESS-WS-101MS` (url=297ms, nekobox=375ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-101MS` (url=278ms, nekobox=299ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-107MS` (url=266ms, nekobox=326ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-111MS` (url=283ms, nekobox=323ms, status=yes)
5. `AKUN-005-DIXONS-VLESS-WS-116MS` (url=288ms, nekobox=305ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-121MS` (url=278ms, nekobox=326ms, status=yes)
7. `AKUN-007-UK-GB-DCL-01-20191003-VLESS-WS-117MS` (url=300ms, nekobox=342ms, status=yes)
8. `AKUN-008-UK-GB-DCL-01-20191003-VLESS-WS-123MS` (url=290ms, nekobox=343ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-126MS` (url=270ms, nekobox=307ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-108MS` (url=306ms, nekobox=315ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-117MS` (url=321ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-140MS` (url=287ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-139MS` (url=305ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-143MS` (url=286ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-105MS` (url=313ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-126MS` (url=302ms, status=HTTP 204)
17. `AKUN-017-POLICE-VLESS-WS-141MS` (url=287ms, status=HTTP 204)
18. `AKUN-018-WEBEX-VLESS-WS-136MS` (url=275ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-140MS` (url=300ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-187MS` (url=307ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-304MS` (url=1622ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-331MS` (url=662ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-342MS` (url=4677ms, status=HTTP 204)
24. `AKUN-024-IRCYBERSEC-VLESS-WS-316MS` (url=723ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-341MS` (url=919ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
