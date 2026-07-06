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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=224ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=293ms, nekobox=272ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS` (url=206ms, nekobox=243ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=239ms, nekobox=251ms, status=yes)
5. `AKUN-005-WEYRO-NET-VLESS-WS-74MS` (url=218ms, nekobox=265ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-69MS` (url=240ms, nekobox=262ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-59MS` (url=214ms, nekobox=274ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-67MS` (url=229ms, nekobox=239ms, status=yes)
9. `AKUN-009-APNIC-AP-VLESS-WS-86MS` (url=227ms, nekobox=237ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-93MS` (url=208ms, nekobox=253ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-80MS` (url=230ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-87MS` (url=226ms, status=HTTP 204)
13. `AKUN-014-DEV-VLESS-WS-88MS` (url=236ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-78MS` (url=219ms, status=HTTP 204)
15. `AKUN-016-WEBEX-VLESS-WS-78MS` (url=214ms, status=HTTP 204)
16. `AKUN-017-WEBEX-VLESS-WS-60MS` (url=230ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-83MS` (url=291ms, status=HTTP 204)
18. `AKUN-019-466688-VLESS-WS-78MS` (url=233ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-79MS` (url=234ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-334MS` (url=770ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-355MS` (url=745ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-380MS` (url=848ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-366MS` (url=792ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-376MS` (url=778ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-384MS` (url=827ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
