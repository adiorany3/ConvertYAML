# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 25

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=220ms, nekobox=220ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=226ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-57MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS`
5. `AKUN-005-ZVC-VLESS-WS-90MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-72MS`
7. `AKUN-007-UNKNOWN-VLESS-WS-118MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-64MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-67MS`
11. `AKUN-013-UNKNOWN-VLESS-WS-163MS` (url=220ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-166MS` (url=269ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-237MS` (url=499ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-224MS` (url=1093ms, status=HTTP 204)
15. `AKUN-019-CLOUDFLARE-VLESS-WS-269MS` (url=522ms, status=HTTP 204)
16. `AKUN-022-CLOUDFLARE-VLESS-WS-421MS` (url=686ms, status=HTTP 204)
17. `AKUN-023-CLOUDFLARE-VLESS-WS-420MS` (url=683ms, status=HTTP 204)
18. `AKUN-028-CLOUDFLARE-VLESS-WS-453MS` (url=2172ms, status=HTTP 204)
19. `AKUN-032-CLOUDFLARE-VLESS-WS-519MS` (url=1212ms, status=HTTP 204)
20. `AKUN-033-UNKNOWN-VLESS-WS-517MS` (url=845ms, status=HTTP 204)
21. `AKUN-034-CLOUDFLARE-VLESS-WS-656MS` (url=1363ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
