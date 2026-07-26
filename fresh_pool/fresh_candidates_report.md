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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-83MS` (url=230ms, nekobox=225ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-82MS` (url=205ms, nekobox=230ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=198ms, nekobox=229ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-85MS` (url=200ms, nekobox=226ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-85MS` (url=209ms, nekobox=259ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS` (url=204ms, nekobox=235ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=203ms, nekobox=229ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS` (url=230ms, nekobox=242ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-99MS` (url=206ms, nekobox=229ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-101MS` (url=217ms, nekobox=228ms, status=yes)
11. `AKUN-011-ZOOM-VLESS-WS-91MS` (url=210ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-97MS` (url=217ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-90MS` (url=232ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-115MS` (url=206ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-124MS` (url=202ms, status=HTTP 204)
16. `AKUN-017-SKK-VLESS-WS-120MS` (url=249ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-129MS` (url=201ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-139MS` (url=238ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-83MS` (url=199ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-90MS` (url=200ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-99MS` (url=198ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-91MS` (url=208ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-374MS` (url=749ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-91MS` (url=232ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-684MS` (url=1136ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
