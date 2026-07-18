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
1. `AKUN-001-9889888-VLESS-WS-62MS` (url=256ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=234ms, nekobox=259ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-76MS` (url=254ms, nekobox=272ms, status=yes)
4. `AKUN-004-ZOOM-VLESS-WS-81MS` (url=273ms, nekobox=256ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-79MS` (url=227ms, nekobox=268ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-89MS` (url=289ms, nekobox=276ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-88MS` (url=224ms, nekobox=262ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-81MS` (url=238ms, nekobox=270ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-98MS` (url=258ms, nekobox=284ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-80MS` (url=264ms, nekobox=334ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-74MS` (url=236ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-95MS` (url=261ms, status=HTTP 204)
13. `AKUN-013-ORG-VLESS-WS-83MS` (url=239ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-108MS` (url=294ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-100MS` (url=297ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-113MS` (url=239ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-115MS` (url=280ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-95MS` (url=227ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-117MS` (url=245ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-100MS` (url=262ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-86MS` (url=238ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-122MS` (url=319ms, status=HTTP 204)
23. `AKUN-023-WPENG-VLESS-WS-115MS` (url=288ms, status=HTTP 204)
24. `AKUN-024-CONFLU-VLESS-WS-245MS` (url=569ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-113MS` (url=239ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
