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
1. `AKUN-001-CNAE-VLESS-WS-90MS` (url=246ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-101MS` (url=241ms, nekobox=265ms, status=yes)
3. `AKUN-003-EU-VLESS-WS-84MS` (url=242ms, nekobox=280ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-111MS` (url=252ms, nekobox=267ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-115MS` (url=232ms, nekobox=271ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-105MS` (url=267ms, nekobox=273ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-112MS` (url=258ms, nekobox=279ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-112MS` (url=257ms, nekobox=267ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-80MS` (url=232ms, nekobox=268ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-104MS` (url=238ms, nekobox=270ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=248ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-145MS` (url=242ms, status=HTTP 204)
13. `AKUN-013-GO-DADDY-COM-LLC-VLESS-WS-156MS` (url=257ms, status=HTTP 204)
14. `AKUN-014-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-90MS` (url=235ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-264MS` (url=579ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-267MS` (url=583ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-284MS` (url=630ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-287MS` (url=567ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-306MS` (url=656ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-316MS` (url=665ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-306MS` (url=618ms, status=HTTP 204)
22. `AKUN-026-UNKNOWN-VLESS-WS-556MS` (url=912ms, status=HTTP 204)
23. `AKUN-028-UNKNOWN-VLESS-WS-620MS` (url=1027ms, status=HTTP 204)
24. `AKUN-031-DEV-VLESS-WS-726MS` (url=1064ms, status=HTTP 204)
25. `AKUN-032-UNKNOWN-VLESS-WS-551MS` (url=2235ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
