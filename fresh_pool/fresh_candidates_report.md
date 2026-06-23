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
1. `AKUN-001-ALIBABA-VLESS-WS-89MS` (url=229ms, nekobox=235ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS` (url=229ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS` (url=235ms, nekobox=232ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-116MS` (url=250ms, nekobox=253ms, status=yes)
5. `AKUN-005-UK-GB-DCL-01-20191003-VLESS-WS-119MS` (url=316ms, nekobox=235ms, status=yes)
6. `AKUN-006-ALIBABA-VLESS-WS-84MS` (url=205ms, nekobox=236ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS` (url=202ms, nekobox=235ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS` (url=225ms, nekobox=263ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-89MS` (url=208ms, nekobox=250ms, status=yes)
10. `AKUN-010-BROADNNET-KR-VLESS-WS-118MS` (url=249ms, nekobox=286ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-129MS` (url=251ms, status=HTTP 204)
12. `AKUN-012-BROADNNET-KR-VLESS-WS-95MS` (url=232ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-146MS` (url=201ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-270MS` (url=569ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-279MS` (url=575ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-270MS` (url=587ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-290MS` (url=592ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-268MS` (url=577ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-277MS` (url=555ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-256MS` (url=562ms, status=HTTP 204)
21. `AKUN-029-VIDBOXCO-VLESS-WS-559MS` (url=721ms, status=HTTP 204)
22. `AKUN-032-UNKNOWN-VLESS-WS-542MS` (url=717ms, status=HTTP 204)
23. `AKUN-033-UNKNOWN-VLESS-WS-471MS` (url=822ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-743MS` (url=4561ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
