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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-69MS` (url=205ms, nekobox=235ms, status=yes)
2. `AKUN-002-SIN-VLESS-WS-69MS` (url=199ms, nekobox=232ms, status=yes)
3. `AKUN-003-MEDIUM-VLESS-WS-77MS` (url=203ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=217ms, nekobox=245ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=218ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=228ms, nekobox=232ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-83MS` (url=205ms, nekobox=245ms, status=yes)
8. `AKUN-008-WPENG-VLESS-WS-77MS` (url=221ms, nekobox=255ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-69MS` (url=229ms, nekobox=234ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-82MS` (url=208ms, nekobox=230ms, status=yes)
11. `AKUN-011-OVH-VLESS-WS-107MS` (url=216ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-109MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-88MS` (url=201ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-81MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-130MS` (url=235ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-120MS` (url=208ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-69MS` (url=199ms, status=HTTP 204)
18. `AKUN-018-1PASSWORD-VLESS-WS-88MS` (url=236ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-102MS` (url=298ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-121MS` (url=261ms, status=HTTP 204)
21. `AKUN-021-MYBB-VLESS-WS-93MS` (url=212ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-231MS` (url=518ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-263MS` (url=499ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-266MS` (url=586ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-268MS` (url=571ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
