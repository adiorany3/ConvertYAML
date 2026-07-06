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
1. `AKUN-001-UNKNOWN-VLESS-WS-59MS` (url=229ms, nekobox=247ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-63MS` (url=217ms, nekobox=265ms, status=yes)
3. `AKUN-003-CHSL-HEL-VLESS-WS-67MS` (url=257ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-69MS` (url=232ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-68MS` (url=226ms, nekobox=187ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-69MS`
8. `AKUN-007-ZOOM-VLESS-WS-69MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-79MS`
10. `AKUN-009-WEYRO-NET-VLESS-WS-69MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS`
12. `AKUN-012-WPENG-VLESS-WS-68MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-110MS` (url=229ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-70MS` (url=227ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-69MS` (url=237ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-64MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-84MS` (url=273ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-144MS` (url=203ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-83MS` (url=429ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-351MS` (url=737ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-353MS` (url=820ms, status=HTTP 204)
22. `AKUN-022-INTERNETWORKS-45-131-208-VLESS-WS-364MS` (url=790ms, status=HTTP 204)
23. `AKUN-023-CELESTARA-VLESS-WS-365MS` (url=850ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-375MS` (url=743ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-382MS` (url=791ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
