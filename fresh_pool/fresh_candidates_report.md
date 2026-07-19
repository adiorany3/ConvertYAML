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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-80MS` (url=200ms, nekobox=241ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=229ms, nekobox=262ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-89MS` (url=202ms, nekobox=230ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-91MS` (url=221ms, nekobox=252ms, status=yes)
5. `AKUN-005-GO-DADDY-COM-LLC-VLESS-WS-104MS` (url=205ms, nekobox=264ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-81MS` (url=201ms, nekobox=242ms, status=yes)
7. `AKUN-007-466688-VLESS-WS-109MS` (url=230ms, nekobox=262ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS` (url=199ms, nekobox=231ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-104MS` (url=223ms, nekobox=246ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-93MS` (url=213ms, nekobox=7173ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-122MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-121MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-117MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-99MS` (url=241ms, status=HTTP 204)
15. `AKUN-015-UK-GB-DCL-01-20191003-VLESS-WS-108MS` (url=257ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-132MS` (url=211ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-112MS` (url=232ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-119MS` (url=210ms, status=HTTP 204)
19. `AKUN-019-ZOOM-VLESS-WS-140MS` (url=233ms, status=HTTP 204)
20. `AKUN-020-CF-CLIENTS-VLESS-WS-80MS` (url=211ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-88MS` (url=233ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-117MS` (url=234ms, status=HTTP 204)
23. `AKUN-023-RTCOMM-SRAVNI-RU-VLESS-WS-91MS` (url=236ms, status=HTTP 204)
24. `AKUN-024-RS-RAPIDSEEDBOX-20190717-VLESS-WS-80MS` (url=207ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-94MS` (url=240ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
