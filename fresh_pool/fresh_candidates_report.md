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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=227ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-63MS` (url=222ms, nekobox=275ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-66MS` (url=212ms, nekobox=251ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-63MS` (url=219ms, nekobox=244ms, status=yes)
5. `AKUN-005-UK-GB-DCL-01-20191003-VLESS-WS-67MS` (url=215ms, nekobox=251ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=217ms, nekobox=259ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-61MS` (url=230ms, nekobox=255ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-69MS` (url=219ms, nekobox=251ms, status=yes)
9. `AKUN-009-WEYRO-NET-VLESS-WS-85MS` (url=231ms, nekobox=255ms, status=yes)
10. `AKUN-010-WPENG-VLESS-WS-104MS` (url=225ms, nekobox=268ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-95MS` (url=241ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-102MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-466688-VLESS-WS-94MS` (url=233ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-128MS` (url=234ms, status=HTTP 204)
15. `AKUN-015-WEYRO-NET-VLESS-WS-134MS` (url=226ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-221MS` (url=722ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-346MS` (url=773ms, status=HTTP 204)
18. `AKUN-019-CONFLU-VLESS-WS-354MS` (url=719ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-378MS` (url=805ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-368MS` (url=831ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-369MS` (url=832ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-380MS` (url=807ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-64MS` (url=920ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-669MS` (url=1079ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-644MS` (url=1095ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
