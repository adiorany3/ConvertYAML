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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=211ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=217ms, nekobox=176ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS`
5. `AKUN-004-WPENG-VLESS-WS-83MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-64MS`
7. `AKUN-006-COMPREND-NET-VLESS-WS-75MS`
8. `AKUN-007-DIGITALOCEAN-VLESS-WS-83MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS`
10. `AKUN-009-WPENG-VLESS-WS-85MS`
11. `AKUN-010-COMPREND-NET-VLESS-WS-90MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-74MS` (url=212ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-68MS` (url=198ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-74MS` (url=206ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-117MS` (url=219ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-130MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-100MS` (url=223ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-112MS` (url=198ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-78MS` (url=205ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-161MS` (url=210ms, status=HTTP 204)
21. `AKUN-021-ADF-VLESS-WS-127MS` (url=217ms, status=HTTP 204)
22. `AKUN-022-MYBB-VLESS-WS-73MS` (url=228ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-104MS` (url=218ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-230MS` (url=494ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-234MS` (url=527ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
