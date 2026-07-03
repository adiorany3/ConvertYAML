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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-82MS` (url=225ms, nekobox=261ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=222ms, nekobox=250ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=227ms, nekobox=245ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=230ms, nekobox=249ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-87MS` (url=232ms, nekobox=230ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-87MS` (url=228ms, nekobox=258ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS` (url=229ms, nekobox=255ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-95MS` (url=227ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-83MS` (url=220ms, nekobox=251ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS` (url=227ms, nekobox=251ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-102MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-OVH-VLESS-WS-101MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-97MS` (url=230ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-102MS` (url=234ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-84MS` (url=211ms, status=HTTP 204)
16. `AKUN-016-WPENG-VLESS-WS-80MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-93MS` (url=226ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-88MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-ZVC-VLESS-WS-137MS` (url=229ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-126MS` (url=203ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-118MS` (url=220ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-93MS` (url=213ms, status=HTTP 204)
23. `AKUN-023-PAGES-VLESS-WS-131MS` (url=211ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-241MS` (url=516ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-257MS` (url=545ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
