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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-79MS` (url=235ms, nekobox=280ms, status=yes)
2. `AKUN-002-WPENG-VLESS-WS-71MS` (url=237ms, nekobox=250ms, status=yes)
3. `AKUN-003-ZOOM-VLESS-WS-83MS` (url=240ms, nekobox=279ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-107MS` (url=258ms, nekobox=182ms, status=no)
5. `AKUN-004-DEV-VLESS-WS-123MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-102MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-147MS`
9. `AKUN-008-ES-FORNEX-20160629-VLESS-WS-91MS`
10. `AKUN-009-DIGITALOCEAN-VLESS-WS-87MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-258MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-262MS` (url=542ms, status=HTTP 204)
13. `AKUN-014-DEV-VLESS-WS-292MS` (url=3766ms, status=HTTP 204)
14. `AKUN-015-DEV-VLESS-WS-306MS` (url=2476ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-127MS` (url=550ms, status=HTTP 204)
16. `AKUN-017-DEV-VLESS-WS-331MS` (url=2468ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-75MS` (url=240ms, status=HTTP 204)
18. `AKUN-019-DEV-VLESS-WS-337MS` (url=1476ms, status=HTTP 204)
19. `AKUN-020-DEV-VLESS-WS-330MS` (url=1347ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-257MS` (url=597ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-439MS` (url=548ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-416MS` (url=533ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-73MS` (url=229ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-408MS` (url=530ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-514MS` (url=1103ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
