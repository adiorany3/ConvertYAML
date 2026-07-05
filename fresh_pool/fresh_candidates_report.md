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
1. `AKUN-001-CNAE-VLESS-WS-101MS` (url=273ms, nekobox=296ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-103MS` (url=241ms, nekobox=319ms, status=yes)
3. `AKUN-003-WEBEX-VLESS-WS-88MS` (url=294ms, nekobox=298ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-104MS` (url=224ms, nekobox=278ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-103MS` (url=232ms, nekobox=265ms, status=yes)
6. `AKUN-006-INTERNETWORKS-45-131-208-VLESS-WS-114MS` (url=274ms, nekobox=307ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS` (url=245ms, nekobox=314ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-105MS` (url=267ms, nekobox=316ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-119MS` (url=256ms, nekobox=281ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-121MS` (url=262ms, nekobox=277ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-122MS` (url=275ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-103MS` (url=278ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-135MS` (url=317ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-102MS` (url=301ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-104MS` (url=266ms, status=HTTP 204)
16. `AKUN-016-WEYRO-NET-VLESS-WS-126MS` (url=303ms, status=HTTP 204)
17. `AKUN-018-WEBEX-VLESS-WS-106MS` (url=272ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-152MS` (url=287ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-306MS` (url=594ms, status=HTTP 204)
20. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-306MS` (url=756ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-317MS` (url=761ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-319MS` (url=739ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-339MS` (url=667ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-374MS` (url=630ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-314MS` (url=609ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
