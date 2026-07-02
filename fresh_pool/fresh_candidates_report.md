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
1. `AKUN-001-COMPREND-NET-VLESS-WS-157MS` (url=310ms, nekobox=305ms, status=yes)
2. `AKUN-002-WPENG-VLESS-WS-162MS` (url=355ms, nekobox=323ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-165MS` (url=313ms, nekobox=376ms, status=yes)
4. `AKUN-004-DIGITALOCEAN-VLESS-WS-143MS` (url=317ms, nekobox=354ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-166MS` (url=289ms, nekobox=345ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-169MS` (url=279ms, nekobox=314ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-152MS` (url=282ms, nekobox=305ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-153MS` (url=276ms, nekobox=356ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-143MS` (url=342ms, nekobox=364ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-181MS` (url=249ms, nekobox=310ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-177MS` (url=312ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-168MS` (url=296ms, status=HTTP 204)
13. `AKUN-013-ALIBABA-VLESS-WS-168MS` (url=297ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-164MS` (url=266ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-197MS` (url=308ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-169MS` (url=299ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-167MS` (url=272ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-196MS` (url=327ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-140MS` (url=282ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-355MS` (url=713ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-305MS` (url=508ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-363MS` (url=698ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-378MS` (url=740ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-367MS` (url=690ms, status=HTTP 204)
25. `AKUN-026-WPENG-VLESS-WS-401MS` (url=764ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
