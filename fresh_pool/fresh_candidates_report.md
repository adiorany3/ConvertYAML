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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=205ms, nekobox=247ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-70MS` (url=206ms, nekobox=252ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-92MS` (url=198ms, nekobox=235ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-106MS` (url=220ms, nekobox=236ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-103MS` (url=226ms, nekobox=244ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-96MS` (url=229ms, nekobox=258ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-110MS` (url=247ms, nekobox=7177ms, status=no)
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-112MS`
9. `AKUN-008-UK-GB-DCL-01-20191003-VLESS-WS-118MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-126MS`
11. `AKUN-010-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-84MS`
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS` (url=212ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-120MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-93MS` (url=199ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-261MS` (url=580ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-283MS` (url=574ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-297MS` (url=555ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-289MS` (url=539ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-263MS` (url=519ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-368MS` (url=549ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-270MS` (url=549ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-281MS` (url=526ms, status=HTTP 204)
23. `AKUN-027-RS-RAPIDSEEDBOX-20190717-VLESS-WS-453MS` (url=691ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-102MS` (url=232ms, status=HTTP 204)
25. `AKUN-031-RS-RAPIDSEEDBOX-20190717-VLESS-WS-504MS` (url=820ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
