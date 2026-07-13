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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=217ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=211ms, nekobox=228ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=211ms, nekobox=253ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS` (url=211ms, nekobox=229ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=217ms, nekobox=234ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS` (url=218ms, nekobox=253ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS` (url=201ms, nekobox=258ms, status=yes)
8. `AKUN-008-IDC-SG-VLESS-WS-119MS` (url=216ms, nekobox=268ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-80MS` (url=211ms, nekobox=245ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-115MS` (url=208ms, nekobox=246ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-137MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-116MS` (url=212ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-140MS` (url=204ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-134MS` (url=245ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-118MS` (url=230ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-86MS` (url=306ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-156MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-136MS` (url=258ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-242MS` (url=573ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-258MS` (url=532ms, status=HTTP 204)
21. `AKUN-021-SPEEDTEST-VLESS-WS-257MS` (url=528ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-269MS` (url=627ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-274MS` (url=555ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-249MS` (url=486ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-306MS` (url=1737ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
