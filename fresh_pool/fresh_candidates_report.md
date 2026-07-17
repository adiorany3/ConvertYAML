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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=222ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=226ms, nekobox=250ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=208ms, nekobox=7177ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS` (url=220ms, nekobox=7177ms, status=no)
7. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS`
8. `AKUN-006-GO-DADDY-COM-LLC-VLESS-WS-78MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS`
12. `AKUN-010-UNKNOWN-VLESS-WS-94MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-81MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-99MS` (url=217ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-73MS` (url=219ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-75MS` (url=204ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-96MS` (url=613ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-99MS` (url=218ms, status=HTTP 204)
19. `AKUN-019-ADF-VLESS-WS-90MS` (url=214ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-114MS` (url=223ms, status=HTTP 204)
21. `AKUN-021-POLICE-VLESS-WS-109MS` (url=233ms, status=HTTP 204)
22. `AKUN-022-WEBEX-VLESS-WS-106MS` (url=232ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-149MS` (url=203ms, status=HTTP 204)
24. `AKUN-024-MEDIUM-VLESS-WS-110MS` (url=220ms, status=HTTP 204)
25. `AKUN-025-1PASSWORD-VLESS-WS-156MS` (url=203ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
