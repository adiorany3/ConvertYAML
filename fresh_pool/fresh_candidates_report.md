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
1. `AKUN-001-UNKNOWN-VLESS-WS-83MS` (url=262ms, nekobox=252ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-96MS` (url=271ms, nekobox=233ms, status=yes)
3. `AKUN-003-U1HOST-FRA-VLESS-WS-98MS` (url=238ms, nekobox=237ms, status=yes)
4. `AKUN-004-DIGITALOCEAN-VLESS-WS-104MS` (url=217ms, nekobox=271ms, status=yes)
5. `AKUN-005-NETCUP-VLESS-WS-90MS` (url=226ms, nekobox=264ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS` (url=211ms, nekobox=7176ms, status=no)
7. `AKUN-006-UNKNOWN-VLESS-WS-85MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-105MS`
9. `AKUN-008-ORACLE-VLESS-WS-74MS`
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-109MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-116MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-123MS` (url=238ms, status=HTTP 204)
13. `AKUN-014-ADF-VLESS-WS-119MS` (url=254ms, status=HTTP 204)
14. `AKUN-015-1PASSWORD-VLESS-WS-100MS` (url=247ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-95MS` (url=246ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-102MS` (url=240ms, status=HTTP 204)
17. `AKUN-018-MEDIUM-VLESS-WS-119MS` (url=222ms, status=HTTP 204)
18. `AKUN-019-DEV-VLESS-WS-118MS` (url=233ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-103MS` (url=223ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-121MS` (url=237ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-103MS` (url=242ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-92MS` (url=226ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-431MS` (url=4367ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-417MS` (url=903ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-125MS` (url=292ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
