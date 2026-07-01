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
1. `AKUN-001-UNKNOWN-VLESS-WS-63MS` (url=200ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=201ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=225ms, nekobox=227ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-59MS` (url=245ms, nekobox=250ms, status=yes)
5. `AKUN-005-WEYRO-NET-VLESS-WS-71MS` (url=204ms, nekobox=231ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-78MS` (url=218ms, nekobox=255ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-101MS` (url=227ms, nekobox=264ms, status=yes)
8. `AKUN-008-SPACECORE-VLESS-WS-73MS` (url=211ms, nekobox=249ms, status=yes)
9. `AKUN-009-U1HOST-FRA-VLESS-WS-80MS` (url=203ms, nekobox=256ms, status=yes)
10. `AKUN-010-NETCUP-VLESS-WS-76MS` (url=238ms, nekobox=233ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-86MS` (url=227ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-75MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-130MS` (url=207ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-101MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-126MS` (url=227ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-76MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-139MS` (url=221ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-119MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-91MS` (url=196ms, status=HTTP 204)
20. `AKUN-020-ZVC-VLESS-WS-84MS` (url=220ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-203MS` (url=301ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-179MS` (url=341ms, status=HTTP 204)
23. `AKUN-023-ADF-VLESS-WS-75MS` (url=208ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-376MS` (url=775ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-368MS` (url=789ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
