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
1. `AKUN-001-UNKNOWN-VLESS-WS-58MS` (url=226ms, nekobox=245ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-62MS` (url=231ms, nekobox=263ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS` (url=213ms, nekobox=244ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-65MS` (url=246ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-65MS` (url=214ms, nekobox=259ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=227ms, nekobox=253ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-66MS` (url=214ms, nekobox=261ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-71MS` (url=215ms, nekobox=269ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-61MS` (url=231ms, nekobox=321ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-73MS` (url=233ms, nekobox=263ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-69MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-DEV-VLESS-WS-83MS` (url=222ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-94MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-106MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-63MS` (url=249ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-72MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-105MS` (url=210ms, status=HTTP 204)
18. `AKUN-018-SPEEDTEST-VLESS-WS-96MS` (url=231ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-104MS` (url=214ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-82MS` (url=226ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-103MS` (url=224ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-199MS` (url=679ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-357MS` (url=768ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-379MS` (url=3590ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-374MS` (url=785ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
