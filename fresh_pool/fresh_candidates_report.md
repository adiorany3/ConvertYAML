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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-87MS` (url=324ms, nekobox=329ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-90MS` (url=309ms, nekobox=348ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-98MS` (url=299ms, nekobox=390ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-106MS` (url=352ms, nekobox=298ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-118MS` (url=294ms, nekobox=819ms, status=yes)
6. `AKUN-006-SAVVY-7-VLESS-WS-118MS` (url=349ms, nekobox=325ms, status=yes)
7. `AKUN-007-466688-VLESS-WS-126MS` (url=359ms, nekobox=379ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-121MS` (url=371ms, nekobox=320ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-117MS` (url=349ms, nekobox=418ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS` (url=350ms, nekobox=345ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-105MS` (url=273ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-107MS` (url=371ms, status=HTTP 204)
13. `AKUN-013-AIMALL-VLESS-WS-101MS` (url=324ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-125MS` (url=310ms, status=HTTP 204)
15. `AKUN-015-DE5-VLESS-WS-135MS` (url=397ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-111MS` (url=299ms, status=HTTP 204)
17. `AKUN-017-UK-GB-DCL-01-20191003-VLESS-WS-116MS` (url=321ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-161MS` (url=345ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-139MS` (url=373ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-149MS` (url=410ms, status=HTTP 204)
21. `AKUN-022-WPENG-VLESS-WS-120MS` (url=443ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-322MS` (url=663ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-343MS` (url=651ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-321MS` (url=3051ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-370MS` (url=652ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
