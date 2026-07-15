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
1. `AKUN-001-UNKNOWN-VLESS-WS-69MS` (url=249ms, nekobox=324ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=237ms, nekobox=255ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=269ms, nekobox=273ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-76MS` (url=230ms, nekobox=274ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=267ms, nekobox=264ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS` (url=257ms, nekobox=286ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS` (url=241ms, nekobox=288ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS` (url=230ms, nekobox=7177ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-87MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-87MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-75MS` (url=296ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-109MS` (url=263ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-74MS` (url=248ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-74MS` (url=268ms, status=HTTP 204)
16. `AKUN-016-MYBB-VLESS-WS-107MS` (url=274ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-75MS` (url=292ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-82MS` (url=258ms, status=HTTP 204)
19. `AKUN-019-US-VLESS-WS-90MS` (url=250ms, status=HTTP 204)
20. `AKUN-020-MYBB-VLESS-WS-87MS` (url=344ms, status=HTTP 204)
21. `AKUN-021-MEDIUM-VLESS-WS-84MS` (url=255ms, status=HTTP 204)
22. `AKUN-022-ADF-VLESS-WS-98MS` (url=238ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-102MS` (url=244ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-105MS` (url=244ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-103MS` (url=256ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
