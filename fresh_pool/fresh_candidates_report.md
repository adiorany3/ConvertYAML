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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=225ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=216ms, nekobox=190ms, status=no)
3. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=244ms, nekobox=190ms, status=no)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=251ms, nekobox=177ms, status=no)
6. `AKUN-003-GO-DADDY-COM-LLC-VLESS-WS-71MS`
7. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS`
8. `AKUN-005-CLOUDFLARE-VLESS-WS-97MS`
9. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-68MS`
10. `AKUN-007-CLOUDFLARE-VLESS-WS-123MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-87MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-120MS`
13. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-122MS`
14. `AKUN-014-UNKNOWN-VLESS-WS-99MS` (url=279ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-103MS` (url=227ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-180MS` (url=238ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-193MS` (url=396ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-362MS` (url=792ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-357MS` (url=770ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-393MS` (url=833ms, status=HTTP 204)
21. `AKUN-021-SPEEDTEST-VLESS-WS-388MS` (url=835ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-410MS` (url=859ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-399MS` (url=840ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-357MS` (url=763ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-680MS` (url=924ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
