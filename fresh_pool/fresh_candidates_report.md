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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-55MS` (url=209ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-57MS` (url=212ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=221ms, nekobox=243ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-57MS` (url=210ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-61MS` (url=229ms, nekobox=171ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-58MS`
8. `AKUN-007-ZVC-VLESS-WS-71MS`
9. `AKUN-008-CCWU-VLESS-WS-67MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-101MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-76MS`
12. `AKUN-013-DEV-VLESS-WS-72MS` (url=850ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-76MS` (url=213ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-137MS` (url=221ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-328MS` (url=743ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-341MS` (url=759ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-334MS` (url=4562ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-341MS` (url=966ms, status=HTTP 204)
19. `AKUN-024-CLOUDFLARE-VLESS-WS-535MS` (url=663ms, status=HTTP 204)
20. `AKUN-025-CLOUDFLARE-VLESS-WS-628MS` (url=3403ms, status=HTTP 204)
21. `AKUN-031-CLOUDFLARE-VLESS-WS-856MS` (url=1815ms, status=HTTP 204)
22. `AKUN-032-CLOUDFLARE-VLESS-WS-850MS` (url=1753ms, status=HTTP 204)
23. `AKUN-033-CLOUDFLARE-VLESS-WS-867MS` (url=1794ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-858MS` (url=1797ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
