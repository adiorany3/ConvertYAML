# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-UNKNOWN-VLESS-WS-81MS` (url=416ms, nekobox=349ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-88MS` (url=356ms, nekobox=310ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-101MS` (url=314ms, nekobox=340ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-91MS` (url=351ms, nekobox=346ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-111MS` (url=324ms, nekobox=378ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-92MS` (url=369ms, nekobox=300ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-95MS` (url=294ms, nekobox=319ms, status=yes)
8. `AKUN-008-SPEEDTEST-VLESS-WS-115MS` (url=349ms, nekobox=187ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-141MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-141MS` (url=349ms, nekobox=350ms, status=yes)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-193MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-225MS` (url=411ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-337MS` (url=686ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-434MS` (url=762ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-444MS` (url=1105ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-485MS` (url=837ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-535MS` (url=931ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-567MS` (url=968ms, status=HTTP 204)
19. `AKUN-026-CLOUDFLARE-VLESS-WS-599MS` (url=1119ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-587MS` (url=1066ms, status=HTTP 204)
21. `AKUN-033-CLOUDFLARE-VLESS-WS-615MS` (url=1001ms, status=HTTP 204)
22. `AKUN-034-CLOUDFLARE-VLESS-WS-643MS` (url=2103ms, status=HTTP 204)
23. `AKUN-035-CLOUDFLARE-VLESS-WS-850MS` (url=4774ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
