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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-194MS` (url=1456ms, nekobox=421ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-247MS` (url=656ms, nekobox=979ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-196MS` (url=956ms, nekobox=617ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-195MS` (url=762ms, nekobox=438ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-224MS` (url=452ms, nekobox=3470ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-234MS` (url=618ms, nekobox=674ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-251MS` (url=369ms, nekobox=433ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-242MS` (url=1209ms, nekobox=425ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-265MS` (url=665ms, nekobox=916ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-278MS` (url=415ms, nekobox=2558ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-196MS` (url=360ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-267MS` (url=439ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-261MS` (url=414ms, status=HTTP 204)
14. `AKUN-014-ZOOM-VLESS-WS-355MS` (url=423ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-265MS` (url=1017ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-214MS` (url=858ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-379MS` (url=737ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-317MS` (url=429ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-532MS` (url=2050ms, status=HTTP 204)
20. `AKUN-020-UK-GB-DCL-01-20191003-VLESS-WS-509MS` (url=1531ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-576MS` (url=1069ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-573MS` (url=1444ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-537MS` (url=381ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-275MS` (url=598ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-449MS` (url=458ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
