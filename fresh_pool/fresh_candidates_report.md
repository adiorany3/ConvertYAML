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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-84MS` (url=228ms, nekobox=201ms, status=no)
2. `AKUN-002-DEV-VLESS-WS-71MS` (url=227ms, nekobox=205ms, status=no)
3. `AKUN-003-DEV-VLESS-WS-76MS` (url=203ms, nekobox=186ms, status=no)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=249ms, nekobox=201ms, status=no)
5. `AKUN-001-UNKNOWN-VLESS-WS-93MS`
6. `AKUN-002-UNKNOWN-VLESS-WS-105MS`
7. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS`
8. `AKUN-004-CLOUDFLARE-VLESS-WS-92MS`
9. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS`
10. `AKUN-006-CLOUDFLARE-VLESS-WS-118MS`
11. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-78MS`
12. `AKUN-008-CLOUDFLARE-VLESS-WS-142MS`
13. `AKUN-009-CLOUDFLARE-VLESS-WS-258MS`
14. `AKUN-015-CLOUDFLARE-VLESS-WS-297MS` (url=2359ms, nekobox=405ms, status=no)
15. `AKUN-010-CLOUDFLARE-VLESS-WS-308MS`
16. `AKUN-017-CLOUDFLARE-VLESS-WS-306MS` (url=2419ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-350MS` (url=615ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-436MS` (url=787ms, status=HTTP 204)
19. `AKUN-021-GSMVPTUN-VLESS-WS-439MS` (url=851ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-461MS` (url=792ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-436MS` (url=750ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-488MS` (url=752ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-275MS` (url=2337ms, status=HTTP 204)
24. `AKUN-031-IRATOM-VLESS-WS-446MS` (url=1406ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-375MS` (url=681ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
