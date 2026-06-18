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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-74MS` (url=239ms, nekobox=270ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=279ms, nekobox=176ms, status=no)
3. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-81MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS` (url=273ms, nekobox=187ms, status=no)
5. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS`
6. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=240ms, nekobox=208ms, status=no)
8. `AKUN-005-1PASSWORD-VLESS-WS-98MS`
9. `AKUN-006-CLOUDFLARE-VLESS-WS-126MS`
10. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-134MS` (url=326ms, nekobox=185ms, status=no)
12. `AKUN-008-CLOUDFLARE-VLESS-WS-83MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-81MS` (url=260ms, nekobox=184ms, status=no)
14. `AKUN-009-CLOUDFLARE-VLESS-WS-101MS`
15. `AKUN-010-ADF-VLESS-WS-115MS`
16. `AKUN-016-CLOUDFLARE-VLESS-WS-84MS` (url=248ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-77MS` (url=246ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-258MS` (url=571ms, status=HTTP 204)
19. `AKUN-019-008500-VLESS-WS-89MS` (url=249ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-325MS` (url=2610ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-116MS` (url=245ms, status=HTTP 204)
22. `AKUN-022-RS-RAPIDSEEDBOX-20190717-VLESS-WS-289MS` (url=652ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-86MS` (url=241ms, status=HTTP 204)
24. `AKUN-024-JISON-VLESS-WS-401MS` (url=733ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-302MS` (url=650ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
