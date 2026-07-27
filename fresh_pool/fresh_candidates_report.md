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
1. `AKUN-001-UNKNOWN-VLESS-WS-73MS` (url=219ms, nekobox=254ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-73MS` (url=225ms, nekobox=258ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS` (url=226ms, nekobox=261ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-85MS` (url=222ms, nekobox=252ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-81MS` (url=228ms, nekobox=252ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-103MS` (url=231ms, nekobox=252ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-103MS` (url=234ms, nekobox=262ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-107MS` (url=225ms, nekobox=249ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-70MS` (url=224ms, nekobox=261ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS` (url=223ms, nekobox=261ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-87MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-121MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-75MS` (url=201ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-96MS` (url=206ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-109MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-130MS` (url=241ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-141MS` (url=220ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-125MS` (url=220ms, status=HTTP 204)
19. `AKUN-020-ZVC-VLESS-WS-74MS` (url=210ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-122MS` (url=227ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-74MS` (url=234ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-102MS` (url=220ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-352MS` (url=749ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-114MS` (url=342ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-366MS` (url=856ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
