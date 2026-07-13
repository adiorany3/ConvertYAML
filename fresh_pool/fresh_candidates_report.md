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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-87MS` (url=496ms, nekobox=342ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=454ms, nekobox=399ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-98MS` (url=406ms, nekobox=407ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=334ms, nekobox=369ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-102MS` (url=287ms, nekobox=370ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-106MS` (url=364ms, nekobox=436ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-101MS` (url=392ms, nekobox=366ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-112MS` (url=348ms, nekobox=389ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS` (url=330ms, nekobox=381ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-100MS` (url=347ms, nekobox=371ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-118MS` (url=402ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-100MS` (url=341ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-123MS` (url=1018ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-133MS` (url=393ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-123MS` (url=338ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-130MS` (url=363ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-113MS` (url=398ms, status=HTTP 204)
18. `AKUN-018-PUBLICDOMAINREGISTRY-NET-VLESS-WS-137MS` (url=442ms, status=HTTP 204)
19. `AKUN-019-US-VLESS-WS-185MS` (url=410ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-113MS` (url=351ms, status=HTTP 204)
21. `AKUN-021-ES-FORNEX-20160629-VLESS-WS-137MS` (url=328ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-128MS` (url=401ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-318MS` (url=719ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-350MS` (url=791ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-338MS` (url=676ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
