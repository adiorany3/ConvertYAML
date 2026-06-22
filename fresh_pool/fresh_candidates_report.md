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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=275ms, nekobox=252ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-73MS` (url=220ms, nekobox=260ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-81MS` (url=201ms, nekobox=257ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-85MS` (url=226ms, nekobox=234ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS` (url=222ms, nekobox=251ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS` (url=224ms, nekobox=250ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS` (url=222ms, nekobox=252ms, status=yes)
8. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-82MS` (url=223ms, nekobox=246ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS` (url=231ms, nekobox=255ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-91MS` (url=226ms, nekobox=259ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-75MS` (url=212ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-79MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-90MS` (url=203ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-367MS` (url=774ms, status=HTTP 204)
15. `AKUN-015-WPENG-VLESS-WS-380MS` (url=806ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-366MS` (url=759ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-400MS` (url=893ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-360MS` (url=747ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-395MS` (url=861ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-384MS` (url=855ms, status=HTTP 204)
21. `AKUN-025-UNKNOWN-VLESS-WS-716MS` (url=982ms, status=HTTP 204)
22. `AKUN-027-UNKNOWN-VLESS-WS-730MS` (url=1221ms, status=HTTP 204)
23. `AKUN-028-RS-RAPIDSEEDBOX-20190717-VLESS-WS-753MS` (url=1189ms, status=HTTP 204)
24. `AKUN-030-UNKNOWN-VLESS-WS-805MS` (url=1263ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-826MS` (url=1201ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
