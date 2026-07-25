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
1. `AKUN-001-UNKNOWN-VLESS-WS-57MS` (url=235ms, nekobox=271ms, status=yes)
2. `AKUN-002-GOOGLE-VLESS-WS-58MS` (url=219ms, nekobox=252ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-59MS` (url=236ms, nekobox=260ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-55MS` (url=218ms, nekobox=245ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-58MS` (url=219ms, nekobox=243ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-62MS` (url=219ms, nekobox=262ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-58MS` (url=219ms, nekobox=247ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-57MS` (url=231ms, nekobox=259ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-62MS` (url=238ms, nekobox=246ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-74MS` (url=218ms, nekobox=246ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-58MS` (url=234ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-95MS` (url=220ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-99MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-3666888-VLESS-WS-100MS` (url=228ms, status=HTTP 204)
15. `AKUN-015-LEVIKOGJGFDD-VLESS-WS-134MS` (url=277ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-67MS` (url=269ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-104MS` (url=240ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-158MS` (url=253ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-139MS` (url=289ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-54MS` (url=218ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-166MS` (url=258ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-102MS` (url=244ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-67MS` (url=263ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-134MS` (url=238ms, status=HTTP 204)
25. `AKUN-025-NET-141-11-202-0-23-VLESS-WS-333MS` (url=793ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
