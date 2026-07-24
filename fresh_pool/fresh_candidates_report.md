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
1. `AKUN-001-UNKNOWN-VLESS-WS-84MS` (url=269ms, nekobox=301ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-85MS` (url=269ms, nekobox=302ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS` (url=298ms, nekobox=371ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS` (url=255ms, nekobox=361ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-104MS` (url=276ms, nekobox=328ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-107MS` (url=319ms, nekobox=302ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-109MS` (url=276ms, nekobox=291ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS` (url=260ms, nekobox=303ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-122MS` (url=319ms, nekobox=297ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-124MS` (url=278ms, nekobox=330ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-108MS` (url=266ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-86MS` (url=315ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-114MS` (url=315ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-105MS` (url=290ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-136MS` (url=279ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-153MS` (url=254ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-105MS` (url=284ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-87MS` (url=285ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-134MS` (url=271ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-135MS` (url=377ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-168MS` (url=427ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-163MS` (url=520ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-193MS` (url=364ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-196MS` (url=422ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-281MS` (url=2679ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
