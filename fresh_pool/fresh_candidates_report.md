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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-76MS` (url=251ms, nekobox=268ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-88MS` (url=321ms, nekobox=317ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS` (url=249ms, nekobox=273ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=250ms, nekobox=288ms, status=yes)
5. `AKUN-005-GOV-VLESS-WS-84MS` (url=257ms, nekobox=267ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS` (url=297ms, nekobox=303ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS` (url=237ms, nekobox=264ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=251ms, nekobox=285ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-101MS` (url=284ms, nekobox=267ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-115MS` (url=258ms, nekobox=331ms, status=yes)
11. `AKUN-013-CONFLU-VLESS-WS-274MS` (url=569ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-334MS` (url=645ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-299MS` (url=3569ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-314MS` (url=650ms, status=HTTP 204)
15. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-345MS` (url=640ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-323MS` (url=2196ms, status=HTTP 204)
17. `AKUN-019-CLUTCHPROTOCOL-VLESS-WS-310MS` (url=2600ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-336MS` (url=644ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-395MS` (url=728ms, status=HTTP 204)
20. `AKUN-023-JISON-VLESS-WS-412MS` (url=878ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-436MS` (url=669ms, status=HTTP 204)
22. `AKUN-027-JISON-VLESS-WS-409MS` (url=746ms, status=HTTP 204)
23. `AKUN-029-CLOUDFLARE-VLESS-WS-490MS` (url=681ms, status=HTTP 204)
24. `AKUN-030-CLOUDFLARE-VLESS-WS-439MS` (url=647ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-447MS` (url=643ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
