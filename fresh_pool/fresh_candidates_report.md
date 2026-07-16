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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=220ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-63MS` (url=210ms, nekobox=250ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=221ms, nekobox=256ms, status=yes)
4. `AKUN-004-GO-DADDY-COM-LLC-VLESS-WS-67MS` (url=229ms, nekobox=246ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS` (url=221ms, nekobox=238ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=216ms, nekobox=255ms, status=yes)
7. `AKUN-007-ORG-VLESS-WS-91MS` (url=207ms, nekobox=257ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=201ms, nekobox=289ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-97MS` (url=219ms, nekobox=241ms, status=yes)
10. `AKUN-010-466688-VLESS-WS-124MS` (url=226ms, nekobox=266ms, status=yes)
11. `AKUN-011-CZ-LOTUNA-19970206-VLESS-WS-107MS` (url=234ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-127MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-NEXUSMODS-VLESS-WS-94MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-139MS` (url=196ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-76MS` (url=207ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-134MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-123MS` (url=198ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-141MS` (url=208ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-179MS` (url=366ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-74MS` (url=202ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-373MS` (url=768ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-384MS` (url=816ms, status=HTTP 204)
23. `AKUN-024-RS-RAPIDSEEDBOX-20190717-VLESS-WS-352MS` (url=820ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-373MS` (url=761ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-100MS` (url=245ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
