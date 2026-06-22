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
1. `AKUN-001-UNKNOWN-VLESS-WS-141MS` (url=287ms, nekobox=323ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-152MS` (url=284ms, nekobox=306ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-153MS` (url=277ms, nekobox=312ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-138MS` (url=286ms, nekobox=320ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-158MS` (url=287ms, nekobox=329ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-140MS` (url=268ms, nekobox=306ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-167MS` (url=371ms, nekobox=303ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-166MS` (url=276ms, nekobox=336ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-168MS` (url=264ms, nekobox=337ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-154MS` (url=274ms, nekobox=302ms, status=yes)
11. `AKUN-012-CLOUDFLARE-VLESS-WS-168MS` (url=293ms, status=HTTP 204)
12. `AKUN-013-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-139MS` (url=279ms, status=HTTP 204)
13. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-189MS` (url=294ms, status=HTTP 204)
14. `AKUN-015-SPEEDTEST-VLESS-WS-320MS` (url=457ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-365MS` (url=1787ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-386MS` (url=796ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-391MS` (url=787ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-394MS` (url=785ms, status=HTTP 204)
19. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-383MS` (url=771ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-376MS` (url=721ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-388MS` (url=5171ms, status=HTTP 204)
22. `AKUN-031-RS-RAPIDSEEDBOX-20190717-VLESS-WS-668MS` (url=888ms, status=HTTP 204)
23. `AKUN-032-RS-RAPIDSEEDBOX-20190717-VLESS-WS-788MS` (url=2281ms, status=HTTP 204)
24. `AKUN-034-RS-RAPIDSEEDBOX-20190717-VLESS-WS-629MS` (url=1071ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
