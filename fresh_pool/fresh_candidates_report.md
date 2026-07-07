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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=221ms, nekobox=246ms, status=yes)
2. `AKUN-002-ORACLE-VLESS-WS-60MS` (url=205ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS` (url=218ms, nekobox=252ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-73MS` (url=229ms, nekobox=245ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-69MS` (url=231ms, nekobox=178ms, status=no)
6. `AKUN-005-CHSL-HEL-VLESS-WS-71MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-67MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-72MS`
9. `AKUN-008-WPENG-VLESS-WS-80MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-65MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-70MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-73MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-97MS` (url=251ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-99MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-131MS` (url=226ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-91MS` (url=233ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-123MS` (url=229ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-137MS` (url=209ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-77MS` (url=237ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-355MS` (url=737ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-375MS` (url=1346ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-380MS` (url=832ms, status=HTTP 204)
23. `AKUN-023-SPEEDTEST-VLESS-WS-366MS` (url=802ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-371MS` (url=847ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-364MS` (url=765ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
