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
1. `AKUN-001-OVH-VLESS-WS-137MS` (url=290ms, nekobox=279ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-130MS` (url=259ms, nekobox=295ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-142MS` (url=270ms, nekobox=305ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-143MS` (url=270ms, nekobox=287ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-145MS` (url=267ms, nekobox=284ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-143MS` (url=260ms, nekobox=288ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-138MS` (url=269ms, nekobox=289ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-153MS` (url=267ms, nekobox=288ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-132MS` (url=253ms, nekobox=283ms, status=yes)
10. `AKUN-010-LT-LRTC-20060503-VLESS-WS-215MS` (url=530ms, nekobox=546ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-176MS` (url=335ms, status=HTTP 204)
12. `AKUN-012-RMGYVPN-VLESS-WS-242MS` (url=502ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-169MS` (url=263ms, status=HTTP 204)
14. `AKUN-018-UNKNOWN-VLESS-WS-254MS` (url=402ms, status=HTTP 204)
15. `AKUN-019-CLOUDFLARE-VLESS-WS-580MS` (url=979ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-587MS` (url=1277ms, status=HTTP 204)
17. `AKUN-021-UNKNOWN-VLESS-WS-603MS` (url=928ms, status=HTTP 204)
18. `AKUN-022-CLOUDFLARE-VLESS-WS-588MS` (url=950ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-589MS` (url=965ms, status=HTTP 204)
20. `AKUN-024-HCAPTCHA-VLESS-WS-616MS` (url=819ms, status=HTTP 204)
21. `AKUN-026-UNKNOWN-VLESS-WS-729MS` (url=4606ms, status=HTTP 204)
22. `AKUN-030-UNKNOWN-VLESS-WS-637MS` (url=1247ms, status=HTTP 204)
23. `AKUN-031-UNKNOWN-VLESS-WS-809MS` (url=1190ms, status=HTTP 204)
24. `AKUN-032-CLOUDFLARE-VLESS-WS-778MS` (url=2252ms, status=HTTP 204)
25. `AKUN-033-CLOUDFLARE-VLESS-WS-839MS` (url=1681ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
