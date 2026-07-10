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
1. `AKUN-001-UNKNOWN-VLESS-WS-62MS` (url=210ms, nekobox=240ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=218ms, nekobox=247ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=225ms, nekobox=255ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-80MS` (url=202ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS` (url=227ms, nekobox=246ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=203ms, nekobox=254ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-80MS` (url=218ms, nekobox=271ms, status=yes)
8. `AKUN-008-NODEJS-VLESS-WS-83MS` (url=214ms, nekobox=183ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-75MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS`
11. `AKUN-010-DEV-VLESS-WS-90MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-100MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-94MS` (url=221ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-101MS` (url=217ms, status=HTTP 204)
15. `AKUN-015-DIGITALOCEAN-VLESS-WS-73MS` (url=228ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-82MS` (url=196ms, status=HTTP 204)
17. `AKUN-017-ES-FORNEX-20160629-VLESS-WS-119MS` (url=219ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-72MS` (url=312ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-82MS` (url=204ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-70MS` (url=679ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-206MS` (url=338ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-236MS` (url=522ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-126MS` (url=381ms, status=HTTP 204)
24. `AKUN-024-DEV-VLESS-WS-271MS` (url=1368ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-353MS` (url=785ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
