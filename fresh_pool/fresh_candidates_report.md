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
1. `AKUN-001-IPXO-VLESS-WS-57MS` (url=218ms, nekobox=240ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-56MS` (url=221ms, nekobox=258ms, status=yes)
3. `AKUN-003-OVH-VLESS-WS-57MS` (url=237ms, nekobox=241ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-59MS` (url=225ms, nekobox=172ms, status=no)
5. `AKUN-004-GOOGLE-VLESS-WS-56MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-61MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-85MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-87MS`
10. `AKUN-010-SPEEDTEST-VLESS-WS-81MS` (url=229ms, nekobox=170ms, status=no)
11. `AKUN-009-UNKNOWN-VLESS-WS-60MS`
12. `AKUN-010-EU-VLESS-WS-103MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-113MS` (url=237ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-58MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-83MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-008500-VLESS-WS-63MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-67MS` (url=224ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-80MS` (url=215ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-101MS` (url=230ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-66MS` (url=233ms, status=HTTP 204)
21. `AKUN-021-ZVC-VLESS-WS-56MS` (url=223ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-109MS` (url=227ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-167MS` (url=386ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-207MS` (url=364ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-336MS` (url=686ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
