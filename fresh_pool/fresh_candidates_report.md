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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-127MS` (url=276ms, nekobox=294ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-134MS` (url=265ms, nekobox=288ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-134MS` (url=277ms, nekobox=297ms, status=yes)
4. `AKUN-004-CCWU-VLESS-WS-131MS` (url=270ms, nekobox=305ms, status=yes)
5. `AKUN-005-DEV-VLESS-WS-136MS` (url=268ms, nekobox=310ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-129MS` (url=265ms, nekobox=279ms, status=yes)
7. `AKUN-007-SPEEDTEST-VLESS-WS-125MS` (url=266ms, nekobox=221ms, status=no)
8. `AKUN-007-DEV-VLESS-WS-134MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-126MS`
10. `AKUN-009-1PASSWORD-VLESS-WS-134MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-140MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-146MS` (url=275ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-142MS` (url=263ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-143MS` (url=290ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-144MS` (url=272ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-137MS` (url=297ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-135MS` (url=282ms, status=HTTP 204)
18. `AKUN-018-008500-VLESS-WS-126MS` (url=261ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-136MS` (url=291ms, status=HTTP 204)
20. `AKUN-020-SPEEDTEST-VLESS-WS-170MS` (url=236ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-138MS` (url=271ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-165MS` (url=291ms, status=HTTP 204)
23. `AKUN-023-MYBB-VLESS-WS-142MS` (url=268ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-148MS` (url=245ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-157MS` (url=281ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
