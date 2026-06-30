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
1. `AKUN-001-ORACLE-VLESS-WS-62MS` (url=213ms, nekobox=238ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-63MS` (url=222ms, nekobox=246ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-66MS` (url=228ms, nekobox=230ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-69MS` (url=255ms, nekobox=178ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS`
6. `AKUN-005-COMPREND-NET-VLESS-WS-71MS`
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS`
8. `AKUN-007-ZVC-VLESS-WS-69MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS`
10. `AKUN-009-COMPREND-NET-VLESS-WS-113MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-91MS` (url=206ms, nekobox=180ms, status=no)
12. `AKUN-010-UNKNOWN-VLESS-WS-73MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-128MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-71MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-75MS` (url=236ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-81MS` (url=214ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-59MS` (url=222ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-356MS` (url=758ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-352MS` (url=744ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-91MS` (url=230ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-371MS` (url=814ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-392MS` (url=823ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-372MS` (url=712ms, status=HTTP 204)
24. `AKUN-027-MICROSOFT-VLESS-WS-390MS` (url=824ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-726MS` (url=1210ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
