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
1. `AKUN-001-WPENG-VLESS-WS-67MS` (url=280ms, nekobox=253ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=246ms, nekobox=279ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-75MS` (url=232ms, nekobox=266ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS` (url=246ms, nekobox=274ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-74MS` (url=279ms, nekobox=187ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS`
9. `AKUN-008-UK-GB-DCL-01-20191003-VLESS-WS-63MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-74MS`
11. `AKUN-010-ZOOM-VLESS-WS-74MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-97MS` (url=239ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-87MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-110MS` (url=245ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-75MS` (url=244ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-82MS` (url=241ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-107MS` (url=242ms, status=HTTP 204)
18. `AKUN-018-MYBB-VLESS-WS-111MS` (url=255ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-111MS` (url=254ms, status=HTTP 204)
20. `AKUN-020-1PASSWORD-VLESS-WS-122MS` (url=240ms, status=HTTP 204)
21. `AKUN-021-MEDIUM-VLESS-WS-104MS` (url=241ms, status=HTTP 204)
22. `AKUN-022-COMPREND-NET-VLESS-WS-149MS` (url=253ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-77MS` (url=234ms, status=HTTP 204)
24. `AKUN-024-PAGES-VLESS-WS-191MS` (url=245ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-259MS` (url=537ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
