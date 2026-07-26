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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-57MS` (url=198ms, nekobox=223ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-57MS` (url=198ms, nekobox=228ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-60MS` (url=212ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS` (url=301ms, nekobox=253ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS` (url=207ms, nekobox=223ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS` (url=211ms, nekobox=243ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-58MS` (url=201ms, nekobox=226ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-64MS` (url=214ms, nekobox=238ms, status=yes)
9. `AKUN-009-DEV-VLESS-WS-77MS` (url=216ms, nekobox=238ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-69MS` (url=201ms, nekobox=230ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-79MS` (url=228ms, status=HTTP 204)
12. `AKUN-012-DEV-VLESS-WS-68MS` (url=206ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-95MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-94MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-77MS` (url=203ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-93MS` (url=228ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-107MS` (url=215ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-203MS` (url=731ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-233MS` (url=477ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-236MS` (url=1533ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-91MS` (url=203ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-398MS` (url=669ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-401MS` (url=1137ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-438MS` (url=468ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-422MS` (url=1182ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
