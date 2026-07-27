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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=230ms, nekobox=268ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=264ms, nekobox=170ms, status=no)
3. `AKUN-002-UNKNOWN-VLESS-WS-68MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-69MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-62MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-61MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-63MS`
9. `AKUN-008-008500-VLESS-WS-65MS`
10. `AKUN-009-DEV-VLESS-WS-72MS`
11. `AKUN-011-UNKNOWN-VLESS-WS-63MS` (url=218ms, nekobox=7173ms, status=no)
12. `AKUN-010-UNKNOWN-VLESS-WS-91MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-85MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-104MS` (url=228ms, status=HTTP 204)
15. `AKUN-015-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-117MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-75MS` (url=282ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-100MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-76MS` (url=245ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-83MS` (url=240ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-116MS` (url=231ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-65MS` (url=227ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-92MS` (url=221ms, status=HTTP 204)
23. `AKUN-023-ZVC-VLESS-WS-70MS` (url=278ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-85MS` (url=232ms, status=HTTP 204)
25. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-127MS` (url=298ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
