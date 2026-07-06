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
1. `AKUN-001-UNKNOWN-VLESS-WS-142MS` (url=279ms, nekobox=315ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-148MS` (url=302ms, nekobox=342ms, status=yes)
3. `AKUN-003-090227-VLESS-WS-137MS` (url=287ms, nekobox=302ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-142MS` (url=297ms, nekobox=307ms, status=yes)
5. `AKUN-005-WEBEX-VLESS-WS-152MS` (url=397ms, nekobox=313ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-159MS` (url=278ms, nekobox=330ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-131MS` (url=277ms, nekobox=322ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-150MS` (url=312ms, nekobox=338ms, status=yes)
9. `AKUN-009-466688-VLESS-WS-154MS` (url=289ms, nekobox=305ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-173MS` (url=330ms, nekobox=345ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-152MS` (url=280ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-150MS` (url=528ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-158MS` (url=263ms, status=HTTP 204)
14. `AKUN-014-WEBEX-VLESS-WS-151MS` (url=295ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-164MS` (url=325ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-176MS` (url=311ms, status=HTTP 204)
17. `AKUN-017-WEYRO-NET-VLESS-WS-204MS` (url=301ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-165MS` (url=296ms, status=HTTP 204)
19. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-381MS` (url=811ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-380MS` (url=552ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-387MS` (url=705ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-394MS` (url=781ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-399MS` (url=807ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-375MS` (url=714ms, status=HTTP 204)
25. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-392MS` (url=748ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
