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
1. `AKUN-001-UNKNOWN-VLESS-WS-56MS` (url=227ms, nekobox=261ms, status=yes)
2. `AKUN-002-008500-VLESS-WS-56MS` (url=238ms, nekobox=266ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-55MS` (url=217ms, nekobox=246ms, status=yes)
4. `AKUN-004-VULTR-VLESS-WS-57MS` (url=218ms, nekobox=267ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-58MS` (url=247ms, nekobox=257ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-58MS` (url=222ms, nekobox=253ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-60MS` (url=224ms, nekobox=242ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-57MS` (url=239ms, nekobox=250ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-72MS` (url=218ms, nekobox=248ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-97MS` (url=219ms, nekobox=249ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-73MS` (url=238ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-89MS` (url=220ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-119MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-AMAZON-VLESS-WS-88MS` (url=242ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-106MS` (url=227ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-81MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-LEVIKOGJGFDD-VLESS-WS-132MS` (url=259ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-73MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-84MS` (url=221ms, status=HTTP 204)
20. `AKUN-020-LT-LRTC-20060503-VLESS-WS-359MS` (url=852ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-357MS` (url=2166ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-326MS` (url=749ms, status=HTTP 204)
23. `AKUN-023-ZVC-VLESS-WS-58MS` (url=245ms, status=HTTP 204)
24. `AKUN-024-NET-141-11-202-0-23-VLESS-WS-498MS` (url=899ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-602MS` (url=1050ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
