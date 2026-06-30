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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-118MS` (url=239ms, nekobox=275ms, status=yes)
2. `AKUN-002-NETCUP-VLESS-WS-118MS` (url=242ms, nekobox=281ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-123MS` (url=303ms, nekobox=331ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-117MS` (url=284ms, nekobox=278ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-124MS` (url=240ms, nekobox=267ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-126MS` (url=324ms, nekobox=327ms, status=yes)
7. `AKUN-007-466688-VLESS-WS-108MS` (url=248ms, nekobox=349ms, status=yes)
8. `AKUN-008-NET-NL-VLESS-WS-129MS` (url=301ms, nekobox=293ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-121MS` (url=239ms, nekobox=300ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-115MS` (url=287ms, nekobox=313ms, status=yes)
11. `AKUN-011-HOSTOFF-NET-VLESS-WS-121MS` (url=254ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-120MS` (url=243ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-126MS` (url=320ms, status=HTTP 204)
14. `AKUN-014-SPACECORE-VLESS-WS-139MS` (url=272ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-129MS` (url=281ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-115MS` (url=238ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-133MS` (url=252ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-142MS` (url=269ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-132MS` (url=255ms, status=HTTP 204)
20. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-126MS` (url=280ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-281MS` (url=687ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-317MS` (url=772ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-293MS` (url=614ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-298MS` (url=724ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-349MS` (url=695ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
