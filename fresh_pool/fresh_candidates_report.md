# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-75MS` (url=259ms, nekobox=274ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=227ms, nekobox=296ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=251ms, nekobox=264ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=235ms, nekobox=255ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS` (url=260ms, nekobox=278ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=233ms, nekobox=276ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS` (url=323ms, nekobox=308ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-108MS` (url=254ms, nekobox=260ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-133MS` (url=261ms, nekobox=274ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-109MS` (url=277ms, nekobox=180ms, status=no)
11. `AKUN-010-COMPREND-NET-VLESS-WS-97MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-282MS` (url=616ms, status=HTTP 204)
13. `AKUN-014-SPEEDTEST-VLESS-WS-306MS` (url=677ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-311MS` (url=631ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-303MS` (url=653ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-270MS` (url=583ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-288MS` (url=681ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-279MS` (url=581ms, status=HTTP 204)
19. `AKUN-021-466688-VLESS-WS-106MS` (url=251ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-477MS` (url=776ms, status=HTTP 204)
21. `AKUN-028-RC-PRO-5-VLESS-WS-533MS` (url=919ms, status=HTTP 204)
22. `AKUN-029-CLOUDFLARE-VLESS-WS-548MS` (url=1145ms, status=HTTP 204)
23. `AKUN-032-UNKNOWN-VLESS-WS-573MS` (url=772ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-597MS` (url=888ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
