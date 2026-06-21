# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-128MS` (url=257ms, nekobox=298ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-138MS` (url=291ms, nekobox=315ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-143MS` (url=272ms, nekobox=315ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-143MS` (url=271ms, nekobox=291ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-144MS` (url=294ms, nekobox=291ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-156MS` (url=297ms, nekobox=304ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-143MS` (url=316ms, nekobox=298ms, status=yes)
8. `AKUN-008-DEV-VLESS-WS-141MS` (url=251ms, nekobox=227ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-141MS`
10. `AKUN-009-VULTR-VLESS-WS-182MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-167MS`
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-174MS` (url=263ms, status=HTTP 204)
13. `AKUN-013-GO-DADDY-COM-LLC-VLESS-WS-167MS` (url=266ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-349MS` (url=693ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-383MS` (url=788ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-402MS` (url=779ms, status=HTTP 204)
17. `AKUN-017-SPEEDTEST-VLESS-WS-390MS` (url=753ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-394MS` (url=774ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-359MS` (url=705ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-376MS` (url=750ms, status=HTTP 204)
21. `AKUN-029-CLOUDFLARE-VLESS-WS-674MS` (url=1108ms, status=HTTP 204)
22. `AKUN-031-BIGCOMMERCE-VLESS-WS-630MS` (url=966ms, status=HTTP 204)
23. `AKUN-034-CLOUDFLARE-VLESS-WS-757MS` (url=1247ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
