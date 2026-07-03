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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=233ms, nekobox=260ms, status=yes)
2. `AKUN-002-WPENG-VLESS-WS-78MS` (url=206ms, nekobox=260ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-75MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS`
5. `AKUN-005-WEYRO-NET-VLESS-WS-78MS`
6. `AKUN-006-WPENG-VLESS-WS-106MS`
7. `AKUN-007-COMPREND-NET-VLESS-WS-100MS`
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-79MS`
9. `AKUN-009-ZOOM-VLESS-WS-88MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-104MS`
11. `AKUN-012-COMPREND-NET-VLESS-WS-104MS` (url=206ms, status=HTTP 204)
12. `AKUN-013-COMPREND-NET-VLESS-WS-87MS` (url=225ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-118MS` (url=226ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-95MS` (url=217ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-134MS` (url=205ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-145MS` (url=223ms, status=HTTP 204)
17. `AKUN-018-COMPREND-NET-VLESS-WS-81MS` (url=229ms, status=HTTP 204)
18. `AKUN-019-COMPREND-NET-VLESS-WS-138MS` (url=221ms, status=HTTP 204)
19. `AKUN-020-COMPREND-NET-VLESS-WS-103MS` (url=218ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-96MS` (url=280ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-329MS` (url=572ms, status=HTTP 204)
22. `AKUN-023-CONFLU-VLESS-WS-351MS` (url=759ms, status=HTTP 204)
23. `AKUN-024-WPENG-VLESS-WS-380MS` (url=809ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-370MS` (url=735ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-380MS` (url=911ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
