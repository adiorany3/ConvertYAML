# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 24

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
1. `AKUN-001-ICOOK-VLESS-WS-87MS` (url=202ms, nekobox=260ms, status=yes)
2. `AKUN-002-ICOOK-VLESS-WS-90MS` (url=233ms, nekobox=287ms, status=yes)
3. `AKUN-003-ZOOM-VLESS-WS-96MS` (url=221ms, nekobox=237ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-111MS` (url=212ms, nekobox=275ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-115MS` (url=211ms, nekobox=247ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS` (url=210ms, nekobox=245ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-100MS` (url=220ms, nekobox=279ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-117MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-112MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-167MS`
11. `AKUN-013-UNKNOWN-VLESS-WS-106MS` (url=216ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-95MS` (url=224ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-370MS` (url=775ms, status=HTTP 204)
14. `AKUN-017-LEVIKOGJGFDD-VLESS-WS-434MS` (url=894ms, status=HTTP 204)
15. `AKUN-020-CLOUDFLARE-VLESS-WS-578MS` (url=1354ms, status=HTTP 204)
16. `AKUN-021-CLOUDFLARE-VLESS-WS-710MS` (url=1105ms, status=HTTP 204)
17. `AKUN-023-UNKNOWN-VLESS-WS-737MS` (url=1184ms, status=HTTP 204)
18. `AKUN-029-CLOUDFLARE-VLESS-WS-690MS` (url=1110ms, status=HTTP 204)
19. `AKUN-031-UNKNOWN-VLESS-WS-878MS` (url=1202ms, status=HTTP 204)
20. `AKUN-032-CLOUDFLARE-VLESS-WS-722MS` (url=1211ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
