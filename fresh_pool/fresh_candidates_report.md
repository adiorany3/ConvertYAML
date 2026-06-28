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
1. `AKUN-001-UNKNOWN-VLESS-WS-75MS` (url=221ms, nekobox=242ms, status=yes)
2. `AKUN-002-COMPREND-NET-VLESS-WS-109MS` (url=225ms, nekobox=225ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=226ms, nekobox=239ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-93MS` (url=228ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-105MS` (url=488ms, nekobox=405ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-106MS` (url=208ms, nekobox=241ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-134MS` (url=538ms, nekobox=523ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-128MS` (url=207ms, nekobox=230ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-122MS` (url=225ms, nekobox=257ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-136MS` (url=214ms, nekobox=264ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-86MS` (url=232ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-79MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-230MS` (url=495ms, status=HTTP 204)
14. `AKUN-014-GUARDNETWORK-VLESS-WS-267MS` (url=577ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-232MS` (url=495ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-265MS` (url=624ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-259MS` (url=4135ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-98MS` (url=315ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-224MS` (url=492ms, status=HTTP 204)
20. `AKUN-020-TIME-VLESS-WS-138MS` (url=587ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-315MS` (url=556ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-97MS` (url=230ms, status=HTTP 204)
23. `AKUN-023-CREATIVECOMMONS-VLESS-WS-127MS` (url=478ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-294MS` (url=623ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-267MS` (url=583ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
