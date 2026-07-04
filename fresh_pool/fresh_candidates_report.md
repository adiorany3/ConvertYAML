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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=209ms, nekobox=252ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=212ms, nekobox=233ms, status=yes)
3. `AKUN-003-WEYRO-NET-VLESS-WS-85MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-79MS`
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS`
7. `AKUN-007-ZVC-VLESS-WS-94MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-83MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-62MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-117MS`
11. `AKUN-012-UNKNOWN-VLESS-WS-97MS` (url=206ms, status=HTTP 204)
12. `AKUN-013-UNKNOWN-VLESS-WS-94MS` (url=203ms, status=HTTP 204)
13. `AKUN-014-WEBEX-VLESS-WS-88MS` (url=222ms, status=HTTP 204)
14. `AKUN-015-466688-VLESS-WS-72MS` (url=213ms, status=HTTP 204)
15. `AKUN-016-WEYRO-NET-VLESS-WS-90MS` (url=250ms, status=HTTP 204)
16. `AKUN-017-WEBEX-VLESS-WS-110MS` (url=216ms, status=HTTP 204)
17. `AKUN-018-DEV-VLESS-WS-176MS` (url=380ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-224MS` (url=493ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-230MS` (url=503ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-239MS` (url=529ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-244MS` (url=559ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-244MS` (url=346ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-247MS` (url=531ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-251MS` (url=537ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-231MS` (url=569ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
