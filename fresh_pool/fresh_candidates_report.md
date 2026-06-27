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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=210ms, nekobox=238ms, status=yes)
2. `AKUN-002-DE-XTOM-20210903-VLESS-WS-79MS` (url=219ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=218ms, nekobox=176ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-82MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-82MS` (url=207ms, nekobox=236ms, status=yes)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-77MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-90MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-87MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-105MS` (url=205ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS` (url=198ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-84MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-72MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-88MS` (url=206ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-135MS` (url=212ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-139MS` (url=206ms, status=HTTP 204)
19. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-66MS` (url=203ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-75MS` (url=220ms, status=HTTP 204)
21. `AKUN-021-COMPREND-NET-VLESS-WS-121MS` (url=220ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-230MS` (url=2634ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-250MS` (url=542ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-91MS` (url=215ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-234MS` (url=505ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
