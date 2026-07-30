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
1. `AKUN-001-DEV-VLESS-WS-104MS` (url=294ms, nekobox=773ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-105MS` (url=274ms, nekobox=777ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS` (url=271ms, nekobox=314ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-106MS` (url=780ms, nekobox=324ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-108MS` (url=348ms, nekobox=802ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-121MS` (url=758ms, nekobox=359ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-102MS` (url=652ms, nekobox=297ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-183MS` (url=815ms, nekobox=892ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-170MS` (url=391ms, nekobox=934ms, status=yes)
10. `AKUN-010-NET-141-11-202-0-23-VLESS-WS-334MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-105MS` (url=261ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-141MS` (url=759ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-114MS` (url=246ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-95MS` (url=273ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-97MS` (url=759ms, status=HTTP 204)
16. `AKUN-018-ZOOM-VLESS-WS-109MS` (url=273ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-111MS` (url=758ms, status=HTTP 204)
18. `AKUN-020-008500-VLESS-WS-119MS` (url=330ms, status=HTTP 204)
19. `AKUN-021-DEV-VLESS-WS-122MS` (url=295ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-105MS` (url=296ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-115MS` (url=763ms, status=HTTP 204)
22. `AKUN-024-CCWU-VLESS-WS-157MS` (url=761ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-112MS` (url=783ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-113MS` (url=298ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-123MS` (url=811ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
