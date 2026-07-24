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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-55MS` (url=226ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-57MS` (url=219ms, nekobox=258ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS` (url=220ms, nekobox=248ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-60MS` (url=246ms, nekobox=252ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=243ms, nekobox=245ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS` (url=219ms, nekobox=277ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS` (url=216ms, nekobox=258ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS` (url=340ms, nekobox=300ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-63MS` (url=213ms, nekobox=250ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-71MS` (url=337ms, nekobox=295ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-98MS` (url=237ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-83MS` (url=226ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-82MS` (url=267ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-106MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-80MS` (url=291ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-87MS` (url=235ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-65MS` (url=217ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-120MS` (url=291ms, status=HTTP 204)
19. `AKUN-019-ZVC-VLESS-WS-69MS` (url=225ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-114MS` (url=283ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-111MS` (url=279ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-96MS` (url=201ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-113MS` (url=265ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-108MS` (url=280ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-162MS` (url=229ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
