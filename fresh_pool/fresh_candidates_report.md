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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=205ms, nekobox=242ms, status=yes)
2. `AKUN-002-SPEEDTEST-VLESS-WS-70MS` (url=228ms, nekobox=222ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-72MS` (url=205ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS` (url=213ms, nekobox=235ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS` (url=217ms, nekobox=254ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-90MS` (url=214ms, nekobox=263ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-67MS` (url=218ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-72MS` (url=213ms, nekobox=251ms, status=yes)
9. `AKUN-009-SPEEDTEST-VLESS-WS-74MS` (url=210ms, nekobox=170ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-104MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-72MS` (url=207ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-89MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-70MS` (url=202ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-83MS` (url=228ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-108MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-95MS` (url=207ms, status=HTTP 204)
18. `AKUN-018-MEDIUM-VLESS-WS-76MS` (url=198ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-114MS` (url=205ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-62MS` (url=213ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-130MS` (url=203ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-65MS` (url=319ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-108MS` (url=230ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-146MS` (url=211ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-155MS` (url=1028ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
