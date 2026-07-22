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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=218ms, nekobox=239ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-57MS` (url=256ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=216ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-63MS` (url=216ms, nekobox=244ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-64MS` (url=203ms, nekobox=245ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-62MS` (url=217ms, nekobox=248ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-65MS` (url=214ms, nekobox=242ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-62MS` (url=231ms, nekobox=247ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=221ms, nekobox=278ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-58MS` (url=226ms, nekobox=240ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-96MS` (url=221ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-60MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-96MS` (url=236ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-107MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-65MS` (url=215ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-90MS` (url=216ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-110MS` (url=265ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-158MS` (url=336ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-94MS` (url=223ms, status=HTTP 204)
20. `AKUN-021-ZVC-VLESS-WS-72MS` (url=209ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-194MS` (url=243ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-144MS` (url=351ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-334MS` (url=713ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-352MS` (url=721ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-333MS` (url=728ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
