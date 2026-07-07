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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=253ms, nekobox=270ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-64MS` (url=233ms, nekobox=267ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-64MS` (url=268ms, nekobox=263ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-65MS` (url=248ms, nekobox=271ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-68MS` (url=247ms, nekobox=295ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-77MS` (url=241ms, nekobox=282ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-80MS` (url=241ms, nekobox=283ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-78MS` (url=238ms, nekobox=282ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-71MS` (url=241ms, nekobox=258ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-71MS` (url=238ms, nekobox=260ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-83MS` (url=220ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-84MS` (url=239ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-76MS` (url=294ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-93MS` (url=257ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-132MS` (url=258ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-140MS` (url=255ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-70MS` (url=243ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-142MS` (url=252ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-76MS` (url=228ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-108MS` (url=242ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-260MS` (url=559ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-268MS` (url=601ms, status=HTTP 204)
23. `AKUN-023-WPENG-VLESS-WS-299MS` (url=633ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-258MS` (url=605ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-212MS` (url=385ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
