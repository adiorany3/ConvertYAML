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
1. `AKUN-001-UNKNOWN-VLESS-WS-69MS` (url=240ms, nekobox=303ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-71MS` (url=231ms, nekobox=284ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=240ms, nekobox=253ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=254ms, nekobox=264ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-73MS` (url=237ms, nekobox=249ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-75MS` (url=236ms, nekobox=272ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-74MS` (url=248ms, nekobox=281ms, status=yes)
8. `AKUN-008-WPENG-VLESS-WS-83MS` (url=274ms, nekobox=270ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-66MS` (url=260ms, nekobox=257ms, status=yes)
10. `AKUN-010-DIXONS-VLESS-WS-84MS` (url=248ms, nekobox=272ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-77MS` (url=237ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-76MS` (url=236ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-76MS` (url=233ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-86MS` (url=239ms, status=HTTP 204)
15. `AKUN-015-ES-FORNEX-20160629-VLESS-WS-89MS` (url=255ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-89MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-84MS` (url=245ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-74MS` (url=242ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-74MS` (url=254ms, status=HTTP 204)
20. `AKUN-020-SHOPIFY-VLESS-WS-95MS` (url=238ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-117MS` (url=273ms, status=HTTP 204)
22. `AKUN-022-US-VLESS-WS-93MS` (url=234ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-112MS` (url=260ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-127MS` (url=247ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-77MS` (url=254ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
