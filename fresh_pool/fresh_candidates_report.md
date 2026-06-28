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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-132MS` (url=271ms, nekobox=300ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-134MS` (url=275ms, nekobox=308ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-133MS` (url=273ms, nekobox=306ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-137MS` (url=264ms, nekobox=300ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-157MS` (url=296ms, nekobox=301ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-162MS` (url=274ms, nekobox=290ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-184MS` (url=269ms, nekobox=297ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-140MS` (url=292ms, nekobox=325ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-150MS` (url=300ms, nekobox=284ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-167MS` (url=265ms, nekobox=298ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-145MS` (url=276ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-156MS` (url=268ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-144MS` (url=283ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-141MS` (url=245ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-346MS` (url=949ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-354MS` (url=693ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-385MS` (url=750ms, status=HTTP 204)
18. `AKUN-018-WPENG-VLESS-WS-387MS` (url=760ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-384MS` (url=764ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-375MS` (url=762ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-412MS` (url=780ms, status=HTTP 204)
22. `AKUN-022-BIGCOMMERCE-VLESS-WS-632MS` (url=1059ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-396MS` (url=1078ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-655MS` (url=1037ms, status=HTTP 204)
25. `AKUN-027-VIDBOXCO-VLESS-WS-649MS` (url=933ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
