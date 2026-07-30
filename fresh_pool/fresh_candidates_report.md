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
1. `AKUN-001-CCWU-VLESS-WS-58MS` (url=221ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=211ms, nekobox=237ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-62MS` (url=225ms, nekobox=244ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-66MS` (url=226ms, nekobox=258ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-66MS` (url=224ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-59MS` (url=222ms, nekobox=250ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS` (url=222ms, nekobox=7178ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-91MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-82MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-85MS`
12. `AKUN-012-LEVIKOGJGFDD-VLESS-WS-76MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-92MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-77MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-83MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-67MS` (url=237ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-101MS` (url=219ms, status=HTTP 204)
18. `AKUN-018-SPEEDTEST-VLESS-WS-69MS` (url=228ms, status=HTTP 204)
19. `AKUN-019-BIGCOMMERCE-VLESS-WS-94MS` (url=224ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-108MS` (url=216ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-115MS` (url=231ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-74MS` (url=221ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-73MS` (url=228ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-164MS` (url=225ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-63MS` (url=204ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
