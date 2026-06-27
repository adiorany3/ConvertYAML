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
1. `AKUN-001-UNKNOWN-VLESS-WS-135MS` (url=275ms, nekobox=287ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-148MS` (url=267ms, nekobox=300ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-148MS` (url=280ms, nekobox=323ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-146MS` (url=245ms, nekobox=313ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-141MS` (url=250ms, nekobox=333ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-144MS` (url=274ms, nekobox=297ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-141MS` (url=274ms, nekobox=305ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-162MS` (url=284ms, nekobox=316ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-148MS` (url=256ms, nekobox=331ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-162MS` (url=314ms, nekobox=351ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-161MS` (url=271ms, status=HTTP 204)
12. `AKUN-012-VULTR-VLESS-WS-151MS` (url=269ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-157MS` (url=280ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-144MS` (url=291ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-172MS` (url=275ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-165MS` (url=252ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-141MS` (url=297ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-147MS` (url=295ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-184MS` (url=276ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-217MS` (url=272ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-157MS` (url=324ms, status=HTTP 204)
22. `AKUN-022-CLOUDWEBMANAGE-EU-FR-VLESS-WS-165MS` (url=294ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-305MS` (url=501ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-350MS` (url=1581ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-357MS` (url=704ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
