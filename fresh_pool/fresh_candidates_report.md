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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-104MS` (url=270ms, nekobox=298ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-113MS` (url=285ms, nekobox=340ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-98MS` (url=301ms, nekobox=288ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-112MS` (url=260ms, nekobox=297ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-115MS` (url=321ms, nekobox=307ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-115MS` (url=254ms, nekobox=309ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-117MS` (url=256ms, nekobox=284ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-118MS` (url=322ms, nekobox=324ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-110MS` (url=253ms, nekobox=333ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-150MS` (url=253ms, nekobox=224ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-149MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-151MS` (url=317ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-150MS` (url=301ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-161MS` (url=245ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-151MS` (url=266ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-139MS` (url=330ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-165MS` (url=280ms, status=HTTP 204)
18. `AKUN-018-CONFLU-VLESS-WS-318MS` (url=698ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-322MS` (url=591ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-333MS` (url=628ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-327MS` (url=501ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-338MS` (url=760ms, status=HTTP 204)
23. `AKUN-023-WPENG-VLESS-WS-336MS` (url=689ms, status=HTTP 204)
24. `AKUN-024-RS-RAPIDSEEDBOX-20190717-VLESS-WS-356MS` (url=761ms, status=HTTP 204)
25. `AKUN-026-IRCYBERSEC-VLESS-WS-322MS` (url=790ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
