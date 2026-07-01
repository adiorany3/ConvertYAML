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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-99MS` (url=253ms, nekobox=273ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-94MS` (url=245ms, nekobox=261ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-111MS` (url=257ms, nekobox=280ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-111MS` (url=240ms, nekobox=271ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-98MS` (url=234ms, nekobox=262ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-114MS` (url=267ms, nekobox=281ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-112MS` (url=236ms, nekobox=253ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-111MS` (url=225ms, nekobox=256ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-120MS` (url=238ms, nekobox=256ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-126MS` (url=276ms, nekobox=257ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-129MS` (url=216ms, status=HTTP 204)
12. `AKUN-012-WEYRO-NET-VLESS-WS-118MS` (url=255ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=220ms, status=HTTP 204)
14. `AKUN-014-ZOOM-VLESS-WS-114MS` (url=257ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-100MS` (url=264ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-318MS` (url=643ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-106MS` (url=240ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-346MS` (url=734ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-375MS` (url=750ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-353MS` (url=704ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-391MS` (url=747ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-372MS` (url=719ms, status=HTTP 204)
23. `AKUN-024-DEV-VLESS-WS-112MS` (url=234ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-107MS` (url=235ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-347MS` (url=649ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
