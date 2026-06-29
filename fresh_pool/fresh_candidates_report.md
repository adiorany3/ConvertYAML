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
1. `AKUN-001-466688-VLESS-WS-72MS` (url=250ms, nekobox=270ms, status=yes)
2. `AKUN-002-NETCRAFTERS-VLESS-WS-74MS` (url=247ms, nekobox=281ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS` (url=261ms, nekobox=187ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS`
5. `AKUN-004-COMPREND-NET-VLESS-WS-75MS`
6. `AKUN-005-466688-VLESS-WS-133MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-147MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-113MS` (url=251ms, nekobox=178ms, status=no)
10. `AKUN-008-ZVC-VLESS-WS-121MS`
11. `AKUN-009-DEV-VLESS-WS-187MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-262MS`
13. `AKUN-015-UNKNOWN-VLESS-WS-227MS` (url=1051ms, status=HTTP 204)
14. `AKUN-016-WPENG-VLESS-WS-306MS` (url=635ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-319MS` (url=618ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-248MS` (url=605ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-339MS` (url=610ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-345MS` (url=694ms, status=HTTP 204)
19. `AKUN-021-UK-GB-DCL-01-20191003-VLESS-WS-130MS` (url=254ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-389MS` (url=636ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-432MS` (url=547ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-428MS` (url=526ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-410MS` (url=737ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-494MS` (url=501ms, status=HTTP 204)
25. `AKUN-035-CLOUDFLARE-VLESS-WS-463MS` (url=1101ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
