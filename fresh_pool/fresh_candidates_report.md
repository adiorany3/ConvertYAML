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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-99MS` (url=230ms, nekobox=240ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-102MS` (url=230ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-102MS` (url=207ms, nekobox=202ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-97MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-101MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS` (url=216ms, nekobox=215ms, status=no)
7. `AKUN-005-UNKNOWN-VLESS-WS-111MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-109MS` (url=217ms, nekobox=212ms, status=no)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS` (url=227ms, nekobox=205ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-107MS` (url=217ms, nekobox=200ms, status=no)
11. `AKUN-006-CLOUDFLARE-VLESS-WS-127MS`
12. `AKUN-007-UNKNOWN-VLESS-WS-109MS`
13. `AKUN-008-UNKNOWN-VLESS-WS-113MS`
14. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-119MS`
15. `AKUN-015-UNKNOWN-VLESS-WS-140MS` (url=256ms, nekobox=205ms, status=no)
16. `AKUN-010-UNKNOWN-VLESS-WS-149MS`
17. `AKUN-017-UNKNOWN-VLESS-WS-151MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-169MS` (url=212ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-141MS` (url=219ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-165MS` (url=223ms, status=HTTP 204)
21. `AKUN-021-BROADNNET-KR-VLESS-WS-91MS` (url=209ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-177MS` (url=221ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-363MS` (url=753ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-404MS` (url=830ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-399MS` (url=878ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
