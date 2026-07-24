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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-57MS`
2. `AKUN-002-ZVC-VLESS-WS-61MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-61MS`
4. `AKUN-004-ZVC-VLESS-WS-63MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-77MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-85MS` (url=229ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-91MS` (url=211ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-97MS` (url=219ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-84MS` (url=219ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-72MS` (url=228ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-81MS` (url=226ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-148MS` (url=297ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-74MS` (url=258ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-140MS` (url=235ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-332MS` (url=743ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-339MS` (url=758ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-645MS` (url=1052ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-705MS` (url=1117ms, status=HTTP 204)
24. `AKUN-031-CLOUDFLARE-VLESS-WS-775MS` (url=1140ms, status=HTTP 204)
25. `AKUN-032-SUKARIO-VLESS-WS-655MS` (url=1113ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
