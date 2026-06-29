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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=234ms, nekobox=238ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-68MS` (url=218ms, nekobox=256ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=219ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-92MS` (url=214ms, nekobox=253ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-104MS` (url=223ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS` (url=208ms, nekobox=254ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-91MS` (url=207ms, nekobox=248ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-110MS` (url=277ms, nekobox=267ms, status=yes)
9. `AKUN-009-DEV-VLESS-WS-81MS` (url=219ms, nekobox=215ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-107MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-128MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-77MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-82MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-101MS` (url=232ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-133MS` (url=231ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-194MS` (url=459ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-226MS` (url=539ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-257MS` (url=1015ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-258MS` (url=585ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-238MS` (url=515ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-260MS` (url=575ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-280MS` (url=625ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-252MS` (url=497ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-287MS` (url=576ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
