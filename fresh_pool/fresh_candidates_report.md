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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=244ms, nekobox=266ms, status=yes)
2. `AKUN-002-ZOOM-VLESS-WS-89MS` (url=265ms, nekobox=267ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-90MS` (url=283ms, nekobox=300ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-92MS` (url=231ms, nekobox=274ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-76MS` (url=238ms, nekobox=279ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-88MS` (url=243ms, nekobox=293ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-95MS` (url=241ms, nekobox=261ms, status=yes)
8. `AKUN-008-WPENG-VLESS-WS-91MS` (url=333ms, nekobox=265ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS` (url=247ms, nekobox=265ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-93MS` (url=271ms, nekobox=292ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-111MS` (url=245ms, status=HTTP 204)
12. `AKUN-012-WEYRO-NET-VLESS-WS-124MS` (url=247ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-89MS` (url=251ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-106MS` (url=236ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-88MS` (url=267ms, status=HTTP 204)
16. `AKUN-016-ALIBABA-VLESS-WS-112MS` (url=278ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-144MS` (url=294ms, status=HTTP 204)
18. `AKUN-019-CONFLU-VLESS-WS-265MS` (url=575ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-286MS` (url=627ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-258MS` (url=570ms, status=HTTP 204)
21. `AKUN-022-MICROSOFT-VLESS-WS-291MS` (url=623ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-306MS` (url=637ms, status=HTTP 204)
23. `AKUN-024-LOCAL-VLESS-WS-301MS` (url=602ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-274MS` (url=559ms, status=HTTP 204)
25. `AKUN-027-QURAN-VLESS-WS-492MS` (url=816ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
