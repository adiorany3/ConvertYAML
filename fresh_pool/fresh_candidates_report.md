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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-106MS` (url=236ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-109MS` (url=224ms, nekobox=277ms, status=yes)
3. `AKUN-003-466688-VLESS-WS-121MS` (url=260ms, nekobox=279ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-102MS` (url=213ms, nekobox=271ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-106MS` (url=247ms, nekobox=255ms, status=yes)
6. `AKUN-006-OVH-VLESS-WS-104MS` (url=283ms, nekobox=255ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-126MS` (url=250ms, nekobox=300ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-127MS` (url=243ms, nekobox=269ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-117MS` (url=280ms, nekobox=265ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-103MS` (url=226ms, nekobox=255ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-115MS` (url=287ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-134MS` (url=239ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-128MS` (url=257ms, status=HTTP 204)
14. `AKUN-014-ZOOM-VLESS-WS-112MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-130MS` (url=282ms, status=HTTP 204)
16. `AKUN-016-MEDIUM-VLESS-WS-94MS` (url=233ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-152MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-125MS` (url=274ms, status=HTTP 204)
19. `AKUN-019-MYBB-VLESS-WS-120MS` (url=260ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-142MS` (url=271ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-111MS` (url=256ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-147MS` (url=311ms, status=HTTP 204)
23. `AKUN-023-NL-BRAINOZA-20250311-VLESS-WS-157MS` (url=232ms, status=HTTP 204)
24. `AKUN-024-1PASSWORD-VLESS-WS-112MS` (url=256ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-167MS` (url=259ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
