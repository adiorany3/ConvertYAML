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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=200ms, nekobox=247ms, status=yes)
2. `AKUN-002-RU-BAXET-20190717-VLESS-WS-65MS` (url=214ms, nekobox=278ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=220ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS` (url=220ms, nekobox=241ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-76MS` (url=227ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS` (url=225ms, nekobox=242ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-74MS` (url=247ms, nekobox=231ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-71MS` (url=218ms, nekobox=234ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-80MS` (url=247ms, nekobox=258ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-86MS` (url=228ms, nekobox=181ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-92MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-76MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-77MS` (url=218ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-85MS` (url=224ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-92MS` (url=215ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-104MS` (url=258ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-105MS` (url=231ms, status=HTTP 204)
18. `AKUN-019-ZVC-VLESS-WS-86MS` (url=212ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-120MS` (url=224ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-89MS` (url=211ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-94MS` (url=227ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-98MS` (url=216ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-157MS` (url=225ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-175MS` (url=228ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-232MS` (url=509ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
