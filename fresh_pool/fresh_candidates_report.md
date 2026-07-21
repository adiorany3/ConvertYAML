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
1. `AKUN-001-UNKNOWN-VLESS-WS-94MS` (url=221ms, nekobox=246ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-94MS` (url=224ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-102MS` (url=226ms, nekobox=255ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-105MS` (url=244ms, nekobox=245ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-114MS` (url=259ms, nekobox=299ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-136MS` (url=230ms, nekobox=272ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-132MS` (url=264ms, nekobox=295ms, status=yes)
8. `AKUN-008-DEV-VLESS-WS-114MS` (url=261ms, nekobox=248ms, status=yes)
9. `AKUN-009-DEV-VLESS-WS-132MS` (url=223ms, nekobox=252ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-105MS` (url=229ms, nekobox=257ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-144MS` (url=245ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-117MS` (url=301ms, status=HTTP 204)
13. `AKUN-013-UK-GB-DCL-01-20191003-VLESS-WS-160MS` (url=329ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-120MS` (url=286ms, status=HTTP 204)
15. `AKUN-015-SHOPIFY-VLESS-WS-161MS` (url=252ms, status=HTTP 204)
16. `AKUN-016-1PASSWORD-VLESS-WS-183MS` (url=241ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-174MS` (url=216ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-191MS` (url=293ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-151MS` (url=255ms, status=HTTP 204)
20. `AKUN-020-UK-GB-DCL-01-20191003-VLESS-WS-123MS` (url=257ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-149MS` (url=441ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-106MS` (url=209ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-156MS` (url=325ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-144MS` (url=319ms, status=HTTP 204)
25. `AKUN-025-ZOOM-VLESS-WS-124MS` (url=234ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
