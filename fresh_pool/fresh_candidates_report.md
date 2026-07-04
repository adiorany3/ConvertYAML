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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=214ms, nekobox=252ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=232ms, nekobox=253ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=227ms, nekobox=261ms, status=yes)
4. `AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-79MS` (url=228ms, nekobox=248ms, status=yes)
5. `AKUN-005-WEYRO-NET-VLESS-WS-94MS` (url=236ms, nekobox=249ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-74MS` (url=214ms, nekobox=254ms, status=yes)
7. `AKUN-007-OVH-VLESS-WS-99MS` (url=211ms, nekobox=250ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-93MS` (url=203ms, nekobox=232ms, status=yes)
9. `AKUN-009-WPENG-VLESS-WS-95MS` (url=202ms, nekobox=260ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-91MS` (url=251ms, nekobox=233ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-98MS` (url=225ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-91MS` (url=232ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-143MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-130MS` (url=228ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-154MS` (url=224ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-118MS` (url=208ms, status=HTTP 204)
17. `AKUN-017-PAGES-VLESS-WS-108MS` (url=204ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-92MS` (url=217ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-130MS` (url=227ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-209MS` (url=359ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-247MS` (url=544ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-262MS` (url=558ms, status=HTTP 204)
23. `AKUN-023-SPEEDTEST-VLESS-WS-245MS` (url=510ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-257MS` (url=565ms, status=HTTP 204)
25. `AKUN-025-ADF-VLESS-WS-84MS` (url=232ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
