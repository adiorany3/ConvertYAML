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
1. `AKUN-001-EDU-VLESS-WS-78MS` (url=288ms, nekobox=332ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-80MS` (url=338ms, nekobox=301ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-81MS` (url=308ms, nekobox=314ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS` (url=259ms, nekobox=322ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS` (url=311ms, nekobox=346ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-87MS` (url=275ms, nekobox=310ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-85MS` (url=288ms, nekobox=302ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-86MS` (url=260ms, nekobox=303ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-96MS` (url=295ms, nekobox=380ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-74MS` (url=271ms, nekobox=307ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-95MS` (url=292ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-88MS` (url=293ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-85MS` (url=377ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-84MS` (url=325ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-116MS` (url=272ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-115MS` (url=334ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-116MS` (url=360ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-125MS` (url=300ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-127MS` (url=318ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-124MS` (url=297ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-202MS` (url=375ms, status=HTTP 204)
22. `AKUN-023-SKK-VLESS-WS-269MS` (url=519ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-278MS` (url=582ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-307MS` (url=655ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-299MS` (url=633ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
