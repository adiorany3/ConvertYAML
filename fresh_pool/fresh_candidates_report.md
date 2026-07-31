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
1. `AKUN-001-DEV-VLESS-WS-126MS` (url=253ms, nekobox=291ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-130MS` (url=260ms, nekobox=292ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-125MS` (url=276ms, nekobox=296ms, status=yes)
4. `AKUN-004-CCWU-VLESS-WS-128MS` (url=264ms, nekobox=288ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-130MS` (url=242ms, nekobox=258ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-124MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-131MS`
8. `AKUN-007-DEV-VLESS-WS-133MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-138MS` (url=264ms, nekobox=7176ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-140MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-149MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-143MS`
13. `AKUN-013-NET-USA-VLESS-WS-137MS` (url=275ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-144MS` (url=284ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-129MS` (url=273ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-135MS` (url=259ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-137MS` (url=284ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-138MS` (url=268ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-141MS` (url=269ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-174MS` (url=301ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-180MS` (url=268ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-205MS` (url=339ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-210MS` (url=235ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-197MS` (url=248ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-143MS` (url=287ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
