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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-133MS` (url=277ms, nekobox=329ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-143MS` (url=269ms, nekobox=323ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-148MS` (url=293ms, nekobox=353ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-152MS` (url=269ms, nekobox=336ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-149MS` (url=277ms, nekobox=325ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-141MS` (url=331ms, nekobox=325ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-137MS` (url=265ms, nekobox=324ms, status=yes)
8. `AKUN-008-WPENG-VLESS-WS-160MS` (url=332ms, nekobox=352ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-161MS` (url=320ms, nekobox=396ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-150MS` (url=305ms, nekobox=322ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-167MS` (url=345ms, status=HTTP 204)
12. `AKUN-012-WPENG-VLESS-WS-163MS` (url=328ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-173MS` (url=303ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-159MS` (url=315ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-182MS` (url=354ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-173MS` (url=381ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-179MS` (url=327ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-186MS` (url=330ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-366MS` (url=746ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-375MS` (url=725ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-401MS` (url=814ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-344MS` (url=476ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-411MS` (url=816ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-397MS` (url=795ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-681MS` (url=1139ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
