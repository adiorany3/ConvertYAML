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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-56MS` (url=217ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=221ms, nekobox=241ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-67MS` (url=211ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-88MS` (url=224ms, nekobox=256ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-103MS` (url=198ms, nekobox=248ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS` (url=269ms, nekobox=243ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-93MS` (url=203ms, nekobox=252ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS` (url=221ms, nekobox=246ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-84MS` (url=222ms, nekobox=228ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-93MS` (url=322ms, nekobox=242ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-132MS` (url=219ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-88MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-116MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-138MS` (url=207ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-121MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-148MS` (url=231ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS` (url=214ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-72MS` (url=218ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-344MS` (url=752ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-383MS` (url=843ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-378MS` (url=831ms, status=HTTP 204)
22. `AKUN-022-CONFLU-VLESS-WS-343MS` (url=732ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-76MS` (url=222ms, status=HTTP 204)
24. `AKUN-024-WPENG-VLESS-WS-388MS` (url=793ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-414MS` (url=858ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
