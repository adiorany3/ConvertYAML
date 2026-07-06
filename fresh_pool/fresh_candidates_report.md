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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=202ms, nekobox=230ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=210ms, nekobox=229ms, status=yes)
3. `AKUN-003-OVH-VLESS-WS-81MS` (url=207ms, nekobox=236ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=203ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=229ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-74MS` (url=210ms, nekobox=233ms, status=yes)
7. `AKUN-007-HETZNER-VLESS-WS-89MS` (url=220ms, nekobox=240ms, status=yes)
8. `AKUN-008-WEYRO-NET-VLESS-WS-82MS` (url=209ms, nekobox=233ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=225ms, nekobox=253ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS` (url=217ms, nekobox=199ms, status=no)
11. `AKUN-010-WPENG-VLESS-WS-75MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-73MS` (url=220ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-85MS` (url=308ms, status=HTTP 204)
14. `AKUN-014-008500-VLESS-WS-117MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-72MS` (url=212ms, status=HTTP 204)
16. `AKUN-016-PAGES-VLESS-WS-100MS` (url=279ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-145MS` (url=232ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-147MS` (url=227ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-98MS` (url=214ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-79MS` (url=223ms, status=HTTP 204)
21. `AKUN-021-MYBB-VLESS-WS-71MS` (url=219ms, status=HTTP 204)
22. `AKUN-022-1PASSWORD-VLESS-WS-73MS` (url=207ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-229MS` (url=503ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-248MS` (url=565ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-234MS` (url=481ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
