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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=230ms, nekobox=261ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-72MS` (url=222ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-85MS` (url=211ms, nekobox=263ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-78MS` (url=218ms, nekobox=230ms, status=yes)
5. `AKUN-005-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-91MS` (url=226ms, nekobox=236ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-101MS` (url=229ms, nekobox=243ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS` (url=232ms, nekobox=188ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-102MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-105MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-90MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-109MS` (url=203ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-132MS` (url=471ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-87MS` (url=229ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-147MS` (url=232ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-180MS` (url=281ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-79MS` (url=228ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-169MS` (url=467ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-333MS` (url=738ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-417MS` (url=668ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-516MS` (url=933ms, status=HTTP 204)
22. `AKUN-028-CLOUDFLARE-VLESS-WS-424MS` (url=4490ms, status=HTTP 204)
23. `AKUN-030-UNKNOWN-VLESS-WS-601MS` (url=2111ms, status=HTTP 204)
24. `AKUN-031-UNKNOWN-VLESS-WS-407MS` (url=733ms, status=HTTP 204)
25. `AKUN-033-CLOUDFLARE-VLESS-WS-185MS` (url=260ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
