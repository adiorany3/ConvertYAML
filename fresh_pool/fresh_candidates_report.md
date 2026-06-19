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
1. `AKUN-001-UNKNOWN-VLESS-WS-121MS` (url=276ms, nekobox=288ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-139MS` (url=252ms, nekobox=313ms, status=yes)
3. `AKUN-003-EGN-22-VLESS-WS-148MS` (url=310ms, nekobox=289ms, status=yes)
4. `AKUN-004-U1HOST-FRA-VLESS-WS-147MS` (url=270ms, nekobox=296ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-147MS` (url=298ms, nekobox=307ms, status=yes)
6. `AKUN-006-HOSTOFF-NET-VLESS-WS-139MS` (url=250ms, nekobox=305ms, status=yes)
7. `AKUN-007-SPACECORE-VLESS-WS-145MS` (url=280ms, nekobox=313ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-141MS` (url=297ms, nekobox=329ms, status=yes)
9. `AKUN-009-MEDIUM-VLESS-WS-132MS` (url=251ms, nekobox=312ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-155MS` (url=256ms, nekobox=316ms, status=yes)
11. `AKUN-011-1PASSWORD-VLESS-WS-137MS` (url=242ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-172MS` (url=278ms, status=HTTP 204)
13. `AKUN-013-NET-NL-VLESS-WS-146MS` (url=251ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-146MS` (url=331ms, status=HTTP 204)
15. `AKUN-015-NETCUP-VLESS-WS-150MS` (url=257ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-155MS` (url=272ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-190MS` (url=275ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-150MS` (url=268ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-145MS` (url=262ms, status=HTTP 204)
20. `AKUN-020-CLOUDWEBMANAGE-EU-FR-VLESS-WS-140MS` (url=317ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-145MS` (url=299ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-138MS` (url=247ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-395MS` (url=754ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-400MS` (url=4567ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-386MS` (url=809ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
