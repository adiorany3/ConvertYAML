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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=223ms, nekobox=240ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-74MS` (url=205ms, nekobox=251ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-61MS` (url=201ms, nekobox=229ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=218ms, nekobox=248ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=221ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=215ms, nekobox=254ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=230ms, nekobox=182ms, status=no)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-75MS` (url=198ms, nekobox=174ms, status=no)
9. `AKUN-007-CLOUDFLARE-VLESS-WS-64MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS`
11. `AKUN-009-CZ-LOTUNA-19970206-VLESS-WS-87MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-77MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-93MS` (url=283ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-92MS` (url=213ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-120MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-76MS` (url=203ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-101MS` (url=215ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-129MS` (url=225ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-132MS` (url=225ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-103MS` (url=228ms, status=HTTP 204)
21. `AKUN-021-POLICE-VLESS-WS-130MS` (url=206ms, status=HTTP 204)
22. `AKUN-022-466688-VLESS-WS-165MS` (url=226ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-165MS` (url=212ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-246MS` (url=505ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-246MS` (url=506ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
