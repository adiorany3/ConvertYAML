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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-100MS` (url=234ms, nekobox=266ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-99MS` (url=231ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-108MS` (url=237ms, nekobox=301ms, status=yes)
4. `AKUN-004-GO-DADDY-COM-LLC-VLESS-WS-110MS` (url=216ms, nekobox=317ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-109MS` (url=234ms, nekobox=240ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-109MS` (url=229ms, nekobox=255ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-111MS` (url=228ms, nekobox=262ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-114MS` (url=243ms, nekobox=7177ms, status=no)
9. `AKUN-008-466688-VLESS-WS-90MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-115MS`
11. `AKUN-010-BGP48-HK-VLESS-WS-115MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-112MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-127MS` (url=235ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-117MS` (url=214ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-114MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-ADF-VLESS-WS-125MS` (url=211ms, status=HTTP 204)
17. `AKUN-017-MEDIUM-VLESS-WS-108MS` (url=222ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-131MS` (url=450ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-163MS` (url=349ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-153MS` (url=668ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-176MS` (url=289ms, status=HTTP 204)
22. `AKUN-022-UK-GB-DCL-01-20191003-VLESS-WS-153MS` (url=277ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-156MS` (url=280ms, status=HTTP 204)
24. `AKUN-024-WPENG-VLESS-WS-156MS` (url=228ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-107MS` (url=260ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
