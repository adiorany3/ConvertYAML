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
1. `AKUN-001-UNKNOWN-VLESS-WS-58MS` (url=220ms, nekobox=264ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=230ms, nekobox=247ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-68MS` (url=216ms, nekobox=247ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-70MS` (url=218ms, nekobox=253ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=213ms, nekobox=257ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-58MS` (url=230ms, nekobox=253ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-92MS` (url=243ms, nekobox=238ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS` (url=203ms, nekobox=254ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-69MS` (url=265ms, nekobox=272ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-116MS` (url=224ms, nekobox=247ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-55MS` (url=221ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-97MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-114MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-114MS` (url=253ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-86MS` (url=241ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-110MS` (url=227ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-114MS` (url=222ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-75MS` (url=221ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-122MS` (url=246ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-64MS` (url=218ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-105MS` (url=209ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-108MS` (url=235ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-188MS` (url=255ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-71MS` (url=220ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-340MS` (url=734ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
