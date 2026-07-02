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
1. `AKUN-001-UNKNOWN-VLESS-WS-68MS` (url=215ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=235ms, nekobox=237ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-65MS` (url=213ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS` (url=224ms, nekobox=264ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-86MS` (url=197ms, nekobox=235ms, status=yes)
6. `AKUN-006-WPENG-VLESS-WS-71MS` (url=218ms, nekobox=238ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS` (url=205ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=213ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-84MS` (url=223ms, nekobox=239ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS` (url=223ms, nekobox=242ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-105MS` (url=215ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-113MS` (url=209ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-82MS` (url=206ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-96MS` (url=215ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-127MS` (url=203ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-88MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-95MS` (url=216ms, status=HTTP 204)
18. `AKUN-018-PAGES-VLESS-WS-117MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-120MS` (url=206ms, status=HTTP 204)
20. `AKUN-020-WPENG-VLESS-WS-69MS` (url=226ms, status=HTTP 204)
21. `AKUN-022-SPEEDTEST-VLESS-WS-246MS` (url=482ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-250MS` (url=548ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-253MS` (url=492ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-247MS` (url=498ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-256MS` (url=547ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
