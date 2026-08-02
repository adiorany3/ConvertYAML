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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=210ms, nekobox=232ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=208ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS` (url=202ms, nekobox=241ms, status=yes)
4. `AKUN-004-SPEEDTEST-VLESS-WS-60MS` (url=205ms, nekobox=179ms, status=no)
5. `AKUN-004-UNKNOWN-VLESS-WS-61MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-63MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-59MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-62MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-66MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-62MS`
11. `AKUN-010-MEDIUM-VLESS-WS-83MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-71MS` (url=199ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-84MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-76MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-76MS` (url=211ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-75MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-76MS` (url=208ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-77MS` (url=217ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-116MS` (url=207ms, status=HTTP 204)
20. `AKUN-020-CCWU-VLESS-WS-96MS` (url=203ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-89MS` (url=221ms, status=HTTP 204)
22. `AKUN-022-SPEEDTEST-VLESS-WS-126MS` (url=217ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-74MS` (url=206ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-65MS` (url=207ms, status=HTTP 204)
25. `AKUN-025-RMGYVPN-VLESS-WS-181MS` (url=334ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
