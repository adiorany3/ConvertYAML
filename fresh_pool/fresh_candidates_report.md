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
1. `AKUN-001-UNKNOWN-VLESS-WS-63MS` (url=222ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=220ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS` (url=216ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=234ms, nekobox=263ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-90MS` (url=222ms, nekobox=253ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-74MS` (url=213ms, nekobox=244ms, status=yes)
7. `AKUN-007-BGP48-HK-VLESS-WS-85MS` (url=230ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS` (url=230ms, nekobox=261ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS` (url=236ms, nekobox=272ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-91MS` (url=230ms, nekobox=257ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-75MS` (url=224ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-83MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-93MS` (url=205ms, status=HTTP 204)
14. `AKUN-014-NEXUSMODS-VLESS-WS-95MS` (url=253ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-78MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-86MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-SHOPIFY-VLESS-WS-78MS` (url=224ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-80MS` (url=230ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-102MS` (url=232ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-64MS` (url=212ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-84MS` (url=222ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-117MS` (url=227ms, status=HTTP 204)
23. `AKUN-023-UK-GB-DCL-01-20191003-VLESS-WS-112MS` (url=230ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-85MS` (url=225ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-99MS` (url=247ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
