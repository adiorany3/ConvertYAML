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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-74MS` (url=225ms, nekobox=237ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-70MS` (url=203ms, nekobox=233ms, status=yes)
3. `AKUN-003-ADF-VLESS-WS-89MS` (url=204ms, nekobox=242ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS` (url=210ms, nekobox=234ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-93MS` (url=223ms, nekobox=265ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-72MS` (url=235ms, nekobox=244ms, status=yes)
7. `AKUN-007-NET-NL-VLESS-WS-72MS` (url=229ms, nekobox=246ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS` (url=208ms, nekobox=236ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-107MS` (url=222ms, nekobox=254ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-102MS` (url=252ms, nekobox=253ms, status=yes)
11. `AKUN-011-DIGITALOCEAN-VLESS-WS-91MS` (url=213ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-92MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-NETCUP-VLESS-WS-97MS` (url=214ms, status=HTTP 204)
14. `AKUN-014-MYBB-VLESS-WS-109MS` (url=195ms, status=HTTP 204)
15. `AKUN-015-MEDIUM-VLESS-WS-80MS` (url=227ms, status=HTTP 204)
16. `AKUN-016-U1HOST-FRA-VLESS-WS-89MS` (url=203ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-90MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-SPACECORE-VLESS-WS-85MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-90MS` (url=206ms, status=HTTP 204)
20. `AKUN-020-CONFLU-VLESS-WS-244MS` (url=506ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-238MS` (url=503ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-240MS` (url=506ms, status=HTTP 204)
23. `AKUN-023-WPENG-VLESS-WS-262MS` (url=587ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-269MS` (url=551ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-279MS` (url=569ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
