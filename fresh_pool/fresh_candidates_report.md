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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-79MS` (url=267ms, nekobox=282ms, status=yes)
2. `AKUN-002-CNAE-VLESS-WS-82MS` (url=256ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=258ms, nekobox=292ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-92MS` (url=349ms, nekobox=283ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-96MS` (url=241ms, nekobox=199ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-107MS`
7. `AKUN-006-DIGITALOCEAN-VLESS-WS-75MS`
8. `AKUN-007-CLOUDWEBMANAGE-EU-FR-VLESS-WS-107MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-90MS` (url=256ms, nekobox=188ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-106MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-120MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-122MS` (url=236ms, status=HTTP 204)
14. `AKUN-014-BROADNNET-KR-VLESS-WS-90MS` (url=283ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-103MS` (url=256ms, status=HTTP 204)
16. `AKUN-016-1PASSWORD-VLESS-WS-81MS` (url=252ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-279MS` (url=559ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-284MS` (url=629ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-285MS` (url=660ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-301MS` (url=604ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-305MS` (url=664ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-79MS` (url=251ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-260MS` (url=559ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-271MS` (url=567ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-397MS` (url=606ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
