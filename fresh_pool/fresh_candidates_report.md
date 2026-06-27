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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=241ms, nekobox=232ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-68MS` (url=197ms, nekobox=236ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=223ms, nekobox=179ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=218ms, nekobox=245ms, status=yes)
8. `AKUN-007-DE-XTOM-20210903-VLESS-WS-73MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-69MS` (url=198ms, nekobox=196ms, status=no)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-69MS` (url=196ms, nekobox=177ms, status=no)
12. `AKUN-009-UNKNOWN-VLESS-WS-70MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-73MS` (url=200ms, nekobox=176ms, status=no)
14. `AKUN-010-UNKNOWN-VLESS-WS-72MS`
15. `AKUN-015-ZOOM-VLESS-WS-81MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-82MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-90MS` (url=200ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-96MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-357MS` (url=778ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-368MS` (url=845ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-374MS` (url=849ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-403MS` (url=930ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-382MS` (url=628ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-396MS` (url=847ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-422MS` (url=874ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
