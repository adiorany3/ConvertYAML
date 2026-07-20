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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=236ms, nekobox=263ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=202ms, nekobox=262ms, status=yes)
3. `AKUN-003-UK-GB-DCL-01-20191003-VLESS-WS-74MS` (url=220ms, nekobox=259ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-70MS` (url=200ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-65MS` (url=213ms, nekobox=235ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-58MS` (url=229ms, nekobox=251ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-67MS` (url=276ms, nekobox=272ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-69MS` (url=241ms, nekobox=249ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-83MS` (url=225ms, nekobox=7177ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-72MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-76MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-78MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-92MS` (url=243ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-97MS` (url=253ms, status=HTTP 204)
15. `AKUN-015-UK-GB-DCL-01-20191003-VLESS-WS-106MS` (url=245ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-101MS` (url=243ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-150MS` (url=217ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-76MS` (url=233ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-138MS` (url=242ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-163MS` (url=237ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-137MS` (url=248ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-338MS` (url=742ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-354MS` (url=769ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-368MS` (url=857ms, status=HTTP 204)
25. `AKUN-026-WPENG-VLESS-WS-114MS` (url=263ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
