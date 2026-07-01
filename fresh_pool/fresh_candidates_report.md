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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=213ms, nekobox=217ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-66MS` (url=190ms, nekobox=235ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-65MS` (url=221ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=219ms, nekobox=256ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=202ms, nekobox=224ms, status=yes)
6. `AKUN-006-HOSTOFF-NET-VLESS-WS-87MS` (url=200ms, nekobox=256ms, status=yes)
7. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-76MS` (url=216ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-72MS` (url=207ms, nekobox=254ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS` (url=224ms, nekobox=248ms, status=yes)
10. `AKUN-010-MYBB-VLESS-WS-77MS` (url=193ms, nekobox=218ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS` (url=207ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-103MS` (url=216ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-97MS` (url=214ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-87MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-SPACECORE-VLESS-WS-97MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-73MS` (url=211ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-121MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-89MS` (url=207ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-146MS` (url=217ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-157MS` (url=304ms, status=HTTP 204)
21. `AKUN-021-ADF-VLESS-WS-80MS` (url=198ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-96MS` (url=278ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-364MS` (url=734ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-346MS` (url=827ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-397MS` (url=837ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
