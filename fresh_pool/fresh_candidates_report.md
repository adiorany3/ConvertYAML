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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-130MS` (url=268ms, nekobox=314ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-132MS` (url=253ms, nekobox=296ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-136MS` (url=269ms, nekobox=294ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-134MS` (url=274ms, nekobox=298ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-136MS` (url=271ms, nekobox=300ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-134MS` (url=260ms, nekobox=303ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-135MS` (url=260ms, nekobox=295ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-146MS` (url=271ms, nekobox=301ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-148MS` (url=270ms, nekobox=300ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-150MS` (url=259ms, nekobox=308ms, status=yes)
11. `AKUN-011-HETZNER-VLESS-WS-148MS` (url=299ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-151MS` (url=266ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-142MS` (url=268ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-162MS` (url=319ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-156MS` (url=281ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-146MS` (url=312ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-193MS` (url=325ms, status=HTTP 204)
18. `AKUN-018-HETZNER-VLESS-WS-176MS` (url=325ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-191MS` (url=328ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-183MS` (url=339ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-196MS` (url=381ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-222MS` (url=369ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-358MS` (url=1994ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-367MS` (url=2573ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-365MS` (url=1165ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
