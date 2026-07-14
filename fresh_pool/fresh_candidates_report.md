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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-86MS` (url=313ms, nekobox=353ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-95MS` (url=285ms, nekobox=317ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-94MS` (url=317ms, nekobox=327ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-114MS` (url=305ms, nekobox=379ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-109MS` (url=330ms, nekobox=318ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-116MS` (url=345ms, nekobox=391ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-112MS` (url=291ms, nekobox=326ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-109MS` (url=293ms, nekobox=363ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-117MS` (url=277ms, nekobox=318ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-134MS` (url=468ms, nekobox=322ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-112MS` (url=280ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-114MS` (url=310ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-133MS` (url=282ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-137MS` (url=256ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-138MS` (url=381ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-115MS` (url=321ms, status=HTTP 204)
17. `AKUN-017-US-VLESS-WS-129MS` (url=289ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-105MS` (url=316ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-138MS` (url=300ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-137MS` (url=344ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-120MS` (url=365ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-119MS` (url=297ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-169MS` (url=379ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-125MS` (url=347ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-244MS` (url=490ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
