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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=205ms, nekobox=237ms, status=yes)
2. `AKUN-002-GOV-VLESS-WS-63MS` (url=203ms, nekobox=225ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=217ms, nekobox=222ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=222ms, nekobox=251ms, status=yes)
5. `AKUN-005-DEV-VLESS-WS-70MS` (url=218ms, nekobox=244ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=211ms, nekobox=239ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS` (url=207ms, nekobox=7176ms, status=no)
8. `AKUN-007-DEV-VLESS-WS-68MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-69MS`
11. `AKUN-010-ZVC-VLESS-WS-80MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-85MS` (url=216ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-77MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-68MS` (url=210ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-73MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-84MS` (url=206ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-63MS` (url=198ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-72MS` (url=211ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-78MS` (url=201ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-74MS` (url=210ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-120MS` (url=200ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-125MS` (url=243ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-64MS` (url=217ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-87MS` (url=199ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-86MS` (url=200ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
