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
1. `AKUN-001-UNKNOWN-VLESS-WS-58MS` (url=204ms, nekobox=221ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=200ms, nekobox=230ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-62MS` (url=201ms, nekobox=222ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-62MS` (url=198ms, nekobox=1238ms, status=yes)
5. `AKUN-005-MEDIUM-VLESS-WS-63MS` (url=214ms, nekobox=224ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-67MS` (url=213ms, nekobox=224ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-69MS` (url=209ms, nekobox=246ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-68MS` (url=211ms, nekobox=240ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-57MS` (url=202ms, nekobox=225ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-63MS` (url=215ms, nekobox=236ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-59MS` (url=196ms, status=HTTP 204)
12. `AKUN-012-AIMALL-VLESS-WS-63MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-75MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-91MS` (url=209ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-73MS` (url=237ms, status=HTTP 204)
16. `AKUN-016-OVH-VLESS-WS-88MS` (url=199ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-110MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-75MS` (url=230ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-110MS` (url=206ms, status=HTTP 204)
20. `AKUN-020-OVH-VLESS-WS-148MS` (url=209ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-111MS` (url=229ms, status=HTTP 204)
22. `AKUN-022-3666888-VLESS-WS-165MS` (url=204ms, status=HTTP 204)
23. `AKUN-023-CMLIUSSSS-VLESS-WS-154MS` (url=225ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-91MS` (url=218ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-166MS` (url=250ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
