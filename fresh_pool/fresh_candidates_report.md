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
1. `AKUN-001-UNKNOWN-VLESS-WS-68MS` (url=217ms, nekobox=235ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=215ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=205ms, nekobox=254ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=228ms, nekobox=233ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=225ms, nekobox=260ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=216ms, nekobox=260ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS` (url=237ms, nekobox=222ms, status=no)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=206ms, nekobox=192ms, status=no)
9. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-86MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-79MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-71MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-74MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-92MS` (url=208ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-83MS` (url=226ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-99MS` (url=218ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-86MS` (url=208ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-97MS` (url=226ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-78MS` (url=200ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-105MS` (url=212ms, status=HTTP 204)
21. `AKUN-021-466688-VLESS-WS-77MS` (url=218ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-100MS` (url=224ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-97MS` (url=197ms, status=HTTP 204)
24. `AKUN-024-3666888-VLESS-WS-114MS` (url=256ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-137MS` (url=199ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
