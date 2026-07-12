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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-77MS` (url=201ms, nekobox=234ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-75MS` (url=204ms, nekobox=237ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-75MS` (url=208ms, nekobox=242ms, status=yes)
4. `AKUN-004-ZOOM-VLESS-WS-75MS` (url=229ms, nekobox=259ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-84MS` (url=233ms, nekobox=233ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-92MS` (url=233ms, nekobox=232ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-92MS` (url=234ms, nekobox=257ms, status=yes)
8. `AKUN-008-PUBLICDOMAINREGISTRY-NET-VLESS-WS-92MS` (url=232ms, nekobox=245ms, status=yes)
9. `AKUN-009-US-VLESS-WS-98MS` (url=233ms, nekobox=254ms, status=yes)
10. `AKUN-010-UDACITY-VLESS-WS-104MS` (url=229ms, nekobox=283ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-102MS` (url=227ms, status=HTTP 204)
12. `AKUN-012-466688-VLESS-WS-118MS` (url=245ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-105MS` (url=238ms, status=HTTP 204)
14. `AKUN-014-DE-XTOM-20190821-VLESS-WS-93MS` (url=226ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-100MS` (url=224ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-138MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-135MS` (url=207ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-195MS` (url=283ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-365MS` (url=925ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-365MS` (url=817ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-383MS` (url=4587ms, status=HTTP 204)
22. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-400MS` (url=841ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-647MS` (url=1097ms, status=HTTP 204)
24. `AKUN-027-GAMEFICTOINSPEED-VLESS-WS-743MS` (url=1205ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-695MS` (url=1134ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
