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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-55MS` (url=218ms, nekobox=235ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=221ms, nekobox=240ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-85MS` (url=223ms, nekobox=243ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS` (url=1133ms, nekobox=943ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-69MS` (url=213ms, nekobox=237ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-74MS` (url=219ms, nekobox=237ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-68MS` (url=221ms, nekobox=245ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS` (url=202ms, nekobox=177ms, status=no)
9. `AKUN-008-UNKNOWN-VLESS-WS-81MS`
10. `AKUN-009-008500-VLESS-WS-87MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-89MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-111MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-86MS` (url=221ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-107MS` (url=227ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-129MS` (url=214ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-85MS` (url=230ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-91MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-94MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-65MS` (url=209ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-63MS` (url=224ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-118MS` (url=222ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-77MS` (url=213ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-86MS` (url=224ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-115MS` (url=234ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-337MS` (url=763ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
