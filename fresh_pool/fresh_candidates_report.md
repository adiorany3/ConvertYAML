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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=200ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-67MS` (url=217ms, nekobox=247ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS` (url=202ms, nekobox=183ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-81MS`
5. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-86MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-72MS`
8. `AKUN-007-VULTR-VLESS-WS-106MS`
9. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-91MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS` (url=190ms, nekobox=185ms, status=no)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-101MS` (url=204ms, nekobox=189ms, status=no)
12. `AKUN-009-CLOUDFLARE-VLESS-WS-98MS`
13. `AKUN-010-UNKNOWN-VLESS-WS-357MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-353MS` (url=790ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-401MS` (url=830ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-383MS` (url=804ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-390MS` (url=832ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-382MS` (url=844ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-359MS` (url=740ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-635MS` (url=888ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-605MS` (url=882ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-666MS` (url=817ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-659MS` (url=868ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-728MS` (url=1121ms, status=HTTP 204)
25. `AKUN-033-UNKNOWN-VLESS-WS-831MS` (url=1309ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
