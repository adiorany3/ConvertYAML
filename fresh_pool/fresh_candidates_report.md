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
1. `AKUN-001-PUBLICDOMAINREGISTRY-NET-VLESS-WS-82MS` (url=225ms, nekobox=259ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=226ms, nekobox=250ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS` (url=227ms, nekobox=254ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=201ms, nekobox=254ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-85MS` (url=224ms, nekobox=251ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=236ms, nekobox=230ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=210ms, nekobox=253ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=222ms, nekobox=257ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-98MS` (url=214ms, nekobox=228ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-101MS`
11. `AKUN-012-UNKNOWN-VLESS-WS-91MS` (url=203ms, status=HTTP 204)
12. `AKUN-013-UNKNOWN-VLESS-WS-87MS` (url=228ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-112MS` (url=237ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-127MS` (url=219ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-113MS` (url=231ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-127MS` (url=226ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-138MS` (url=211ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-139MS` (url=212ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-101MS` (url=227ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-248MS` (url=558ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-238MS` (url=517ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-258MS` (url=1279ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-272MS` (url=581ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-268MS` (url=3982ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-423MS` (url=715ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
