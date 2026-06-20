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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-61MS` (url=225ms, nekobox=240ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-67MS` (url=207ms, nekobox=251ms, status=yes)
3. `AKUN-003-VULTR-VLESS-WS-72MS` (url=212ms, nekobox=239ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-67MS` (url=217ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS` (url=225ms, nekobox=250ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=202ms, nekobox=256ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-115MS` (url=222ms, nekobox=261ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=222ms, nekobox=7177ms, status=no)
9. `AKUN-008-VULTR-VLESS-WS-120MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-69MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-72MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-73MS` (url=234ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-361MS` (url=736ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-349MS` (url=745ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-404MS` (url=804ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-77MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-422MS` (url=848ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-403MS` (url=894ms, status=HTTP 204)
19. `AKUN-021-BROADNNET-KR-VLESS-WS-695MS` (url=816ms, status=HTTP 204)
20. `AKUN-027-CONFLU-VLESS-WS-381MS` (url=762ms, status=HTTP 204)
21. `AKUN-028-CLOUDFLARE-VLESS-WS-422MS` (url=878ms, status=HTTP 204)
22. `AKUN-032-CLOUDFLARE-VLESS-WS-784MS` (url=1356ms, status=HTTP 204)
23. `AKUN-034-CLOUDFLARE-VLESS-WS-737MS` (url=4294ms, status=HTTP 204)
24. `AKUN-035-CLOUDFLARE-VLESS-WS-877MS` (url=2844ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
