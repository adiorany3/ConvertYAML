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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=208ms, nekobox=241ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-70MS` (url=211ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=223ms, nekobox=238ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-70MS` (url=225ms, nekobox=259ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-66MS` (url=215ms, nekobox=247ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-74MS` (url=219ms, nekobox=228ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-76MS` (url=222ms, nekobox=248ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-77MS` (url=228ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-60MS` (url=198ms, nekobox=233ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-72MS` (url=217ms, nekobox=7177ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-84MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-66MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-63MS` (url=527ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-79MS` (url=228ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-93MS` (url=227ms, status=HTTP 204)
17. `AKUN-017-MYBB-VLESS-WS-76MS` (url=202ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-79MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-1PASSWORD-VLESS-WS-78MS` (url=212ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-73MS` (url=221ms, status=HTTP 204)
21. `AKUN-021-CCWU-VLESS-WS-75MS` (url=225ms, status=HTTP 204)
22. `AKUN-022-ADF-VLESS-WS-111MS` (url=208ms, status=HTTP 204)
23. `AKUN-023-MEDIUM-VLESS-WS-77MS` (url=201ms, status=HTTP 204)
24. `AKUN-024-WEBEX-VLESS-WS-73MS` (url=213ms, status=HTTP 204)
25. `AKUN-025-DEV-VLESS-WS-86MS` (url=202ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
