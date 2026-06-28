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
1. `AKUN-001-UNKNOWN-VLESS-WS-85MS` (url=206ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=217ms, nekobox=232ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=201ms, nekobox=226ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS` (url=211ms, nekobox=241ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-90MS` (url=240ms, nekobox=245ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-81MS` (url=245ms, nekobox=226ms, status=yes)
7. `AKUN-007-466688-VLESS-WS-115MS` (url=204ms, nekobox=257ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS` (url=229ms, nekobox=255ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-117MS` (url=216ms, nekobox=237ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-101MS` (url=221ms, nekobox=253ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-109MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-156MS` (url=198ms, status=HTTP 204)
14. `AKUN-015-CONFLU-VLESS-WS-241MS` (url=532ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-237MS` (url=496ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-269MS` (url=591ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-284MS` (url=577ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-267MS` (url=589ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-283MS` (url=570ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-289MS` (url=627ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-301MS` (url=556ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-261MS` (url=505ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-509MS` (url=846ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-503MS` (url=834ms, status=HTTP 204)
25. `AKUN-030-RC-PRO-5-VLESS-WS-507MS` (url=838ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
