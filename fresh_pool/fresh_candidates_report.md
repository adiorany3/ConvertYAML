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
1. `AKUN-001-UNKNOWN-VLESS-WS-133MS` (url=265ms, nekobox=300ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-134MS` (url=252ms, nekobox=314ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-138MS` (url=266ms, nekobox=292ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-142MS` (url=263ms, nekobox=297ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-136MS` (url=261ms, nekobox=287ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-138MS` (url=267ms, nekobox=290ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-144MS` (url=271ms, nekobox=299ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-147MS` (url=263ms, nekobox=293ms, status=yes)
9. `AKUN-009-DEV-VLESS-WS-136MS` (url=265ms, nekobox=321ms, status=yes)
10. `AKUN-010-CCWU-VLESS-WS-138MS` (url=261ms, nekobox=292ms, status=yes)
11. `AKUN-011-PAGES-VLESS-WS-155MS` (url=290ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-146MS` (url=260ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-149MS` (url=277ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-139MS` (url=271ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-165MS` (url=282ms, status=HTTP 204)
16. `AKUN-016-WEBEX-VLESS-WS-166MS` (url=297ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-135MS` (url=277ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-167MS` (url=302ms, status=HTTP 204)
19. `AKUN-019-ZVC-VLESS-WS-175MS` (url=292ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-147MS` (url=275ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-217MS` (url=398ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-143MS` (url=274ms, status=HTTP 204)
23. `AKUN-023-ZVC-VLESS-WS-147MS` (url=294ms, status=HTTP 204)
24. `AKUN-024-DEV-VLESS-WS-146MS` (url=274ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-158MS` (url=279ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
