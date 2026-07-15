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
1. `AKUN-001-UNKNOWN-VLESS-WS-132MS` (url=299ms, nekobox=335ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-136MS` (url=274ms, nekobox=296ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-137MS` (url=266ms, nekobox=292ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-140MS` (url=281ms, nekobox=310ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-130MS` (url=270ms, nekobox=297ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-141MS` (url=309ms, nekobox=285ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-141MS` (url=265ms, nekobox=292ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-142MS` (url=266ms, nekobox=306ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-138MS` (url=267ms, nekobox=294ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-158MS` (url=380ms, nekobox=320ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-136MS` (url=278ms, status=HTTP 204)
12. `AKUN-012-DEV-VLESS-WS-156MS` (url=300ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-136MS` (url=280ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-148MS` (url=270ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-147MS` (url=277ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-148MS` (url=259ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-154MS` (url=283ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-155MS` (url=267ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-178MS` (url=335ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-136MS` (url=265ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-166MS` (url=293ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-175MS` (url=265ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-137MS` (url=285ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-136MS` (url=314ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-145MS` (url=303ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
