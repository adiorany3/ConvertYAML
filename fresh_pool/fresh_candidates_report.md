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
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-VULTR-VLESS-WS-61MS` (url=228ms, nekobox=298ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=271ms, nekobox=259ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=248ms, nekobox=257ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=235ms, nekobox=261ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS`
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-61MS`
7. `AKUN-007-VULTR-VLESS-WS-109MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-110MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-159MS`
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-144MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-354MS` (url=777ms, status=HTTP 204)
12. `AKUN-014-WPENG-VLESS-WS-392MS` (url=866ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-369MS` (url=828ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-346MS` (url=814ms, status=HTTP 204)
15. `AKUN-017-SPEEDTEST-VLESS-WS-376MS` (url=861ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-414MS` (url=847ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-417MS` (url=2502ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-402MS` (url=832ms, status=HTTP 204)
19. `AKUN-025-CLOUDFLARE-VLESS-WS-639MS` (url=906ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-647MS` (url=879ms, status=HTTP 204)
21. `AKUN-029-CLOUDFLARE-VLESS-WS-619MS` (url=999ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
