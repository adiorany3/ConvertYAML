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
1. `AKUN-001-WPENG-VLESS-WS-59MS` (url=222ms, nekobox=242ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-55MS` (url=212ms, nekobox=238ms, status=yes)
3. `AKUN-003-WPENG-VLESS-WS-65MS` (url=225ms, nekobox=245ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-67MS` (url=215ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-61MS` (url=206ms, nekobox=236ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-63MS` (url=210ms, nekobox=239ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-66MS` (url=223ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-62MS` (url=221ms, nekobox=247ms, status=yes)
9. `AKUN-009-SSL-1134-VLESS-WS-87MS` (url=233ms, nekobox=241ms, status=yes)
10. `AKUN-010-WEYRO-NET-VLESS-WS-81MS` (url=229ms, nekobox=227ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-63MS` (url=209ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-84MS` (url=201ms, status=HTTP 204)
13. `AKUN-014-ZVC-VLESS-WS-75MS` (url=219ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-139MS` (url=228ms, status=HTTP 204)
15. `AKUN-017-SPEEDTEST-VLESS-WS-347MS` (url=737ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-357MS` (url=757ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-381MS` (url=815ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-396MS` (url=827ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-373MS` (url=779ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-348MS` (url=713ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-426MS` (url=901ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-375MS` (url=840ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-527MS` (url=950ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-248MS` (url=1087ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-664MS` (url=1067ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
