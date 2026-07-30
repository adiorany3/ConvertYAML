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
1. `AKUN-001-SPEEDTEST-VLESS-WS-58MS` (url=215ms, nekobox=172ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-67MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-56MS`
5. `AKUN-004-DEV-VLESS-WS-57MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-57MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-61MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-61MS` (url=204ms, nekobox=234ms, status=yes)
9. `AKUN-008-008500-VLESS-WS-71MS`
10. `AKUN-009-EU-VLESS-WS-81MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-61MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-74MS` (url=200ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-78MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-65MS` (url=208ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-67MS` (url=1730ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-91MS` (url=200ms, status=HTTP 204)
17. `AKUN-017-SPEEDTEST-VLESS-WS-115MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-SC-APHRODITEGROUP-201910-VLESS-WS-73MS` (url=213ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-87MS` (url=213ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-141MS` (url=201ms, status=HTTP 204)
21. `AKUN-021-SPEEDTEST-VLESS-WS-104MS` (url=212ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-141MS` (url=261ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-96MS` (url=214ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-170MS` (url=218ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-145MS` (url=210ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
