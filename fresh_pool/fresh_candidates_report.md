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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-104MS` (url=289ms, nekobox=316ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-104MS` (url=316ms, nekobox=311ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-109MS` (url=391ms, nekobox=305ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-113MS` (url=295ms, nekobox=337ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-109MS` (url=323ms, nekobox=355ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-124MS` (url=303ms, nekobox=333ms, status=yes)
7. `AKUN-007-FMN5-RENTED-NET2-VLESS-WS-127MS` (url=301ms, nekobox=334ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-120MS` (url=263ms, nekobox=309ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-106MS` (url=300ms, nekobox=330ms, status=yes)
10. `AKUN-010-WPENG-VLESS-WS-128MS` (url=285ms, nekobox=339ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-144MS` (url=311ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-138MS` (url=1252ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-126MS` (url=311ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-139MS` (url=305ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-148MS` (url=331ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-110MS` (url=294ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-173MS` (url=328ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-193MS` (url=280ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-147MS` (url=319ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-154MS` (url=332ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-242MS` (url=464ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-309MS` (url=681ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-313MS` (url=687ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-126MS` (url=318ms, status=HTTP 204)
25. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-325MS` (url=618ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
