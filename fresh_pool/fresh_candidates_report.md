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
1. `AKUN-001-DEV-VLESS-WS-84MS` (url=244ms, nekobox=243ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-88MS`
3. `AKUN-002-UNKNOWN-VLESS-WS-112MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-97MS` (url=209ms, nekobox=194ms, status=no)
5. `AKUN-003-UNKNOWN-VLESS-WS-108MS`
6. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-100MS` (url=214ms, nekobox=205ms, status=no)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS` (url=237ms, nekobox=198ms, status=no)
9. `AKUN-005-CLOUDFLARE-VLESS-WS-112MS`
10. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-96MS`
11. `AKUN-007-BIGCOMMERCE-VLESS-WS-111MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-121MS` (url=215ms, nekobox=213ms, status=no)
13. `AKUN-013-SPEEDTEST-VLESS-WS-99MS` (url=231ms, nekobox=205ms, status=no)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-83MS` (url=229ms, nekobox=194ms, status=no)
15. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS`
16. `AKUN-016-CLOUDFLARE-VLESS-WS-104MS` (url=205ms, nekobox=217ms, status=no)
17. `AKUN-009-UNKNOWN-VLESS-WS-101MS`
18. `AKUN-010-UNKNOWN-VLESS-WS-235MS`
19. `AKUN-019-CLOUDFLARE-VLESS-WS-271MS` (url=587ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-270MS` (url=562ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-292MS` (url=643ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-289MS` (url=573ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-265MS` (url=552ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-292MS` (url=565ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-320MS` (url=523ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
