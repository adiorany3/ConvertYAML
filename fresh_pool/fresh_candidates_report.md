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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=199ms, nekobox=256ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=203ms, nekobox=7177ms, status=no)
3. `AKUN-002-DEV-VLESS-WS-85MS`
4. `AKUN-003-ZVC-VLESS-WS-87MS`
5. `AKUN-004-DEV-VLESS-WS-84MS`
6. `AKUN-005-DEV-VLESS-WS-84MS` (url=246ms, nekobox=230ms, status=yes)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS`
9. `AKUN-008-RTCOMM-SRAVNI-RU-VLESS-WS-94MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-86MS`
11. `AKUN-010-SAVVY-7-VLESS-WS-86MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-97MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-93MS` (url=250ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-108MS` (url=197ms, status=HTTP 204)
15. `AKUN-015-CF-CLIENTS-VLESS-WS-77MS` (url=260ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-89MS` (url=252ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-95MS` (url=202ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-92MS` (url=204ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-107MS` (url=214ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-119MS` (url=227ms, status=HTTP 204)
21. `AKUN-021-POLICE-VLESS-WS-135MS` (url=272ms, status=HTTP 204)
22. `AKUN-022-466688-VLESS-WS-145MS` (url=215ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-148MS` (url=200ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-167MS` (url=286ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-121MS` (url=232ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
