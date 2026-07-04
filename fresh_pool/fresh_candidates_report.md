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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=227ms, nekobox=235ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-85MS` (url=233ms, nekobox=263ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=229ms, nekobox=250ms, status=yes)
4. `AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-85MS` (url=200ms, nekobox=260ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-101MS` (url=232ms, nekobox=246ms, status=yes)
6. `AKUN-006-IONIS-163-5-207-VLESS-WS-98MS` (url=253ms, nekobox=272ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-103MS` (url=236ms, nekobox=252ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-86MS` (url=224ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-95MS` (url=202ms, nekobox=238ms, status=yes)
10. `AKUN-010-WEYRO-NET-VLESS-WS-99MS` (url=293ms, nekobox=258ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-103MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-99MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-ZOOM-VLESS-WS-104MS` (url=234ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-107MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-120MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-96MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-117MS` (url=216ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-100MS` (url=219ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-146MS` (url=306ms, status=HTTP 204)
20. `AKUN-020-PAGES-VLESS-WS-169MS` (url=227ms, status=HTTP 204)
21. `AKUN-022-SPEEDTEST-VLESS-WS-247MS` (url=536ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-252MS` (url=532ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-249MS` (url=535ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-279MS` (url=586ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-283MS` (url=593ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
