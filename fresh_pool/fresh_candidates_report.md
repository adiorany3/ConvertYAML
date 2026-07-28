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
1. `AKUN-001-UNKNOWN-VLESS-WS-53MS` (url=208ms, nekobox=238ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-56MS` (url=208ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-58MS` (url=220ms, nekobox=245ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-57MS` (url=214ms, nekobox=242ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-65MS` (url=211ms, nekobox=234ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS` (url=212ms, nekobox=250ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS` (url=218ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS` (url=221ms, nekobox=295ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-66MS` (url=216ms, nekobox=254ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-57MS` (url=211ms, nekobox=240ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-102MS` (url=200ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-63MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-64MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-83MS` (url=196ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-62MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-102MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-83MS` (url=219ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-115MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-115MS` (url=194ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-113MS` (url=222ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-71MS` (url=217ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-97MS` (url=214ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-101MS` (url=225ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-104MS` (url=209ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-325MS` (url=689ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
