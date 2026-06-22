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
1. `AKUN-001-UNKNOWN-VLESS-WS-62MS` (url=228ms, nekobox=256ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-66MS` (url=203ms, nekobox=257ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS` (url=215ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-73MS` (url=238ms, nekobox=7177ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-77MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS`
10. `AKUN-009-VULTR-VLESS-WS-78MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-116MS`
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-103MS` (url=239ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-89MS` (url=214ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-86MS` (url=203ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-414MS` (url=730ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-409MS` (url=861ms, status=HTTP 204)
17. `AKUN-018-MICROSOFT-VLESS-WS-395MS` (url=849ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-434MS` (url=865ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-437MS` (url=830ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-365MS` (url=735ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-400MS` (url=805ms, status=HTTP 204)
22. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-710MS` (url=1228ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-680MS` (url=3462ms, status=HTTP 204)
24. `AKUN-028-UNKNOWN-VLESS-WS-792MS` (url=1233ms, status=HTTP 204)
25. `AKUN-032-DEV-VLESS-WS-660MS` (url=502ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
