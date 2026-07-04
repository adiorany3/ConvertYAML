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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-86MS` (url=219ms, nekobox=233ms, status=yes)
2. `AKUN-002-466688-VLESS-WS-91MS` (url=211ms, nekobox=247ms, status=yes)
3. `AKUN-003-ALIBABA-VLESS-WS-89MS` (url=236ms, nekobox=237ms, status=yes)
4. `AKUN-004-TRANSIP-NL-AMS4-CUST-VLESS-WS-104MS` (url=223ms, nekobox=267ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS` (url=234ms, nekobox=237ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS` (url=209ms, nekobox=245ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-103MS` (url=217ms, nekobox=230ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-112MS` (url=227ms, nekobox=248ms, status=yes)
9. `AKUN-009-WPENG-VLESS-WS-104MS` (url=222ms, nekobox=238ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=208ms, nekobox=234ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-103MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-99MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-90MS` (url=210ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-100MS` (url=235ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-115MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-WEYRO-NET-VLESS-WS-107MS` (url=219ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-107MS` (url=228ms, status=HTTP 204)
18. `AKUN-018-WPENG-VLESS-WS-110MS` (url=213ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-104MS` (url=234ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-136MS` (url=231ms, status=HTTP 204)
21. `AKUN-021-466688-VLESS-WS-259MS` (url=368ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-359MS` (url=750ms, status=HTTP 204)
23. `AKUN-024-SPEEDTEST-VLESS-WS-375MS` (url=800ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-375MS` (url=794ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-399MS` (url=836ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
