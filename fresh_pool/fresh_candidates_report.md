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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=915ms, nekobox=896ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=198ms, nekobox=244ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-60MS` (url=215ms, nekobox=235ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-74MS` (url=224ms, nekobox=252ms, status=yes)
5. `AKUN-005-DEV-VLESS-WS-66MS` (url=218ms, nekobox=238ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-103MS` (url=254ms, nekobox=266ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS` (url=219ms, nekobox=247ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-73MS` (url=216ms, nekobox=240ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-89MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-97MS`
11. `AKUN-012-UNKNOWN-VLESS-WS-100MS` (url=204ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-91MS` (url=214ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-89MS` (url=221ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-102MS` (url=217ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-103MS` (url=239ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-79MS` (url=218ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-134MS` (url=211ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-92MS` (url=219ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-114MS` (url=237ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-101MS` (url=223ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-93MS` (url=217ms, status=HTTP 204)
22. `AKUN-023-090227-VLESS-WS-285MS` (url=575ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-303MS` (url=627ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-669MS` (url=1165ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-752MS` (url=1197ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
