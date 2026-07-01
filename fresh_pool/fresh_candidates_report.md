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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-66MS` (url=208ms, nekobox=249ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-61MS` (url=222ms, nekobox=263ms, status=yes)
3. `AKUN-003-ALIBABA-VLESS-WS-66MS` (url=233ms, nekobox=231ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS` (url=225ms, nekobox=250ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-74MS` (url=238ms, nekobox=235ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS` (url=224ms, nekobox=258ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-81MS` (url=250ms, nekobox=268ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS` (url=214ms, nekobox=278ms, status=yes)
9. `AKUN-009-NET-NL-VLESS-WS-84MS` (url=249ms, nekobox=272ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-100MS` (url=226ms, nekobox=273ms, status=yes)
11. `AKUN-011-U1HOST-FRA-VLESS-WS-90MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-HOSTOFF-NET-VLESS-WS-81MS` (url=222ms, status=HTTP 204)
13. `AKUN-013-NETCUP-VLESS-WS-70MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-76MS` (url=206ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-113MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-125MS` (url=309ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-121MS` (url=245ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-103MS` (url=233ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-109MS` (url=213ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-76MS` (url=257ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-90MS` (url=203ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-153MS` (url=196ms, status=HTTP 204)
23. `AKUN-023-COMPREND-NET-VLESS-WS-170MS` (url=203ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-206MS` (url=227ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-355MS` (url=751ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
