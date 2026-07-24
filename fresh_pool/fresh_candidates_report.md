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
1. `AKUN-001-UNKNOWN-VLESS-WS-127MS` (url=256ms, nekobox=293ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-129MS` (url=268ms, nekobox=297ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-124MS` (url=263ms, nekobox=284ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-131MS` (url=257ms, nekobox=289ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-129MS` (url=268ms, nekobox=286ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-140MS` (url=285ms, nekobox=307ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-147MS` (url=261ms, nekobox=290ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-154MS` (url=323ms, nekobox=291ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-136MS` (url=310ms, nekobox=315ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-164MS` (url=265ms, nekobox=288ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-134MS` (url=262ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-142MS` (url=254ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-199MS` (url=336ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-141MS` (url=266ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-176MS` (url=398ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-152MS` (url=331ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-161MS` (url=347ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-222MS` (url=378ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-191MS` (url=384ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-186MS` (url=354ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-139MS` (url=276ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-241MS` (url=386ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-356MS` (url=735ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-350MS` (url=762ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-364MS` (url=739ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
