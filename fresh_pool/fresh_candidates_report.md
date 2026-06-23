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
1. `AKUN-001-090227-VLESS-WS-65MS` (url=217ms, nekobox=244ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS` (url=212ms, nekobox=242ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS` (url=201ms, nekobox=246ms, status=yes)
4. `AKUN-004-BROADNNET-KR-VLESS-WS-72MS` (url=217ms, nekobox=281ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS` (url=226ms, nekobox=245ms, status=yes)
6. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-104MS` (url=212ms, nekobox=241ms, status=yes)
7. `AKUN-007-KIRINO-31-25-88-0-24-VLESS-WS-121MS` (url=220ms, nekobox=260ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS` (url=226ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=218ms, nekobox=262ms, status=yes)
10. `AKUN-010-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-88MS` (url=216ms, nekobox=242ms, status=yes)
11. `AKUN-011-BROADNNET-KR-VLESS-WS-106MS` (url=205ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-90MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-DIGITALOCEAN-VLESS-WS-107MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-70MS` (url=282ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-399MS` (url=847ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-351MS` (url=704ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-424MS` (url=864ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-414MS` (url=843ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-375MS` (url=746ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-397MS` (url=914ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-353MS` (url=725ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-602MS` (url=1045ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-698MS` (url=964ms, status=HTTP 204)
24. `AKUN-031-RS-RAPIDSEEDBOX-20190717-VLESS-WS-765MS` (url=1298ms, status=HTTP 204)
25. `AKUN-034-UNKNOWN-VLESS-WS-809MS` (url=1252ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
