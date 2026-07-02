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
1. `AKUN-001-ORACLE-VLESS-WS-59MS` (url=216ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=218ms, nekobox=227ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS` (url=218ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS` (url=226ms, nekobox=239ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-62MS` (url=216ms, nekobox=239ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-64MS` (url=221ms, nekobox=251ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-67MS` (url=212ms, nekobox=237ms, status=yes)
8. `AKUN-008-OVH-VLESS-WS-76MS` (url=227ms, nekobox=244ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-76MS` (url=227ms, nekobox=229ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-78MS` (url=215ms, nekobox=252ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-84MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-89MS` (url=198ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-83MS` (url=198ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-97MS` (url=213ms, status=HTTP 204)
15. `AKUN-016-WPENG-VLESS-WS-67MS` (url=224ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-82MS` (url=208ms, status=HTTP 204)
17. `AKUN-018-WEYRO-NET-VLESS-WS-112MS` (url=224ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-73MS` (url=223ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-130MS` (url=241ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-246MS` (url=3669ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-359MS` (url=744ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-365MS` (url=768ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-348MS` (url=732ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-379MS` (url=846ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-400MS` (url=820ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
