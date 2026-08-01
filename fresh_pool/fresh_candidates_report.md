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
1. `AKUN-001-UNKNOWN-VLESS-WS-53MS` (url=229ms, nekobox=237ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-56MS` (url=212ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-56MS` (url=209ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-57MS` (url=212ms, nekobox=237ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-67MS` (url=213ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS` (url=216ms, nekobox=239ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-57MS` (url=217ms, nekobox=248ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-65MS` (url=209ms, nekobox=241ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-57MS` (url=217ms, nekobox=245ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-120MS` (url=260ms, nekobox=260ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-67MS` (url=251ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-122MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-DE-CLOUDKLEYER-20190515-VLESS-WS-102MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-90MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-118MS` (url=324ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-129MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-107MS` (url=359ms, status=HTTP 204)
18. `AKUN-019-RMGYVPN-VLESS-WS-267MS` (url=564ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-584MS` (url=4398ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-605MS` (url=1014ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-680MS` (url=1132ms, status=HTTP 204)
22. `AKUN-029-CLOUDFLARE-VLESS-WS-638MS` (url=1037ms, status=HTTP 204)
23. `AKUN-032-UNKNOWN-VLESS-WS-792MS` (url=2412ms, status=HTTP 204)
24. `AKUN-033-CLOUDFLARE-VLESS-WS-789MS` (url=1697ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-800MS` (url=5301ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
