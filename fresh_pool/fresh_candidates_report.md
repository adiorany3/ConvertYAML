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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=231ms, nekobox=256ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-74MS` (url=652ms, nekobox=669ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS` (url=206ms, nekobox=184ms, status=no)
4. `AKUN-003-UNKNOWN-VLESS-WS-73MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-79MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-93MS`
7. `AKUN-008-CLOUDFLARE-VLESS-WS-75MS` (url=225ms, nekobox=189ms, status=no)
8. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS`
10. `AKUN-008-UNKNOWN-VLESS-WS-106MS`
11. `AKUN-009-CCWU-VLESS-WS-107MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS`
13. `AKUN-015-SPEEDTEST-VLESS-WS-102MS` (url=227ms, status=HTTP 204)
14. `AKUN-016-UNKNOWN-VLESS-WS-107MS` (url=237ms, status=HTTP 204)
15. `AKUN-017-MEDIUM-VLESS-WS-114MS` (url=226ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-88MS` (url=218ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-104MS` (url=222ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-109MS` (url=221ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-97MS` (url=241ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-154MS` (url=218ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-142MS` (url=237ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-189MS` (url=304ms, status=HTTP 204)
23. `AKUN-025-NET-141-11-202-0-23-VLESS-WS-235MS` (url=494ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-108MS` (url=211ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-413MS` (url=673ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
