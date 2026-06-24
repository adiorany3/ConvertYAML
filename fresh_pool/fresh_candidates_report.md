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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=225ms, nekobox=223ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-67MS` (url=209ms, nekobox=249ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS` (url=208ms, nekobox=252ms, status=yes)
4. `AKUN-004-BROADNNET-KR-VLESS-WS-85MS` (url=232ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-118MS` (url=238ms, nekobox=251ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-121MS` (url=223ms, nekobox=257ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS` (url=199ms, nekobox=257ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-91MS` (url=200ms, nekobox=203ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-75MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-90MS` (url=213ms, nekobox=189ms, status=no)
12. `AKUN-010-CLOUDWEBMANAGE-EU-FR-VLESS-WS-115MS`
13. `AKUN-013-1PASSWORD-VLESS-WS-81MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-79MS` (url=217ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-184MS` (url=209ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-86MS` (url=228ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-68MS` (url=194ms, status=HTTP 204)
18. `AKUN-018-DIGITALOCEAN-VLESS-WS-168MS` (url=231ms, status=HTTP 204)
19. `AKUN-019-DIGITALOCEAN-VLESS-WS-69MS` (url=222ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-259MS` (url=511ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-365MS` (url=750ms, status=HTTP 204)
22. `AKUN-022-KIRINO-31-25-88-0-24-VLESS-WS-82MS` (url=218ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-381MS` (url=880ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-403MS` (url=864ms, status=HTTP 204)
25. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-418MS` (url=849ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
