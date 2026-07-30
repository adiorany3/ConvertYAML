# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-UNKNOWN-VLESS-WS-68MS` (url=224ms, nekobox=243ms, status=yes)
2. `AKUN-002-ICOOK-VLESS-WS-71MS` (url=218ms, nekobox=230ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=206ms, nekobox=249ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-90MS` (url=227ms, nekobox=229ms, status=yes)
5. `AKUN-005-LEVIKOGJGFDD-VLESS-WS-76MS` (url=231ms, nekobox=257ms, status=yes)
6. `AKUN-006-SPEEDTEST-VLESS-WS-77MS` (url=231ms, nekobox=182ms, status=no)
7. `AKUN-006-UNKNOWN-VLESS-WS-80MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-140MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-143MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-91MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-94MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-139MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-140MS` (url=262ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-131MS` (url=249ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-136MS` (url=356ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-137MS` (url=389ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-120MS` (url=374ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-166MS` (url=204ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-367MS` (url=734ms, status=HTTP 204)
20. `AKUN-023-ECCIM-VLESS-WS-452MS` (url=878ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-459MS` (url=955ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-609MS` (url=1220ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-627MS` (url=1044ms, status=HTTP 204)
24. `AKUN-032-UNKNOWN-VLESS-WS-792MS` (url=1367ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
