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
1. `AKUN-001-UNKNOWN-VLESS-WS-75MS` (url=236ms, nekobox=270ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-82MS` (url=248ms, nekobox=283ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS` (url=323ms, nekobox=276ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=235ms, nekobox=272ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-89MS` (url=256ms, nekobox=303ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS` (url=253ms, nekobox=267ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-109MS` (url=246ms, nekobox=281ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-110MS` (url=300ms, nekobox=300ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-97MS` (url=250ms, nekobox=268ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-85MS` (url=247ms, nekobox=276ms, status=yes)
11. `AKUN-011-ADF-VLESS-WS-121MS` (url=272ms, status=HTTP 204)
12. `AKUN-012-DIGITALOCEAN-VLESS-WS-116MS` (url=255ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-110MS` (url=248ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-87MS` (url=280ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-289MS` (url=620ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-111MS` (url=270ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-309MS` (url=650ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-89MS` (url=243ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-265MS` (url=1852ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-85MS` (url=260ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-404MS` (url=723ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-340MS` (url=585ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-328MS` (url=646ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-384MS` (url=496ms, status=HTTP 204)
25. `AKUN-027-IETF-VLESS-WS-543MS` (url=875ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
