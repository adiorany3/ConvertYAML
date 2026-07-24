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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=227ms, nekobox=254ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-68MS` (url=226ms, nekobox=258ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-62MS` (url=248ms, nekobox=259ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS` (url=257ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=220ms, nekobox=271ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-64MS` (url=251ms, nekobox=261ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-80MS` (url=236ms, nekobox=262ms, status=yes)
8. `AKUN-008-DEV-VLESS-WS-94MS` (url=243ms, nekobox=261ms, status=yes)
9. `AKUN-009-008500-VLESS-WS-76MS` (url=229ms, nekobox=266ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-89MS` (url=233ms, nekobox=270ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-101MS` (url=236ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-108MS` (url=220ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-99MS` (url=254ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-94MS` (url=256ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-72MS` (url=222ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-112MS` (url=373ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-109MS` (url=274ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-70MS` (url=235ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-86MS` (url=219ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-124MS` (url=313ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-95MS` (url=250ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-127MS` (url=335ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-158MS` (url=313ms, status=HTTP 204)
24. `AKUN-025-ZVC-VLESS-WS-101MS` (url=256ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-130MS` (url=339ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
