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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-56MS` (url=234ms, nekobox=259ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=222ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-60MS` (url=228ms, nekobox=251ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-62MS` (url=235ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-62MS` (url=214ms, nekobox=7177ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-61MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-63MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-66MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-64MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-57MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-76MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-77MS` (url=222ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-59MS` (url=221ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-67MS` (url=228ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-82MS` (url=227ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-103MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-MEDIUM-VLESS-WS-64MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-CCWU-VLESS-WS-77MS` (url=235ms, status=HTTP 204)
19. `AKUN-019-ZVC-VLESS-WS-60MS` (url=229ms, status=HTTP 204)
20. `AKUN-020-1PASSWORD-VLESS-WS-66MS` (url=239ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-116MS` (url=319ms, status=HTTP 204)
22. `AKUN-022-LEVIKOGJGFDD-VLESS-WS-248MS` (url=688ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-263MS` (url=556ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-349MS` (url=645ms, status=HTTP 204)
25. `AKUN-025-SUKARIO-VLESS-WS-457MS` (url=772ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
