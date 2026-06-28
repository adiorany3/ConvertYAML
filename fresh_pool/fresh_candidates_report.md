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
1. `AKUN-001-VULTR-VLESS-WS-71MS` (url=231ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=226ms, nekobox=255ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=203ms, nekobox=181ms, status=no)
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-102MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-122MS`
8. `AKUN-007-COMPREND-NET-VLESS-WS-106MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-121MS`
10. `AKUN-009-NETCRAFTERS-VLESS-WS-110MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-131MS` (url=214ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-232MS` (url=491ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-245MS` (url=496ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-277MS` (url=566ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-287MS` (url=613ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-85MS` (url=240ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-293MS` (url=582ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-273MS` (url=581ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-329MS` (url=542ms, status=HTTP 204)
21. `AKUN-022-CCTVHIKVISION-VLESS-WS-401MS` (url=703ms, status=HTTP 204)
22. `AKUN-026-RAVINOZ-VLESS-WS-431MS` (url=790ms, status=HTTP 204)
23. `AKUN-030-IETF-VLESS-WS-492MS` (url=815ms, status=HTTP 204)
24. `AKUN-031-RS-RAPIDSEEDBOX-20190717-VLESS-WS-510MS` (url=907ms, status=HTTP 204)
25. `AKUN-032-UNKNOWN-VLESS-WS-233MS` (url=502ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
