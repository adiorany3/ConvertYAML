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
1. `AKUN-001-UNKNOWN-VLESS-WS-70MS` (url=216ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=211ms, nekobox=239ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-74MS` (url=222ms, nekobox=254ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-79MS` (url=221ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS` (url=216ms, nekobox=237ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-74MS` (url=213ms, nekobox=240ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-83MS` (url=222ms, nekobox=253ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-84MS` (url=222ms, nekobox=245ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS` (url=218ms, nekobox=7173ms, status=no)
10. `AKUN-009-UNKNOWN-VLESS-WS-78MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-87MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-89MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-WEBEX-VLESS-WS-77MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-87MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-78MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-91MS` (url=204ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-83MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-102MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-73MS` (url=227ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-69MS` (url=231ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-117MS` (url=233ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-124MS` (url=227ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-96MS` (url=222ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-144MS` (url=234ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-142MS` (url=248ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
