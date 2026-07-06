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
1. `AKUN-001-ZVC-VLESS-WS-60MS` (url=234ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=241ms, nekobox=275ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=293ms, nekobox=177ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS`
6. `AKUN-005-OVH-VLESS-WS-66MS`
7. `AKUN-006-INTERNETWORKS-45-131-208-VLESS-WS-69MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS`
10. `AKUN-009-WEBEX-VLESS-WS-74MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-95MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-79MS` (url=250ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-81MS` (url=235ms, status=HTTP 204)
14. `AKUN-014-WEBEX-VLESS-WS-69MS` (url=245ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-85MS` (url=245ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-73MS` (url=259ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-74MS` (url=239ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-122MS` (url=251ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-81MS` (url=243ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-86MS` (url=247ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-162MS` (url=249ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-79MS` (url=246ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-255MS` (url=552ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-252MS` (url=554ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-272MS` (url=598ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
