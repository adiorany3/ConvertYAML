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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=214ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=222ms, nekobox=260ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=227ms, nekobox=243ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-72MS` (url=214ms, nekobox=227ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=230ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=225ms, nekobox=257ms, status=yes)
7. `AKUN-007-VULTR-VLESS-WS-86MS` (url=218ms, nekobox=245ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=221ms, nekobox=259ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=212ms, nekobox=252ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS` (url=199ms, nekobox=251ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-97MS` (url=272ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-72MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-75MS` (url=229ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-97MS` (url=214ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-74MS` (url=213ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-78MS` (url=203ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-84MS` (url=226ms, status=HTTP 204)
18. `AKUN-019-GOOGLE-VLESS-WS-83MS` (url=200ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-83MS` (url=211ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-88MS` (url=201ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-111MS` (url=207ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-336MS` (url=723ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-83MS` (url=201ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-346MS` (url=788ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-391MS` (url=808ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
