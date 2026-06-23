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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=212ms, nekobox=242ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS` (url=228ms, nekobox=264ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS` (url=211ms, nekobox=232ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-79MS` (url=211ms, nekobox=260ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS` (url=230ms, nekobox=237ms, status=yes)
6. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-74MS` (url=213ms, nekobox=262ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=198ms, nekobox=244ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-117MS` (url=247ms, nekobox=274ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-125MS` (url=284ms, nekobox=245ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-180MS` (url=216ms, nekobox=247ms, status=yes)
11. `AKUN-011-BROADNNET-KR-VLESS-WS-181MS` (url=232ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-226MS` (url=509ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-269MS` (url=584ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-272MS` (url=493ms, status=HTTP 204)
15. `AKUN-015-SPEEDTEST-VLESS-WS-266MS` (url=576ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-292MS` (url=560ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-316MS` (url=566ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-256MS` (url=505ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-487MS` (url=851ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-470MS` (url=710ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-520MS` (url=670ms, status=HTTP 204)
22. `AKUN-027-WPENG-VLESS-WS-401MS` (url=947ms, status=HTTP 204)
23. `AKUN-028-UNKNOWN-VLESS-WS-720MS` (url=745ms, status=HTTP 204)
24. `AKUN-029-DEV-VLESS-WS-674MS` (url=1037ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-631MS` (url=2576ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
