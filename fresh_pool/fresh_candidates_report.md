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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=265ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=230ms, nekobox=289ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-62MS` (url=222ms, nekobox=254ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-63MS` (url=218ms, nekobox=252ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-68MS` (url=2469ms, nekobox=267ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-75MS` (url=247ms, nekobox=341ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-75MS` (url=234ms, nekobox=259ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-73MS` (url=264ms, nekobox=297ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-82MS` (url=281ms, nekobox=347ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-76MS` (url=268ms, nekobox=260ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-87MS` (url=260ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-64MS` (url=232ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-115MS` (url=335ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-131MS` (url=333ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-63MS` (url=275ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-135MS` (url=243ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-172MS` (url=319ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-230MS` (url=443ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-258MS` (url=583ms, status=HTTP 204)
20. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-267MS` (url=3128ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-224MS` (url=449ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-290MS` (url=580ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-323MS` (url=797ms, status=HTTP 204)
24. `AKUN-027-SUKARIO-VLESS-WS-541MS` (url=751ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-572MS` (url=937ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
