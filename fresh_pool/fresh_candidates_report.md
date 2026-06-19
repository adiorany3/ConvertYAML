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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-9889888-VLESS-WS-62MS` (url=240ms, nekobox=269ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-68MS` (url=241ms, nekobox=262ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS` (url=232ms, nekobox=267ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=244ms, nekobox=273ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-69MS` (url=253ms, nekobox=260ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=238ms, nekobox=281ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-104MS` (url=244ms, nekobox=307ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-67MS` (url=218ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-346MS` (url=743ms, nekobox=765ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-339MS` (url=777ms, nekobox=758ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-78MS` (url=227ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-376MS` (url=828ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-398MS` (url=844ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-411MS` (url=845ms, status=HTTP 204)
15. `AKUN-015-SPEEDTEST-VLESS-WS-409MS` (url=2699ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-635MS` (url=885ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-646MS` (url=888ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-609MS` (url=873ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-654MS` (url=872ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-526MS` (url=840ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-688MS` (url=506ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-391MS` (url=833ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-668MS` (url=843ms, status=HTTP 204)
24. `AKUN-032-UNKNOWN-VLESS-WS-796MS` (url=1216ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
