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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=216ms, nekobox=230ms, status=yes)
2. `AKUN-002-OVH-VLESS-WS-64MS` (url=206ms, nekobox=224ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=205ms, nekobox=249ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-67MS` (url=208ms, nekobox=235ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=209ms, nekobox=244ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=214ms, nekobox=249ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-69MS` (url=211ms, nekobox=233ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-75MS` (url=198ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS` (url=212ms, nekobox=7178ms, status=no)
10. `AKUN-009-CZ-LOTUNA-19970206-VLESS-WS-85MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-74MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-96MS` (url=204ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-73MS` (url=200ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-111MS` (url=209ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-88MS` (url=201ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-81MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-85MS` (url=221ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-98MS` (url=217ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-74MS` (url=203ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-95MS` (url=211ms, status=HTTP 204)
22. `AKUN-022-DEV-VLESS-WS-82MS` (url=213ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-97MS` (url=211ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-82MS` (url=228ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-75MS` (url=213ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
