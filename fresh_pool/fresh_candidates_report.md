# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-82MS` (url=227ms, nekobox=258ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=215ms, nekobox=265ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-77MS` (url=5147ms, status=ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=5.0))
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-81MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-83MS`
7. `AKUN-007-ZVC-VLESS-WS-82MS`
8. `AKUN-008-CCWU-VLESS-WS-105MS`
9. `AKUN-009-GOOGLE-VLESS-WS-77MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-91MS`
11. `AKUN-013-SPEEDTEST-VLESS-WS-149MS` (url=213ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-185MS` (url=390ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-352MS` (url=752ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-362MS` (url=749ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-335MS` (url=2360ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-348MS` (url=779ms, status=HTTP 204)
17. `AKUN-023-DEV-VLESS-WS-83MS` (url=855ms, status=HTTP 204)
18. `AKUN-024-CLOUDFLARE-VLESS-WS-656MS` (url=1399ms, status=HTTP 204)
19. `AKUN-027-CLOUDFLARE-VLESS-WS-662MS` (url=1674ms, status=HTTP 204)
20. `AKUN-028-CLOUDFLARE-VLESS-WS-761MS` (url=1608ms, status=HTTP 204)
21. `AKUN-031-CLOUDFLARE-VLESS-WS-802MS` (url=1327ms, status=HTTP 204)
22. `AKUN-032-CLOUDFLARE-VLESS-WS-796MS` (url=1348ms, status=HTTP 204)
23. `AKUN-033-UNKNOWN-VLESS-WS-792MS` (url=1283ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-792MS` (url=1350ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
