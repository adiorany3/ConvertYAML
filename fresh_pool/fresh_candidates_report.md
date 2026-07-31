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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=223ms, nekobox=173ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=208ms, nekobox=232ms, status=yes)
4. `AKUN-003-MYBB-VLESS-WS-62MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS`
6. `AKUN-005-DEV-VLESS-WS-63MS`
7. `AKUN-006-ADF-VLESS-WS-64MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-68MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-61MS` (url=223ms, nekobox=176ms, status=no)
10. `AKUN-008-UNKNOWN-VLESS-WS-71MS`
11. `AKUN-009-MEDIUM-VLESS-WS-82MS`
12. `AKUN-010-DEV-VLESS-WS-69MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-89MS` (url=209ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-87MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-95MS` (url=201ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-78MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-83MS` (url=202ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-67MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-70MS` (url=214ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-60MS` (url=214ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-63MS` (url=196ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-69MS` (url=220ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-80MS` (url=220ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-62MS` (url=219ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-189MS` (url=277ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
