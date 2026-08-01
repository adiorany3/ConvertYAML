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
1. `AKUN-001-UNKNOWN-VLESS-WS-74MS` (url=375ms, nekobox=306ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=278ms, nekobox=312ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=370ms, nekobox=389ms, status=yes)
4. `AKUN-004-008500-VLESS-WS-83MS` (url=281ms, nekobox=312ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-78MS` (url=278ms, nekobox=303ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=323ms, nekobox=349ms, status=yes)
7. `AKUN-007-SPEEDTEST-VLESS-WS-86MS` (url=300ms, nekobox=199ms, status=no)
8. `AKUN-007-UNKNOWN-VLESS-WS-88MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-81MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-90MS`
11. `AKUN-010-ALIBABA-VLESS-WS-90MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-91MS` (url=265ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-84MS` (url=351ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-86MS` (url=313ms, status=HTTP 204)
15. `AKUN-015-PAGES-VLESS-WS-101MS` (url=306ms, status=HTTP 204)
16. `AKUN-017-CCWU-VLESS-WS-150MS` (url=369ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-151MS` (url=347ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-190MS` (url=406ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-236MS` (url=383ms, status=HTTP 204)
20. `AKUN-023-TW-CLOUD-VLESS-WS-323MS` (url=780ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-314MS` (url=642ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-476MS` (url=846ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-510MS` (url=881ms, status=HTTP 204)
24. `AKUN-028-UNKNOWN-VLESS-WS-520MS` (url=1137ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-479MS` (url=763ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
