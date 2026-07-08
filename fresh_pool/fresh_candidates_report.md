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
1. `AKUN-001-UNKNOWN-VLESS-WS-130MS` (url=272ms, nekobox=317ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-130MS` (url=289ms, nekobox=316ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-143MS` (url=377ms, nekobox=330ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-146MS` (url=296ms, nekobox=335ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-142MS` (url=392ms, nekobox=315ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-152MS` (url=296ms, nekobox=307ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-131MS` (url=345ms, nekobox=346ms, status=yes)
8. `AKUN-008-PUBLICDOMAINREGISTRY-NET-VLESS-WS-148MS` (url=324ms, nekobox=318ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-160MS` (url=291ms, nekobox=338ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-161MS` (url=280ms, nekobox=315ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-161MS` (url=316ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-174MS` (url=332ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-158MS` (url=296ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-176MS` (url=295ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-155MS` (url=369ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-160MS` (url=275ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-137MS` (url=295ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-169MS` (url=316ms, status=HTTP 204)
19. `AKUN-019-CONFLU-VLESS-WS-360MS` (url=809ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-370MS` (url=776ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-366MS` (url=739ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-398MS` (url=810ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-407MS` (url=834ms, status=HTTP 204)
24. `AKUN-032-CLOUDFLARE-VLESS-WS-701MS` (url=1050ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-669MS` (url=1164ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
