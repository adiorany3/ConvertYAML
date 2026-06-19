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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=241ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-68MS` (url=241ms, nekobox=232ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-66MS` (url=223ms, nekobox=245ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-69MS` (url=216ms, nekobox=177ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-100MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-83MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS` (url=220ms, nekobox=186ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-68MS`
12. `AKUN-010-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-131MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-91MS` (url=203ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-113MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-MYBB-VLESS-WS-101MS` (url=252ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-357MS` (url=734ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-392MS` (url=838ms, status=HTTP 204)
18. `AKUN-019-MICROSOFT-VLESS-WS-397MS` (url=799ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-399MS` (url=2367ms, status=HTTP 204)
20. `AKUN-021-ADF-VLESS-WS-75MS` (url=238ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-410MS` (url=853ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-376MS` (url=833ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-543MS` (url=1540ms, status=HTTP 204)
24. `AKUN-028-UNKNOWN-VLESS-WS-707MS` (url=1092ms, status=HTTP 204)
25. `AKUN-032-UNKNOWN-VLESS-WS-742MS` (url=1174ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
