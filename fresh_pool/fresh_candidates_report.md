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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=216ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=203ms, nekobox=229ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=1935ms, nekobox=231ms, status=yes)
4. `AKUN-004-AIMALL-VLESS-WS-72MS` (url=206ms, nekobox=239ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-75MS` (url=313ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=203ms, nekobox=258ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-77MS` (url=199ms, nekobox=240ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-70MS` (url=199ms, nekobox=232ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-72MS` (url=202ms, nekobox=234ms, status=yes)
10. `AKUN-010-SAVVY-7-VLESS-WS-87MS` (url=210ms, nekobox=242ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-102MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-89MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-106MS` (url=209ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-92MS` (url=206ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-124MS` (url=206ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-72MS` (url=209ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-93MS` (url=212ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-116MS` (url=199ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-82MS` (url=213ms, status=HTTP 204)
20. `AKUN-020-466688-VLESS-WS-75MS` (url=217ms, status=HTTP 204)
21. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-221MS` (url=518ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-227MS` (url=503ms, status=HTTP 204)
23. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-250MS` (url=1325ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-226MS` (url=558ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-207MS` (url=347ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
