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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=242ms, nekobox=260ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-58MS` (url=224ms, nekobox=255ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-61MS` (url=222ms, nekobox=254ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-63MS` (url=219ms, nekobox=254ms, status=yes)
5. `AKUN-005-GOOGLE-VLESS-WS-58MS` (url=223ms, nekobox=270ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-61MS` (url=235ms, nekobox=255ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-71MS` (url=250ms, nekobox=272ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-66MS` (url=234ms, nekobox=270ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-88MS` (url=260ms, nekobox=259ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-115MS` (url=230ms, nekobox=270ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-121MS` (url=249ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-80MS` (url=221ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-114MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-139MS` (url=234ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-134MS` (url=296ms, status=HTTP 204)
16. `AKUN-017-INTERNETWORKS-45-131-210-VLESS-WS-245MS` (url=538ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-58MS` (url=234ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-252MS` (url=659ms, status=HTTP 204)
19. `AKUN-021-NET-141-11-202-0-23-VLESS-WS-351MS` (url=664ms, status=HTTP 204)
20. `AKUN-022-SPEEDTEST-VLESS-WS-63MS` (url=254ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-64MS` (url=1010ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-62MS` (url=258ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-315MS` (url=434ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-421MS` (url=780ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-455MS` (url=799ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
