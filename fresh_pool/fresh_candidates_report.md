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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=215ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=206ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=204ms, nekobox=236ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-69MS` (url=203ms, nekobox=242ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-67MS` (url=204ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=220ms, nekobox=248ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-66MS` (url=233ms, nekobox=247ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-96MS` (url=202ms, nekobox=243ms, status=yes)
9. `AKUN-009-DIXONS-VLESS-WS-91MS` (url=213ms, nekobox=229ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-95MS` (url=206ms, nekobox=254ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-86MS` (url=199ms, status=HTTP 204)
12. `AKUN-012-BGP48-HK-VLESS-WS-123MS` (url=248ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-88MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-118MS` (url=241ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-127MS` (url=212ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-125MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-115MS` (url=208ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-140MS` (url=254ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-122MS` (url=210ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-105MS` (url=226ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-115MS` (url=212ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-143MS` (url=238ms, status=HTTP 204)
23. `AKUN-023-UK-GB-DCL-01-20191003-VLESS-WS-164MS` (url=240ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-239MS` (url=523ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-231MS` (url=936ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
