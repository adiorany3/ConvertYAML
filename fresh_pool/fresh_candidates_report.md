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
1. `AKUN-001-UNKNOWN-VLESS-WS-84MS` (url=274ms, nekobox=339ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-79MS` (url=276ms, nekobox=336ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=249ms, nekobox=289ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-102MS` (url=378ms, nekobox=346ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-107MS` (url=341ms, nekobox=318ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-137MS` (url=300ms, nekobox=214ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-107MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-120MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-114MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-105MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-182MS`
12. `AKUN-012-RMGYVPN-VLESS-WS-204MS` (url=370ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-207MS` (url=589ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-311MS` (url=597ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-440MS` (url=853ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-450MS` (url=892ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-100MS` (url=658ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-507MS` (url=782ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-479MS` (url=895ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-463MS` (url=812ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-565MS` (url=839ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-546MS` (url=888ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-557MS` (url=859ms, status=HTTP 204)
24. `AKUN-030-CLOUDFLARE-VLESS-WS-597MS` (url=943ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-642MS` (url=4214ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
