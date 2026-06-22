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
1. `AKUN-001-090227-VLESS-WS-59MS` (url=230ms, nekobox=249ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-64MS` (url=238ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=214ms, nekobox=260ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-79MS` (url=234ms, nekobox=180ms, status=no)
5. `AKUN-005-UNKNOWN-VLESS-WS-95MS` (url=218ms, nekobox=7182ms, status=no)
6. `AKUN-006-SPEEDTEST-VLESS-WS-101MS` (url=233ms, nekobox=170ms, status=no)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-109MS` (url=223ms, nekobox=7177ms, status=no)
8. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS`
9. `AKUN-005-CLOUDFLARE-VLESS-WS-127MS`
10. `AKUN-006-CLOUDWEBMANAGE-EU-FR-VLESS-WS-88MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-81MS` (url=217ms, nekobox=176ms, status=no)
12. `AKUN-007-CLOUDFLARE-VLESS-WS-85MS`
13. `AKUN-008-UNKNOWN-VLESS-WS-84MS`
14. `AKUN-009-CLOUDFLARE-VLESS-WS-87MS`
15. `AKUN-010-SPEEDTEST-VLESS-WS-390MS`
16. `AKUN-016-UNKNOWN-VLESS-WS-382MS` (url=823ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-396MS` (url=837ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-386MS` (url=733ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-393MS` (url=836ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-380MS` (url=771ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-103MS` (url=233ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-395MS` (url=805ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-660MS` (url=1002ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-817MS` (url=1239ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-878MS` (url=1341ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
