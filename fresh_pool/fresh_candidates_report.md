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
1. `AKUN-001-UNKNOWN-VLESS-WS-69MS` (url=294ms, nekobox=299ms, status=yes)
2. `AKUN-002-466688-VLESS-WS-82MS` (url=253ms, nekobox=263ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-78MS` (url=242ms, nekobox=280ms, status=yes)
4. `AKUN-004-466688-VLESS-WS-90MS` (url=292ms, nekobox=276ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-74MS` (url=251ms, nekobox=290ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-90MS` (url=242ms, nekobox=264ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-107MS` (url=235ms, nekobox=273ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-113MS` (url=241ms, nekobox=270ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-103MS` (url=289ms, nekobox=257ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-98MS` (url=276ms, nekobox=277ms, status=yes)
11. `AKUN-011-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-82MS` (url=242ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-82MS` (url=262ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS` (url=234ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-86MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-131MS` (url=233ms, status=HTTP 204)
16. `AKUN-016-DE-XTOM-20210903-VLESS-WS-87MS` (url=258ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-98MS` (url=243ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-285MS` (url=568ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-286MS` (url=659ms, status=HTTP 204)
20. `AKUN-021-SPEEDTEST-VLESS-WS-299MS` (url=630ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-307MS` (url=605ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-82MS` (url=295ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-301MS` (url=641ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-343MS` (url=597ms, status=HTTP 204)
25. `AKUN-026-MICROSOFT-VLESS-WS-321MS` (url=794ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
