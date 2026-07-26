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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-79MS` (url=309ms, nekobox=346ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=374ms, nekobox=310ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS` (url=323ms, nekobox=303ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-90MS` (url=291ms, nekobox=394ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=368ms, nekobox=334ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-92MS` (url=341ms, nekobox=353ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS` (url=295ms, nekobox=371ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-81MS` (url=398ms, nekobox=303ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-119MS` (url=391ms, nekobox=361ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-132MS` (url=286ms, nekobox=360ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-124MS` (url=318ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-106MS` (url=312ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-124MS` (url=294ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-105MS` (url=311ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-92MS` (url=275ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-144MS` (url=397ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-188MS` (url=399ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-162MS` (url=470ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-180MS` (url=400ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-201MS` (url=405ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-159MS` (url=474ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-337MS` (url=3232ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-313MS` (url=2765ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-448MS` (url=852ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-495MS` (url=911ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
