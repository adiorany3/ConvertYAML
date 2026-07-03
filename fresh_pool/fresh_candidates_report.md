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
1. `AKUN-001-VULTR-VLESS-WS-70MS` (url=226ms, nekobox=258ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=227ms, nekobox=296ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=262ms, nekobox=269ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS` (url=235ms, nekobox=252ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-79MS` (url=323ms, nekobox=268ms, status=yes)
6. `AKUN-006-WPENG-VLESS-WS-67MS` (url=262ms, nekobox=279ms, status=yes)
7. `AKUN-007-466688-VLESS-WS-79MS` (url=246ms, nekobox=276ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-85MS` (url=282ms, nekobox=274ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-93MS` (url=253ms, nekobox=293ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-78MS` (url=236ms, nekobox=296ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-93MS` (url=252ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-81MS` (url=241ms, status=HTTP 204)
13. `AKUN-013-UK-GB-DCL-01-20191003-VLESS-WS-83MS` (url=286ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-85MS` (url=246ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-98MS` (url=268ms, status=HTTP 204)
16. `AKUN-016-WEYRO-NET-VLESS-WS-109MS` (url=257ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-92MS` (url=239ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-144MS` (url=259ms, status=HTTP 204)
19. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS` (url=235ms, status=HTTP 204)
20. `AKUN-020-COMPREND-NET-VLESS-WS-150MS` (url=247ms, status=HTTP 204)
21. `AKUN-021-ZVC-VLESS-WS-90MS` (url=259ms, status=HTTP 204)
22. `AKUN-022-COMPREND-NET-VLESS-WS-70MS` (url=230ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-158MS` (url=314ms, status=HTTP 204)
24. `AKUN-024-COMPREND-NET-VLESS-WS-122MS` (url=289ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-277MS` (url=582ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
