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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-64MS` (url=201ms, nekobox=246ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-72MS` (url=200ms, nekobox=237ms, status=yes)
3. `AKUN-003-ORACLE-VLESS-WS-66MS` (url=212ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=218ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-116MS` (url=213ms, nekobox=252ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS` (url=201ms, nekobox=258ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-101MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-125MS`
9. `AKUN-010-CLOUDFLARE-VLESS-WS-159MS` (url=224ms, nekobox=7176ms, status=no)
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-75MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-86MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-130MS` (url=195ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-227MS` (url=489ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-275MS` (url=545ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-269MS` (url=556ms, status=HTTP 204)
16. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-262MS` (url=540ms, status=HTTP 204)
17. `AKUN-018-SPEEDTEST-VLESS-WS-273MS` (url=580ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-247MS` (url=495ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-257MS` (url=496ms, status=HTTP 204)
20. `AKUN-027-APPLESERAJ-VLESS-WS-451MS` (url=1234ms, status=HTTP 204)
21. `AKUN-028-UNKNOWN-VLESS-WS-467MS` (url=679ms, status=HTTP 204)
22. `AKUN-029-UNKNOWN-VLESS-WS-548MS` (url=4083ms, status=HTTP 204)
23. `AKUN-030-RS-RAPIDSEEDBOX-20190717-VLESS-WS-479MS` (url=5843ms, status=HTTP 204)
24. `AKUN-032-UNKNOWN-VLESS-WS-589MS` (url=882ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
