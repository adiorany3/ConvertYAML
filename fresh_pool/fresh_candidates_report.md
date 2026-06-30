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
1. `AKUN-001-UNKNOWN-VLESS-WS-80MS` (url=224ms, nekobox=260ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS` (url=199ms, nekobox=253ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-81MS` (url=232ms, nekobox=262ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-94MS` (url=236ms, nekobox=253ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS` (url=238ms, nekobox=194ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-107MS`
7. `AKUN-006-COMPREND-NET-VLESS-WS-84MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-116MS`
10. `AKUN-009-COMPREND-NET-VLESS-WS-87MS`
11. `AKUN-010-HOSTOFF-NET-VLESS-WS-95MS`
12. `AKUN-012-U1HOST-FRA-VLESS-WS-107MS` (url=236ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-113MS` (url=210ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-114MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-99MS` (url=211ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-114MS` (url=201ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-89MS` (url=205ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-145MS` (url=246ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-113MS` (url=210ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-100MS` (url=226ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-94MS` (url=235ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-249MS` (url=512ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-262MS` (url=564ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-264MS` (url=582ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-264MS` (url=506ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
