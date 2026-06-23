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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-59MS` (url=223ms, nekobox=243ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-63MS` (url=217ms, nekobox=236ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-72MS` (url=218ms, nekobox=247ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-71MS` (url=198ms, nekobox=181ms, status=no)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-69MS` (url=201ms, nekobox=186ms, status=no)
6. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-95MS`
7. `AKUN-007-DEV-VLESS-WS-77MS` (url=198ms, nekobox=178ms, status=no)
8. `AKUN-005-BROADNNET-KR-VLESS-WS-81MS`
9. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS`
10. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS`
11. `AKUN-011-DEV-VLESS-WS-72MS` (url=211ms, nekobox=178ms, status=no)
12. `AKUN-008-BROADNNET-KR-VLESS-WS-86MS`
13. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-114MS` (url=198ms, nekobox=177ms, status=no)
15. `AKUN-010-UK-GB-DCL-01-20191003-VLESS-WS-120MS`
16. `AKUN-016-CLOUDFLARE-VLESS-WS-368MS` (url=746ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-359MS` (url=739ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-382MS` (url=852ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-410MS` (url=829ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-394MS` (url=876ms, status=HTTP 204)
21. `AKUN-021-CONFLU-VLESS-WS-348MS` (url=753ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-678MS` (url=1000ms, status=HTTP 204)
23. `AKUN-032-UNKNOWN-VLESS-WS-795MS` (url=1359ms, status=HTTP 204)
24. `AKUN-033-RS-RAPIDSEEDBOX-20190717-VLESS-WS-752MS` (url=2243ms, status=HTTP 204)
25. `AKUN-034-NET-89-116-72-0-24-VLESS-WS-764MS` (url=1474ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
