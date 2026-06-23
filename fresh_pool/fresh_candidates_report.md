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
1. `AKUN-001-UNKNOWN-VLESS-WS-62MS` (url=209ms, nekobox=243ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-57MS` (url=214ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS` (url=225ms, nekobox=252ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-93MS` (url=213ms, nekobox=180ms, status=no)
5. `AKUN-004-BROADNNET-KR-VLESS-WS-94MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-99MS`
7. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-69MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-87MS` (url=209ms, nekobox=179ms, status=no)
9. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-105MS`
10. `AKUN-010-DEV-VLESS-WS-77MS` (url=204ms, nekobox=181ms, status=no)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-85MS` (url=210ms, nekobox=185ms, status=no)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-125MS` (url=198ms, nekobox=185ms, status=no)
13. `AKUN-008-CLOUDFLARE-VLESS-WS-94MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-77MS` (url=198ms, nekobox=185ms, status=no)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-88MS` (url=208ms, nekobox=179ms, status=no)
16. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS`
17. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS`
18. `AKUN-018-CLOUDFLARE-VLESS-WS-68MS` (url=200ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-400MS` (url=870ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-355MS` (url=797ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-357MS` (url=816ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-389MS` (url=797ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-350MS` (url=719ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-411MS` (url=848ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-657MS` (url=1948ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
