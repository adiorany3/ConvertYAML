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
1. `AKUN-001-UNKNOWN-VLESS-WS-58MS` (url=217ms, nekobox=226ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=202ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=234ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=203ms, nekobox=248ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=209ms, nekobox=250ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-72MS` (url=204ms, nekobox=234ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS` (url=213ms, nekobox=177ms, status=no)
8. `AKUN-007-ZVC-VLESS-WS-86MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-83MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-86MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-101MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=206ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-76MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-102MS` (url=228ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-68MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-CMLIUSSSS-VLESS-WS-119MS` (url=203ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-125MS` (url=218ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-92MS` (url=217ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-130MS` (url=231ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-111MS` (url=229ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-98MS` (url=221ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-121MS` (url=221ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-86MS` (url=218ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-146MS` (url=334ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
