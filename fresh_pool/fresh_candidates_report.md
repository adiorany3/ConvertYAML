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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-57MS` (url=225ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=209ms, nekobox=238ms, status=yes)
3. `AKUN-003-NOTION-WEB-VLESS-WS-63MS` (url=224ms, nekobox=7177ms, status=no)
4. `AKUN-003-UNKNOWN-VLESS-WS-73MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-65MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-88MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-56MS`
8. `AKUN-007-PAGES-VLESS-WS-80MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-76MS`
10. `AKUN-009-DEV-VLESS-WS-87MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-93MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-96MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-109MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-78MS` (url=210ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-117MS` (url=198ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-69MS` (url=234ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-87MS` (url=212ms, status=HTTP 204)
18. `AKUN-018-ZOOM-VLESS-WS-56MS` (url=209ms, status=HTTP 204)
19. `AKUN-019-LEVIKOGJGFDD-VLESS-WS-118MS` (url=277ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-81MS` (url=229ms, status=HTTP 204)
21. `AKUN-022-090227-VLESS-WS-296MS` (url=691ms, status=HTTP 204)
22. `AKUN-023-LEVIKOGJGFDD-VLESS-WS-356MS` (url=1533ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-357MS` (url=759ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-544MS` (url=936ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-624MS` (url=972ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
