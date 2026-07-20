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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-73MS` (url=213ms, nekobox=232ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-64MS` (url=209ms, nekobox=231ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=203ms, nekobox=252ms, status=yes)
4. `AKUN-004-GO-DADDY-COM-LLC-VLESS-WS-61MS` (url=211ms, nekobox=253ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=232ms, nekobox=259ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS` (url=203ms, nekobox=227ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS` (url=211ms, nekobox=254ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-75MS` (url=204ms, nekobox=227ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS` (url=216ms, nekobox=233ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-83MS` (url=200ms, nekobox=240ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-78MS` (url=203ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-68MS` (url=232ms, status=HTTP 204)
13. `AKUN-013-NEXUSMODS-VLESS-WS-112MS` (url=200ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-116MS` (url=200ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-121MS` (url=197ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-85MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-POLICE-VLESS-WS-125MS` (url=198ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-131MS` (url=234ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-127MS` (url=204ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-65MS` (url=214ms, status=HTTP 204)
21. `AKUN-021-466688-VLESS-WS-121MS` (url=219ms, status=HTTP 204)
22. `AKUN-022-ZOOM-VLESS-WS-80MS` (url=200ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-98MS` (url=215ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-131MS` (url=241ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-231MS` (url=575ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
