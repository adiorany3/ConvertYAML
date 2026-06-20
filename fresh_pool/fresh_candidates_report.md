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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-83MS` (url=226ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=231ms, nekobox=257ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-100MS` (url=202ms, nekobox=265ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-84MS` (url=205ms, nekobox=208ms, status=no)
5. `AKUN-004-UNKNOWN-VLESS-WS-92MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-113MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-102MS` (url=229ms, nekobox=202ms, status=no)
8. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-154MS` (url=233ms, nekobox=197ms, status=no)
10. `AKUN-007-CLOUDFLARE-VLESS-WS-98MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-244MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-111MS`
14. `AKUN-015-CLOUDFLARE-VLESS-WS-282MS` (url=604ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-356MS` (url=598ms, status=HTTP 204)
16. `AKUN-017-SPEEDTEST-VLESS-WS-286MS` (url=649ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-136MS` (url=250ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-279MS` (url=625ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-411MS` (url=600ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-473MS` (url=815ms, status=HTTP 204)
21. `AKUN-027-UNKNOWN-VLESS-WS-349MS` (url=592ms, status=HTTP 204)
22. `AKUN-030-UNKNOWN-VLESS-WS-250MS` (url=517ms, status=HTTP 204)
23. `AKUN-031-UNKNOWN-VLESS-WS-718MS` (url=882ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-660MS` (url=1958ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-417MS` (url=849ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
