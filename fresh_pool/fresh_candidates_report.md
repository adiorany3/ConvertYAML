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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=235ms, nekobox=252ms, status=yes)
2. `AKUN-002-LEVIKOGJGFDD-VLESS-WS-60MS` (url=222ms, nekobox=270ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS` (url=226ms, nekobox=268ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-67MS` (url=230ms, nekobox=268ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-67MS` (url=219ms, nekobox=261ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-67MS` (url=262ms, nekobox=272ms, status=yes)
7. `AKUN-007-008500-VLESS-WS-65MS` (url=229ms, nekobox=259ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-59MS` (url=219ms, nekobox=264ms, status=yes)
9. `AKUN-009-EU-VLESS-WS-65MS` (url=229ms, nekobox=258ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-75MS` (url=227ms, nekobox=270ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-67MS` (url=229ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-71MS` (url=243ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-69MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-76MS` (url=251ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-87MS` (url=235ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-58MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-74MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-MYBB-VLESS-WS-84MS` (url=237ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-88MS` (url=344ms, status=HTTP 204)
20. `AKUN-020-ADF-VLESS-WS-86MS` (url=260ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-61MS` (url=227ms, status=HTTP 204)
22. `AKUN-022-SHOPIFY-VLESS-WS-72MS` (url=234ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-90MS` (url=281ms, status=HTTP 204)
24. `AKUN-024-ALIBABA-VLESS-WS-75MS` (url=230ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-103MS` (url=352ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
