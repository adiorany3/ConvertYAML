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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-OVH-VLESS-WS-79MS` (url=234ms, nekobox=253ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=202ms, nekobox=256ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=211ms, nekobox=240ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=229ms, nekobox=230ms, status=yes)
5. `AKUN-005-SM-VLESS-WS-84MS` (url=213ms, nekobox=257ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS` (url=232ms, nekobox=232ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=227ms, nekobox=254ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS` (url=203ms, nekobox=257ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS` (url=222ms, nekobox=259ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-95MS` (url=223ms, nekobox=262ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-89MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-105MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-90MS` (url=198ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-103MS` (url=208ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-111MS` (url=216ms, status=HTTP 204)
16. `AKUN-017-RMGYVPN-VLESS-WS-256MS` (url=521ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-389MS` (url=930ms, status=HTTP 204)
18. `AKUN-020-SUKARIO-VLESS-WS-602MS` (url=1071ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-624MS` (url=1038ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-648MS` (url=1012ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-718MS` (url=1151ms, status=HTTP 204)
22. `AKUN-029-UNKNOWN-VLESS-WS-749MS` (url=1090ms, status=HTTP 204)
23. `AKUN-030-CLOUDFLARE-VLESS-WS-796MS` (url=1164ms, status=HTTP 204)
24. `AKUN-032-CLOUDFLARE-VLESS-WS-713MS` (url=1145ms, status=HTTP 204)
25. `AKUN-033-UNKNOWN-VLESS-WS-880MS` (url=1427ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
