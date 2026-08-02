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
1. `AKUN-001-ZVC-VLESS-WS-55MS` (url=217ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-57MS` (url=212ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-62MS` (url=211ms, nekobox=250ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-69MS` (url=226ms, nekobox=170ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-90MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-117MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-73MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-76MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-74MS` (url=198ms, nekobox=171ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-69MS`
12. `AKUN-010-UNKNOWN-VLESS-WS-108MS`
13. `AKUN-014-UNKNOWN-VLESS-WS-61MS` (url=337ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-308MS` (url=625ms, status=HTTP 204)
15. `AKUN-016-LT-LRTC-20060503-VLESS-WS-379MS` (url=737ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-515MS` (url=659ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-643MS` (url=1307ms, status=HTTP 204)
18. `AKUN-021-UNKNOWN-VLESS-WS-614MS` (url=1019ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-649MS` (url=1081ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-638MS` (url=893ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-656MS` (url=962ms, status=HTTP 204)
22. `AKUN-025-AE-ORYXLABS-20081128-VLESS-WS-688MS` (url=1055ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-713MS` (url=1579ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-708MS` (url=1208ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-680MS` (url=771ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
