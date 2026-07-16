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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-89MS` (url=218ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=223ms, nekobox=296ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-97MS` (url=225ms, nekobox=238ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-102MS` (url=212ms, nekobox=257ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-105MS` (url=207ms, nekobox=234ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=214ms, nekobox=295ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-110MS` (url=243ms, nekobox=274ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-113MS` (url=246ms, nekobox=283ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-102MS` (url=242ms, nekobox=264ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-116MS` (url=246ms, nekobox=327ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-105MS` (url=290ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-100MS` (url=240ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-114MS` (url=246ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-106MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-116MS` (url=250ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-110MS` (url=238ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-114MS` (url=252ms, status=HTTP 204)
18. `AKUN-018-GO-DADDY-COM-LLC-VLESS-WS-129MS` (url=258ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-134MS` (url=236ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-122MS` (url=282ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-139MS` (url=230ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-88MS` (url=223ms, status=HTTP 204)
23. `AKUN-023-NEXUSMODS-VLESS-WS-119MS` (url=317ms, status=HTTP 204)
24. `AKUN-024-POLICE-VLESS-WS-159MS` (url=349ms, status=HTTP 204)
25. `AKUN-025-MEDIUM-VLESS-WS-97MS` (url=240ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
