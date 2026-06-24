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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=233ms, nekobox=231ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-73MS` (url=216ms, nekobox=253ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-88MS` (url=203ms, nekobox=249ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-80MS` (url=246ms, nekobox=254ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-110MS` (url=204ms, nekobox=253ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-107MS` (url=208ms, nekobox=225ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS` (url=258ms, nekobox=243ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-131MS` (url=220ms, nekobox=253ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-107MS` (url=206ms, nekobox=202ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-135MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-368MS`
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-400MS` (url=861ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-408MS` (url=803ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-399MS` (url=846ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-423MS` (url=880ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-66MS` (url=427ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-351MS` (url=758ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-375MS` (url=776ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-304MS` (url=1019ms, status=HTTP 204)
20. `AKUN-029-UNKNOWN-VLESS-WS-764MS` (url=1671ms, status=HTTP 204)
21. `AKUN-030-HCAPTCHA-VLESS-WS-757MS` (url=880ms, status=HTTP 204)
22. `AKUN-031-UNKNOWN-VLESS-WS-683MS` (url=1997ms, status=HTTP 204)
23. `AKUN-032-CLOUDFLARE-VLESS-WS-798MS` (url=1565ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-879MS` (url=4347ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-860MS` (url=2656ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
