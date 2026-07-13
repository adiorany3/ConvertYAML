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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-96MS` (url=232ms, nekobox=239ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-87MS` (url=221ms, nekobox=271ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-89MS` (url=283ms, nekobox=251ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-98MS` (url=223ms, nekobox=239ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-103MS` (url=212ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=205ms, nekobox=239ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-107MS` (url=265ms, nekobox=281ms, status=yes)
8. `AKUN-008-IDC-SG-VLESS-WS-115MS` (url=264ms, nekobox=278ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-104MS` (url=225ms, nekobox=242ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-129MS` (url=253ms, nekobox=255ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-133MS` (url=258ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-112MS` (url=244ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-116MS` (url=293ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-133MS` (url=385ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-106MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-95MS` (url=243ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-121MS` (url=253ms, status=HTTP 204)
18. `AKUN-018-MYBB-VLESS-WS-117MS` (url=237ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-98MS` (url=230ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-154MS` (url=255ms, status=HTTP 204)
21. `AKUN-021-1PASSWORD-VLESS-WS-102MS` (url=230ms, status=HTTP 204)
22. `AKUN-022-DEV-VLESS-WS-132MS` (url=261ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-122MS` (url=228ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-179MS` (url=237ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-112MS` (url=245ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
