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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=225ms, nekobox=244ms, status=yes)
2. `AKUN-002-COMPREND-NET-VLESS-WS-78MS` (url=227ms, nekobox=263ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-80MS` (url=211ms, nekobox=232ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-65MS` (url=212ms, nekobox=245ms, status=yes)
5. `AKUN-005-MEDIUM-VLESS-WS-83MS` (url=236ms, nekobox=282ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS` (url=201ms, nekobox=254ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-80MS` (url=242ms, nekobox=232ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-121MS` (url=211ms, nekobox=262ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS` (url=251ms, nekobox=292ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS` (url=216ms, nekobox=243ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=219ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-85MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-65MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-79MS` (url=243ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-91MS` (url=219ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-85MS` (url=235ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-196MS` (url=206ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-56MS` (url=220ms, status=HTTP 204)
19. `AKUN-019-US-VLESS-WS-90MS` (url=258ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-350MS` (url=740ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-349MS` (url=728ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-387MS` (url=845ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-403MS` (url=838ms, status=HTTP 204)
24. `AKUN-024-MICROSOFT-VLESS-WS-394MS` (url=823ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-75MS` (url=217ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
