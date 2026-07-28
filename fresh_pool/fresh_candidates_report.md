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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=226ms, nekobox=247ms, status=yes)
2. `AKUN-002-GOOGLE-VLESS-WS-72MS` (url=211ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=221ms, nekobox=229ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-95MS` (url=214ms, nekobox=252ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=211ms, nekobox=242ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-123MS` (url=214ms, nekobox=240ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-85MS` (url=222ms, nekobox=226ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-65MS` (url=198ms, nekobox=227ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-118MS` (url=218ms, nekobox=245ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-149MS` (url=425ms, nekobox=449ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-181MS` (url=300ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-193MS` (url=233ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-242MS` (url=498ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-218MS` (url=267ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-277MS` (url=586ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-288MS` (url=3975ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-268MS` (url=527ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-397MS` (url=663ms, status=HTTP 204)
19. `AKUN-021-SUKARIO-VLESS-WS-412MS` (url=713ms, status=HTTP 204)
20. `AKUN-025-UNKNOWN-VLESS-WS-513MS` (url=837ms, status=HTTP 204)
21. `AKUN-028-CLOUDFLARE-VLESS-WS-552MS` (url=1221ms, status=HTTP 204)
22. `AKUN-031-CLOUDFLARE-VLESS-WS-720MS` (url=1387ms, status=HTTP 204)
23. `AKUN-032-UNKNOWN-VLESS-WS-749MS` (url=1353ms, status=HTTP 204)
24. `AKUN-033-090227-VLESS-WS-245MS` (url=335ms, status=HTTP 204)
25. `AKUN-034-UNKNOWN-VLESS-WS-500MS` (url=1164ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
