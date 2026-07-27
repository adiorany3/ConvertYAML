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
1. `AKUN-001-UNKNOWN-VLESS-WS-62MS` (url=232ms, nekobox=252ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=229ms, nekobox=269ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-63MS` (url=226ms, nekobox=251ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-72MS` (url=228ms, nekobox=271ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-68MS` (url=246ms, nekobox=268ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-63MS` (url=231ms, nekobox=260ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS` (url=247ms, nekobox=267ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-63MS` (url=236ms, nekobox=260ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-78MS` (url=224ms, nekobox=254ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS` (url=239ms, nekobox=248ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-91MS` (url=238ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-92MS` (url=275ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-81MS` (url=281ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-107MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-63MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-111MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-160MS` (url=318ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-145MS` (url=364ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-158MS` (url=310ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-235MS` (url=863ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-246MS` (url=546ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-249MS` (url=557ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-220MS` (url=423ms, status=HTTP 204)
24. `AKUN-024-LEVIKOGJGFDD-VLESS-WS-276MS` (url=3544ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-75MS` (url=218ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
