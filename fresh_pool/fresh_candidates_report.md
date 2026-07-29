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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=216ms, nekobox=173ms, status=no)
2. `AKUN-001-UNKNOWN-VLESS-WS-67MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=209ms, nekobox=171ms, status=no)
5. `AKUN-006-CLOUDFLARE-VLESS-WS-74MS` (url=220ms, nekobox=171ms, status=no)
6. `AKUN-007-CLOUDFLARE-VLESS-WS-60MS` (url=218ms, nekobox=203ms, status=no)
7. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS`
8. `AKUN-004-UNKNOWN-VLESS-WS-78MS`
9. `AKUN-005-CLOUDFLARE-VLESS-WS-112MS`
10. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS`
11. `AKUN-007-CLOUDFLARE-VLESS-WS-109MS`
12. `AKUN-008-CLOUDFLARE-VLESS-WS-111MS`
13. `AKUN-009-BIGCOMMERCE-VLESS-WS-99MS`
14. `AKUN-016-CLOUDFLARE-VLESS-WS-79MS` (url=214ms, nekobox=177ms, status=no)
15. `AKUN-010-CLOUDFLARE-VLESS-WS-136MS`
16. `AKUN-018-CLOUDFLARE-VLESS-WS-84MS` (url=219ms, status=HTTP 204)
17. `AKUN-019-CMLIUSSSS-VLESS-WS-117MS` (url=231ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-156MS` (url=261ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-100MS` (url=211ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-106MS` (url=213ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-220MS` (url=478ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-234MS` (url=485ms, status=HTTP 204)
23. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-221MS` (url=503ms, status=HTTP 204)
24. `AKUN-031-CLOUDFLARE-VLESS-WS-453MS` (url=805ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-416MS` (url=689ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
