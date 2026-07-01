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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=225ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=212ms, nekobox=253ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-85MS` (url=250ms, nekobox=191ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-69MS`
5. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-67MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS`
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-75MS`
9. `AKUN-008-COMPREND-NET-VLESS-WS-76MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-75MS`
11. `AKUN-010-ADF-VLESS-WS-83MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-95MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-83MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-90MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-83MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-83MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-1PASSWORD-VLESS-WS-88MS` (url=212ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-95MS` (url=316ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-105MS` (url=238ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-74MS` (url=205ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-92MS` (url=219ms, status=HTTP 204)
22. `AKUN-022-COMPREND-NET-VLESS-WS-105MS` (url=226ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-182MS` (url=369ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-94MS` (url=265ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-358MS` (url=731ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
