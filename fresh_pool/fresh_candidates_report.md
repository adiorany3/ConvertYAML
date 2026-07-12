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
1. `AKUN-001-UNKNOWN-VLESS-WS-90MS` (url=231ms, nekobox=233ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-100MS` (url=229ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-100MS` (url=235ms, nekobox=254ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-100MS` (url=210ms, nekobox=229ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=200ms, nekobox=236ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS` (url=210ms, nekobox=279ms, status=yes)
7. `AKUN-007-ZOOM-VLESS-WS-88MS` (url=210ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=211ms, nekobox=199ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-98MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-99MS`
11. `AKUN-010-IDC-SG-VLESS-WS-117MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-119MS` (url=226ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-114MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-116MS` (url=209ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-132MS` (url=203ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-159MS` (url=222ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-124MS` (url=202ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-112MS` (url=217ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-100MS` (url=248ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-230MS` (url=358ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-93MS` (url=241ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-382MS` (url=828ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-385MS` (url=958ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-386MS` (url=1825ms, status=HTTP 204)
25. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-387MS` (url=818ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
