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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=212ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=220ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS` (url=223ms, nekobox=245ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-76MS` (url=204ms, nekobox=236ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-76MS` (url=225ms, nekobox=228ms, status=yes)
6. `AKUN-006-WPENG-VLESS-WS-79MS` (url=209ms, nekobox=226ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-74MS` (url=210ms, nekobox=248ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS` (url=200ms, nekobox=247ms, status=yes)
9. `AKUN-009-WEYRO-NET-VLESS-WS-91MS` (url=220ms, nekobox=263ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-87MS` (url=216ms, nekobox=257ms, status=yes)
11. `AKUN-011-VDSINA-VLESS-WS-90MS` (url=228ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-84MS` (url=200ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-83MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-74MS` (url=213ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-86MS` (url=219ms, status=HTTP 204)
16. `AKUN-016-ADF-VLESS-WS-77MS` (url=227ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-84MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-118MS` (url=210ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-129MS` (url=202ms, status=HTTP 204)
20. `AKUN-020-PAGES-VLESS-WS-79MS` (url=261ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-83MS` (url=211ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-223MS` (url=492ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-236MS` (url=481ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-247MS` (url=606ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-244MS` (url=537ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
