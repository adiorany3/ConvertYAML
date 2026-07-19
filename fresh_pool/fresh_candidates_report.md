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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-88MS` (url=275ms, nekobox=307ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-87MS` (url=275ms, nekobox=305ms, status=yes)
3. `AKUN-003-DIXONS-VLESS-WS-107MS` (url=369ms, nekobox=335ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-113MS` (url=289ms, nekobox=329ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-114MS` (url=302ms, nekobox=324ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-121MS` (url=305ms, nekobox=345ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-122MS` (url=303ms, nekobox=7168ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS`
9. `AKUN-008-466688-VLESS-WS-99MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-129MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-129MS` (url=310ms, nekobox=335ms, status=yes)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-107MS` (url=322ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-108MS` (url=287ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-140MS` (url=342ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-146MS` (url=350ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-147MS` (url=337ms, status=HTTP 204)
17. `AKUN-017-UK-GB-DCL-01-20191003-VLESS-WS-124MS` (url=343ms, status=HTTP 204)
18. `AKUN-018-UK-GB-DCL-01-20191003-VLESS-WS-143MS` (url=370ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-168MS` (url=288ms, status=HTTP 204)
20. `AKUN-020-UK-GB-DCL-01-20191003-VLESS-WS-155MS` (url=368ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-169MS` (url=314ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-147MS` (url=340ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-129MS` (url=277ms, status=HTTP 204)
24. `AKUN-024-WEBEX-VLESS-WS-160MS` (url=317ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-149MS` (url=292ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
