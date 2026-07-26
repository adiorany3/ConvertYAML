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
1. `AKUN-001-UNKNOWN-VLESS-WS-57MS` (url=226ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=223ms, nekobox=251ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-62MS` (url=238ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=220ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-59MS` (url=235ms, nekobox=242ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-56MS` (url=237ms, nekobox=264ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-65MS` (url=227ms, nekobox=269ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-59MS` (url=218ms, nekobox=257ms, status=yes)
9. `AKUN-009-008500-VLESS-WS-61MS` (url=222ms, nekobox=242ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-68MS` (url=229ms, nekobox=256ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-69MS` (url=219ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-70MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-67MS` (url=202ms, status=HTTP 204)
14. `AKUN-014-ZOOM-VLESS-WS-59MS` (url=241ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-64MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-70MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-75MS` (url=247ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-65MS` (url=227ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-77MS` (url=230ms, status=HTTP 204)
20. `AKUN-020-CCWU-VLESS-WS-68MS` (url=225ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-68MS` (url=245ms, status=HTTP 204)
22. `AKUN-022-1PASSWORD-VLESS-WS-88MS` (url=201ms, status=HTTP 204)
23. `AKUN-023-MYBB-VLESS-WS-124MS` (url=210ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-324MS` (url=685ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-361MS` (url=745ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
