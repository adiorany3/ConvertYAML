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
1. `AKUN-001-ALIBABA-VLESS-WS-71MS` (url=209ms, nekobox=246ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS` (url=210ms, nekobox=247ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=216ms, nekobox=225ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS` (url=221ms, nekobox=229ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=217ms, nekobox=238ms, status=yes)
6. `AKUN-006-466688-VLESS-WS-91MS` (url=225ms, nekobox=256ms, status=yes)
7. `AKUN-007-466688-VLESS-WS-113MS` (url=222ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS` (url=219ms, nekobox=226ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-112MS` (url=216ms, nekobox=276ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-120MS` (url=226ms, nekobox=250ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-88MS` (url=227ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-181MS` (url=378ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-233MS` (url=498ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-229MS` (url=496ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-267MS` (url=575ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-281MS` (url=575ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-276MS` (url=605ms, status=HTTP 204)
18. `AKUN-018-NODEJS-VLESS-WS-81MS` (url=230ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-277MS` (url=608ms, status=HTTP 204)
20. `AKUN-020-COMPREND-NET-VLESS-WS-89MS` (url=235ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-294MS` (url=609ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-225MS` (url=908ms, status=HTTP 204)
23. `AKUN-023-COMPREND-NET-VLESS-WS-127MS` (url=226ms, status=HTTP 204)
24. `AKUN-030-RS-RAPIDSEEDBOX-20190717-VLESS-WS-519MS` (url=5819ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-521MS` (url=933ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
