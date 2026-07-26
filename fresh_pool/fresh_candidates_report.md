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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-54MS` (url=219ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-54MS` (url=214ms, nekobox=244ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-56MS` (url=217ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-57MS` (url=214ms, nekobox=235ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-59MS` (url=212ms, nekobox=234ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-71MS` (url=211ms, nekobox=235ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-71MS` (url=199ms, nekobox=236ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS` (url=216ms, nekobox=248ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS` (url=3627ms, nekobox=236ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-95MS` (url=208ms, nekobox=236ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-62MS` (url=221ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-66MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-89MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-119MS` (url=271ms, status=HTTP 204)
15. `AKUN-015-GOOGLE-VLESS-WS-60MS` (url=226ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-90MS` (url=208ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-94MS` (url=212ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-115MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-147MS` (url=209ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-330MS` (url=556ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-342MS` (url=745ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-366MS` (url=597ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-640MS` (url=1051ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-664MS` (url=1022ms, status=HTTP 204)
25. `AKUN-026-SPEEDTEST-VLESS-WS-773MS` (url=1483ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
