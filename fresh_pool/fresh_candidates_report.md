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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-53MS` (url=216ms, nekobox=232ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-55MS` (url=212ms, nekobox=235ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-58MS` (url=221ms, nekobox=238ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-66MS` (url=213ms, nekobox=245ms, status=yes)
5. `AKUN-005-CCWU-VLESS-WS-65MS` (url=215ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS` (url=211ms, nekobox=241ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-69MS` (url=215ms, nekobox=238ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-62MS` (url=223ms, nekobox=237ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS` (url=200ms, nekobox=257ms, status=yes)
10. `AKUN-010-ZOOM-VLESS-WS-59MS` (url=205ms, nekobox=236ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-64MS` (url=221ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-105MS` (url=222ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-94MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-67MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-101MS` (url=234ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-95MS` (url=222ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-86MS` (url=214ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-134MS` (url=221ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-79MS` (url=214ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-75MS` (url=223ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-122MS` (url=211ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-150MS` (url=266ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-62MS` (url=216ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-343MS` (url=2708ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-365MS` (url=1416ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
