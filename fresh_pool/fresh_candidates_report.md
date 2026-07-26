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
1. `AKUN-001-UNKNOWN-VLESS-WS-124MS` (url=263ms, nekobox=290ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-126MS` (url=247ms, nekobox=290ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-127MS` (url=249ms, nekobox=291ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-125MS` (url=256ms, nekobox=280ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-131MS` (url=249ms, nekobox=289ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-131MS` (url=259ms, nekobox=300ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-134MS` (url=249ms, nekobox=297ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-136MS` (url=257ms, nekobox=289ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-141MS` (url=272ms, nekobox=305ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-142MS` (url=299ms, nekobox=289ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-132MS` (url=249ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-133MS` (url=269ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-173MS` (url=378ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-186MS` (url=345ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-171MS` (url=309ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-172MS` (url=310ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-182MS` (url=339ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-210MS` (url=323ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-208MS` (url=466ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-125MS` (url=247ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-345MS` (url=5083ms, status=HTTP 204)
22. `AKUN-024-ZVC-VLESS-WS-134MS` (url=295ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-303MS` (url=589ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-469MS` (url=1636ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-654MS` (url=1076ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
