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
1. `AKUN-001-UNKNOWN-VLESS-WS-59MS` (url=214ms, nekobox=246ms, status=yes)
2. `AKUN-002-SM-VLESS-WS-62MS` (url=218ms, nekobox=235ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS` (url=201ms, nekobox=236ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-58MS` (url=219ms, nekobox=252ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-61MS` (url=227ms, nekobox=250ms, status=yes)
6. `AKUN-006-SPEEDTEST-VLESS-WS-62MS` (url=227ms, nekobox=170ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-63MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS`
10. `AKUN-009-DIGITALOCEAN-VLESS-WS-100MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-101MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-59MS` (url=221ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-82MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-113MS` (url=198ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-85MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-97MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-137MS` (url=219ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-109MS` (url=358ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-101MS` (url=220ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-165MS` (url=217ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-66MS` (url=216ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-198MS` (url=273ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-126MS` (url=230ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-124MS` (url=218ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-354MS` (url=760ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
